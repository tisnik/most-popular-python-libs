# Knihovna Pydantic
#
# - model s konfigurací obsahující čtyři atributy
# - kontrola obsahu atributů po inicializaci modelu
# - zákaz inicializace modelu s neznámými atributy
# - funkce pro načtení konfigurace ze souboru typu YAML

import yaml
from typing_extensions import Self

from pydantic import (
    BaseModel,
    ConfigDict,
    PositiveInt,
    model_validator,
)


class ConfigurationBase(BaseModel):
    """Base class for all configuration models that rejects unknown fields."""

    model_config = ConfigDict(extra="forbid")


class ServiceConfiguration(ConfigurationBase):
    """Service configuration."""

    host: str = "localhost"
    port: PositiveInt = 8080
    auth_enabled: bool = False
    workers: PositiveInt = 1

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
    with open(filename, encoding="utf-8") as fin:
        config_dict = yaml.safe_load(fin)
        return Configuration(**config_dict)


configuration = load_configuration("config_05.yaml")

configuration.dump("config_05.json")
