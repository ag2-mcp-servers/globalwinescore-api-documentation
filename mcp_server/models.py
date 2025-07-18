# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T00:33:56+00:00

from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import RootModel


class Color(Enum):
    red = 'red'
    white = 'white'
    pink = 'pink'


class Ordering(Enum):
    date = 'date'
    field_date = '-date'
    score = 'score'
    field_score = '-score'


class WineId(RootModel[List[int]]):
    root: List[int]
