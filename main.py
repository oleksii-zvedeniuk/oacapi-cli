from src import parser, models, api_manager, query_builder


def main() -> None:
    arguments = parser.parser.parse_args()

    query = query_builder.QueryBuilder(
        arguments.catalog,
        models.QueryFilters.from_object(arguments),
        models.BaseQueryParams.from_object(arguments),
        models.BoolQueryParams.from_object(arguments),
        models.SpecialQueryParams.from_object(arguments),
    ).build()

    print(api_manager.make_request(query))


if __name__ == "__main__":
    main()
