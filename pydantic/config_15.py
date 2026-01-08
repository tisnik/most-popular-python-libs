# Knihovna Pydantic
#
# - model s konfigurací obsahující čtyři atributy
# - jeden z atributů je tvořen dalším modelem
# - kontrola obsahu atributů po inicializaci modelu
# - zákaz inicializace modelu s neznámými atributy
# - úprava schématu do podoby OpenAPI
# - řešení atributu exclusiveMinimum
# - řešení volitelné hodnoty
# - export schématu modelu

import json
from typing_extensions import Optional, Self

from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
    FilePath,
    PositiveInt,
    model_validator,
)
from pydantic.json_schema import models_json_schema


# PostgreSQL connection constants
# See: https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNECT-SSLMODE
POSTGRES_DEFAULT_SSL_MODE = "prefer"
# See: https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNECT-GSSENCMODE
POSTGRES_DEFAULT_GSS_ENCMODE = "prefer"


class ConfigurationBase(BaseModel):
    """Base class for all configuration models that rejects unknown fields."""

    model_config = ConfigDict(extra="forbid")


class DatabaseConfiguration(ConfigurationBase):
    """Database configuration."""

    host: str = Field(
        "localhost",
        title="Hostname",
        description="Database server host or socket directory",
    )

    port: PositiveInt = Field(
        5432,
        title="Port",
        description="Database server port",
    )

    db: str = Field(
        ...,
        title="Database name",
        description="Database name to connect to",
    )

    user: str = Field(
        ...,
        title="User name",
        description="Database user name used to authenticate",
    )

    password: str = Field(
        ...,
        title="Password",
        description="Password used to authenticate",
    )

    ssl_mode: str = Field(
        POSTGRES_DEFAULT_SSL_MODE,
        title="SSL mode",
        description="SSL mode",
    )

    gss_encmode: str = Field(
        POSTGRES_DEFAULT_GSS_ENCMODE,
        title="GSS encmode",
        description="This option determines whether or with what priority a secure GSS "
        "TCP/IP connection will be negotiated with the server.",
    )

    ca_cert_path: Optional[FilePath] = Field(
        None,
        title="CA certificate path",
        description="Path to CA certificate",
    )

    @model_validator(mode="after")
    def check_postgres_configuration(self) -> Self:
        """Check PostgreSQL configuration."""
        if self.port > 65535:
            raise ValueError("Port value should be less than 65536")
        return self


class ServiceConfiguration(ConfigurationBase):
    """Service configuration."""

    host: str = Field(
        "localhost",
        title="Host",
        description="Service hostname",
    )

    port: PositiveInt = 8080
    port: PositiveInt = Field(
        8080,
        title="Port",
        description="Service port",
    )

    auth_enabled: bool = Field(
        False,
        title="Authentication enabled",
        description="Enables authentication subsystem",
    )

    workers: PositiveInt = Field(
        1,
        title="Number of workers",
        description="Number of workers to be started",
    )

    database: DatabaseConfiguration = Field(
        ...,
        title="Database configuration",
        description="Database configuration",
    )

    @model_validator(mode="after")
    def check_service_configuration(self) -> Self:
        """Check service configuration."""
        if self.port > 65535:
            raise ValueError("Port value should be less than 65536")
        return self


class Configuration(ConfigurationBase):
    """Global configuration."""

    name: str = Field(
        ...,
        title="Service name",
        description="Service name",
    )

    service: ServiceConfiguration = Field(
        ...,
        title="Service configuration",
        description="Service configuration",
    )

    def dump(self, filename: str = "configuration.json") -> None:
        """Dump actual configuration into JSON file."""
        with open(filename, "w", encoding="utf-8") as fout:
            fout.write(self.model_dump_json(indent=4))


def recursive_update(original: dict) -> dict:
    new = {}
    for key, value in original.items():
        # rekurzivní průchod podslovníky
        if isinstance(value, dict):
            new[key] = recursive_update(original[key])
        # řešení volitelných typů
        elif key == "anyOf" and isinstance(value, list) and value[1]["type"] == "null":
            # jen první typ je konktrétní, ingorovat druhý
            val = value[0]["type"]
            new["type"] = val
            # nový atribut
            new["nullable"] = True
        # řešení atributu exclusiveMinimum
        elif key == "exclusiveMinimum":
            new["minimum"] = value
        else:
            new[key] = value
    return new


with open("schema_15.json", "w") as fout:
    _, schemas = models_json_schema(
        [(model, "validation") for model in [Configuration]],
        ref_template="#/components/schemas/{model}",
    )
    schemas = recursive_update(schemas)
    openapi_schema = {
        "openapi": "3.0.0",
        "info": {
            "title": "Weyland-Yutani Information System",
            "version": "0.3.0",
        },
        "components": {
            "schemas": schemas.get("$defs"),
        },
        "paths": {},
    }
    json.dump(openapi_schema, fout)
