"""Global configuration."""

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


configuration = load_configuration("config_02.yaml")

configuration.dump("config_02.json")
