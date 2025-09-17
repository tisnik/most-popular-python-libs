# Knihovna Pydantic
#
# - model s konfigurací obsahující pět atributů
# - jeden z atributů je tvořen dalším modelem
# - kontrola obsahu atributů po inicializaci modelu
# - atributy typu řetězec, které mohou nabývat jen několika hodnot
# - zákaz inicializace modelu s neznámými atributy
# - funkce pro načtení konfigurace ze souboru typu YAML s expanzí proměnných prostředí


import os

from pyaml_env import parse_config

from typing_extensions import Self, Optional, Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    PositiveInt,
    model_validator,
    FilePath,
)


# PostgreSQL connection constants
# See: https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNECT-SSLMODE
POSTGRES_DEFAULT_SSL_MODE = "prefer"
# See: https://www.postgresql.org/docs/current/libpq-connect.html#LIBPQ-CONNECT-GSSENCMODE
POSTGRES_DEFAULT_GSS_ENCMODE = "prefer"


class InvalidConfigurationError(Exception):
    """Lightspeed configuration is invalid."""


def get_attribute_from_file(file_path: FilePath) -> Optional[str]:
    """Retrieve value of an attribute from a file."""
    with open(file_path, encoding="utf-8") as f:
        return f.read().rstrip()


def file_check(file_path: FilePath) -> None:
    """Check that path is a readable regular file."""
    if not os.path.isfile(file_path):
        raise InvalidConfigurationError(f"{desc} '{path}' is not a file")
    if not os.access(file_path, os.R_OK):
        raise InvalidConfigurationError(f"{desc} '{path}' is not readable")


class ConfigurationBase(BaseModel):
    """Base class for all configuration models that rejects unknown fields."""

    model_config = ConfigDict(extra="forbid")


class DatabaseConfiguration(ConfigurationBase):
    """Database configuration."""

    host: str = "localhost"
    port: PositiveInt = 5432
    db: str
    user: str
    password: str = None
    password_file: FilePath
    ssl_mode: Literal[
        "disable", "allow", "prefer", "require", "verify-ca", "verify-full"
    ] = POSTGRES_DEFAULT_SSL_MODE
    gss_encmode: Literal["disable", "prefer", "require"] = POSTGRES_DEFAULT_GSS_ENCMODE
    ca_cert_path: Optional[FilePath] = None

    @model_validator(mode="after")
    def check_postgres_configuration(self) -> Self:
        """Check PostgreSQL configuration."""
        if self.port > 65535:
            raise ValueError("Port value should be less than 65536")
        file_check(self.password_file)
        self.password = get_attribute_from_file(self.password_file)
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


def load_configuration(filename: str) -> Configuration:
    """Load configuration from YAML file."""
    config_dict = parse_config(filename)
    return Configuration(**config_dict)


configuration = load_configuration("config_09.yaml")

configuration.dump("config_09.json")

configuration = load_configuration("config_09_wrong.yaml")
