# Knihovna Pydantic
#
# - model s konfigurací obsahující jediný atribut
# - zákaz inicializace modelu s neznámými atributy
# - metoda modelu pro uložení konfigurace do souboru typu JSON
# - funkce pro načtení konfigurace ze souboru typu YAML


import yaml

from pydantic import (
    BaseModel,
    ConfigDict,
)


class ConfigurationBase(BaseModel):
    """Base class for all configuration models that rejects unknown fields."""

    model_config = ConfigDict(extra="forbid")


class Configuration(ConfigurationBase):
    """Global configuration."""

    name: str

    def dump(self, filename: str = "configuration.json") -> None:
        """Dump actual configuration into JSON file."""
        with open(filename, "w", encoding="utf-8") as fout:
            fout.write(self.model_dump_json(indent=4))


def load_configuration(filename: str) -> Configuration:
    """Load configuration from YAML file."""
    with open(filename, encoding="utf-8") as fin:
        config_dict = yaml.safe_load(fin)
        return Configuration(**config_dict)


configuration = load_configuration("config_04.yaml")

configuration.dump("config_04.json")
