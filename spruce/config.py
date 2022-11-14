import logging
import pathlib
import pprint
import tomllib


DEFAULT_CONFIG = {
    "implicit_tagging": True,
    "all_posts_page": True,
    "default_layout": "default.html",
    "asset_directory": "assets",
    "content_directory": "content",
    "entrypoint": "index.md",
}

REQUIRED_CONFIG = {
    "name",
    "domain",
}


class Config(object):
    def __init__(self, conf_path: pathlib.Path):
        with open(conf_path, "rb") as conf_file:
            user_config = tomllib.load(conf_file)

        for req in REQUIRED_CONFIG:
            if req not in user_config:
                raise Exception(f"Config {conf_path} missing a configuration for {req}")

        user_config = DEFAULT_CONFIG | user_config
        self.__dict__.update(user_config)

    def __str__(self):
        return pprint.pformat(self.__dict__, indent=4)


def parse(conf_path: pathlib.Path) -> dict:
    return {}
