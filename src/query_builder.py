from typing import Union

from src import constants, models


class QueryBuilder:
    def __init__(
        self,
        catalog: str,
        filters: models.QueryPartBase,
        base_params: models.QueryPartBase,
        bool_params: models.QueryPartBase,
        special_params: models.QueryPartBase,
    ) -> None:
        self.filters = filters
        self.base_params = base_params
        self.bool_params = bool_params
        self.special_params = special_params
        self.query = constants.QUERY_BASE.format(catalog=catalog)

    def build(self) -> str:
        self._extend_query(format(self.base_params), "?")
        self._extend_query(format(self.filters), "&")
        self._extend_query(format(self.special_params), "&")
        self._extend_query(format(self.bool_params))
        return self.query

    def _extend_query(self, part: str, end: Union[str, None] = None) -> None:
        if part:
            self.query = "".join(filter(None, (self.query, part, end)))
