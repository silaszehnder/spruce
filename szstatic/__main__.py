import argparse
import logging
import pathlib
import sys

from typing import List
from config import Config


def build(args: argparse.Namespace) -> int:
    config = Config(args.config)
    print(config)


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="A no-nonsense static site generator.")
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase output verbosity. Pass multiple times to increase output "
        "further.",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        default=0,
        action="count",
        help="Decrease output verbosity. Pass multiple times to reduce output further.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_build = subparsers.add_parser("build", help="build command help")
    parser_build.add_argument(
        "-c",
        "--config",
        type=pathlib.Path,
        help="Config file location.",
        default="config.toml",
    )
    parser_build.set_defaults(func=build)

    args = parser.parse_args(argv)

    logging_levels = [
        logging.DEBUG,
        logging.INFO,
        logging.WARNING,
        logging.ERROR,
        logging.CRITICAL,
    ]
    verbosity = logging_levels.index(logging.INFO) - args.verbose + args.quiet
    verbosity = max(0, min(verbosity, len(logging_levels) - 1))
    logging.basicConfig(
        format="",
        level=logging_levels[verbosity],
    )

    return args


def validate_args(args: argparse.Namespace) -> argparse.Namespace:
    return args


def main(argv: List[str]) -> int:
    args = parse_args(argv)
    args = validate_args(args)
    return args.func(args)


if __name__ == "__main__":
    exit(main(sys.argv[1:]))
