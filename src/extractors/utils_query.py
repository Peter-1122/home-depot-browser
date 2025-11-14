thondef parse_query(query: str):
    """
    Returns tuple: (query_type, value)
    Supports:
    - product:12345
    - store:6789
    - keyword text
    """
    if ":" in query:
        prefix, value = query.split(":", 1)
        prefix = prefix.lower()

        if prefix == "product":
            return "product", value
        if prefix == "store":
            return "store", value

    return "keyword", query