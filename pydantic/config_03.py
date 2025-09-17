# Knihovna Pydantic
#
# - model s konfigurací obsahující jediný atribut
# - metoda modelu pro uložení konfigurace do souboru typu JSON
# - funkce pro načtení konfigurace ze souboru typu YAML

import yaml

from pydantic import (
    BaseModel,
)


class Configuration(BaseModel):
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


configuration = load_configuration("config_03.yaml")

configuration.dump("config_03.json")
