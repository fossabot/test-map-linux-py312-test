# SPDX-FileCopyrightText: © 2024 Romain Brault <mail@romainbrault.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

"""Manage environment variables."""

import logging
from pathlib import Path
from typing import Final

import dotenv


__all__: Final = ["ENVIRONMENT_FILE", "load_dotenv"]

ENVIRONMENT_FILE: Final = Path(".env")


def load_dotenv(environment_file: Path) -> None:
    """Load a dotenv file to os.environ.

    Args:
        environment_file: the dotenv file to load.
    """
    if dotenv.load_dotenv(environment_file):
        logging.getLogger(__name__).info(
            "Loading environment variables from `%s` file.", environment_file
        )
