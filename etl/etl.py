def transform(legacy_data):
    new_data = {}
    for point in legacy_data:
        for value in legacy_data[point]:
            new_data[value.lower()] = point
    return new_data