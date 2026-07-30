def get_schema(data):

    if len(data) == 0:
        return []

    return list(data[0].keys())