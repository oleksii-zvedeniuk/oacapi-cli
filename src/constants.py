from enum import Enum

DEFAULT_OBJECT = "catalog"

QUERY_BASE = "https://api.{catalog}.space/"


class Catalog(Enum):
    """Available catalog names."""

    ASTROCATS = "astrocats"
    SNE = "sne"
    TDE = "tde"
    KILONOVA = "kilonova"
    FASTSTARS = "faststars"


class OutputFormat(Enum):
    """Available output formats."""

    JSON = "json"
    CSV = "csv"
    TSV = "tsv"
