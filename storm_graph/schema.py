# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Storm Project.
#
# storm-graph is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

import json
from jsonschema import validate

from typing import Dict

from pathlib import Path
from pkg_resources import resource_string


def _schema_from_resource() -> Dict:
    """Load a schema from the package resources."""
    from .config import SchemaResourceConfig

    _path = (
        Path(SchemaResourceConfig.SCHEMA_RESOURCE_DIRECTORY)
        / SchemaResourceConfig.SCHEMA_SPEC_VERSION
        / SchemaResourceConfig.SCHEMA_RESOURCE_NAME
    )

    _schema = resource_string(__name__, _path.as_posix())
    return json.loads(_schema)


def validate_schema(instance: Dict):
    """Validate a object based on a JSON Schema."""
    schema_object = _schema_from_resource()
    validate(instance=instance, schema=schema_object)


__all__ = "validate_schema"
