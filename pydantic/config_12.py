# Knihovna Pydantic
#
# - model s konfigurací obsahující čtyři atributy
# - jeden z atributů je tvořen dalším modelem
# - kontrola obsahu atributů po inicializaci modelu
# - zákaz inicializace modelu s neznámými atributy
# - úprava schématu do podoby OpenAPI
# - export schématu modelu

import json
from typing_extensions import Optional, Self

from pydantic import (
    BaseModel,
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

    host: str = "localhost"
    port: PositiveInt = 5432
    db: str
    user: str
    password: str
    ssl_mode: str = POSTGRES_DEFAULT_SSL_MODE
    gss_encmode: str = POSTGRES_DEFAULT_GSS_ENCMODE
    ca_cert_path: Optional[FilePath] = None

    @model_validator(mode="after")
    def check_postgres_configuration(self) -> Self:
        """Check PostgreSQL configuration."""
        if self.port > 65535:
            raise ValueError("Port value should be less than 65536")
        return self


class ServiceConfiguration(ConfigurationBase):
    """Service configuration."""

    host: str = "localhost"
    port: PositiveInt = 8080
    auth_enabled: bool = False
    workers: PositiveInt = 1
    database: DatabaseConfiguration

    @model_validator(mode="after")
    def check_service_configuration(self) -> Self:
        """Check service configuration."""
        if self.port > 65535:
            raise ValueError("Port value should be less than 65536")
        return self


class Configuration(ConfigurationBase):
    """Global configuration."""

    name: str
    service: ServiceConfiguration

    def dump(self, filename: str = "configuration.json") -> None:
        """Dump actual configuration into JSON file."""
        with open(filename, "w", encoding="utf-8") as fout:
            fout.write(self.model_dump_json(indent=4))


with open("schema_12.json", "w") as fout:
    _, schemas = models_json_schema(
        [(model, "validation") for model in [Configuration]],
        ref_template="#/components/schemas/{model}",
    )
    openapi_schema = {
        "openapi": "3.0.0",
        "info": {
            "title": "Weyland-Yutani Information System",
            "version": "0.3.0",
        },
        "components": {
            "schemas": schemas.get('$defs'),
        },
        "paths": {},
    }
    json.dump(openapi_schema, fout)
