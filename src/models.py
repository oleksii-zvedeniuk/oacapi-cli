from __future__ import annotations
from dataclasses import dataclass, fields
from typing import Any, Generator


class QueryPartBase:
    def __iter__(self) -> Generator:
        for field in fields(self):
            if value := getattr(self, field.name):
                yield field.name, value

    @classmethod
    def from_object(cls, obj: Any) -> QueryPartBase:
        return cls(**{f.name: getattr(obj, f.name) for f in fields(cls)})


@dataclass
class SpecialQueryParams(QueryPartBase):
    format: str
    item: str = None
    sortby: str = None

    def __format__(self, __format_spec: str) -> str:
        return "&".join(f"{field_name}={value}" for field_name, value in self)


@dataclass
class BaseQueryParams(QueryPartBase):
    objects: list
    quantities: list
    attributes: list

    def __format__(self, __format_spec: str) -> str:
        formatted = []
        for _, value in self:
            formatted.append("+".join(value_part for value_part in value))
        return "/".join(value for value in formatted)


@dataclass
class QueryFilters(QueryPartBase):
    filters: list

    def __format__(self, __format_spec: str) -> str:
        return "&".join(filter_ for filter_ in self.filters)


@dataclass
class BoolQueryParams(QueryPartBase):
    first: bool
    closest: bool
    complete: bool

    def __format__(self, __format_spec: str) -> str:
        return "&".join(field_name for field_name, _ in self)
