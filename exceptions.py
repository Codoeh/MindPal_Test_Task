class BorderSizeException(Exception):
    def __init__(self, max_border, *args):
        super().__init__(f"Border size must be between 0 and {max_border}")


class PositiveNumberException(Exception):
    def __init__(self, value):
        super().__init__(f"Value must be greater than 0. Got: {value}")


class MissingKeyException(Exception):
    def __init__(self, missing_keys, invalid_dict, *args):
        missing_keys_str = ", ".join(missing_keys)
        super().__init__(f"Missing keys: \"{missing_keys_str}\""
                         f" in {invalid_dict}")


class TypesException(Exception):
    def __init__(self, expected_type, invalid_data, *args):
        super().__init__(f"Wrong input type for {invalid_data}.\n"
                         f"Expected: {expected_type.__name__}.\n"
                         f"Got: {type(invalid_data).__name__}.")
