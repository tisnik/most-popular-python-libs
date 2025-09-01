"""Global configuration."""

import yaml

from pydantic import (
    BaseModel,
)


class Configuration(BaseModel):
    """Global configuration."""

    name: str


def load_configuration(filename: str) -> Configuration:
    """Load configuration from YAML file."""
    with open(filename, encoding="utf-8") as fin:
        config_dict = yaml.safe_load(fin)
        return Configuration(**config_dict)


configuration = load_configuration("config_01.yaml")
print(configuration)
