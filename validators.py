from exceptions import (
    BorderSizeException,
    PositiveNumberException,
    MissingKeyException,
    TypesException
)

MIN_BORDER_SIZE = 0
MIN_VALUE = 0
REQUIRED_KEYS_EXISTING = {"width", "length"}
REQUIRED_KEYS_NEW = {"name", "width", "length"}


def border_size_validator(
        plot_width: float,
        plot_length: float,
        restricted_border: float
):
    max_allowed_border = min(plot_width / 2, plot_length / 2)

    if (restricted_border <= MIN_BORDER_SIZE) or (
            restricted_border >= max_allowed_border):
        raise BorderSizeException(max_allowed_border)


def positive_number_validator(*values):
    for value in values:
        if value <= MIN_VALUE:
            raise PositiveNumberException(value)


def dict_keys_validator(required_keys, *args):
    for arg in args:
        missing = required_keys - set(arg.keys())
        if missing:
            raise MissingKeyException(missing, arg)


def objects_type_validator(*args):
    for arg in args:
        if not isinstance(arg, list):
            raise TypesException(list, arg)
        for element in arg:
            if not isinstance(element, dict):
                raise TypesException(dict, element)
