import matplotlib

from validators import (
    dict_keys_validator,
    positive_number_validator,
    border_size_validator,
    objects_type_validator,
    REQUIRED_KEYS_EXISTING,
    REQUIRED_KEYS_NEW
)
from visualisation import objects_locator
matplotlib.use("TkAgg")


def find_fitting_objects(
        plot_width: float,
        plot_length: float,
        restricted_border: float,
        existing_objects: list[dict],
        new_objects: list[dict]
) -> dict:

    positive_number_validator(
        plot_width, plot_length, restricted_border
    )

    border_size_validator(
        plot_width=plot_width,
        plot_length=plot_length,
        restricted_border=restricted_border
    )

    objects_type_validator(existing_objects, new_objects)

    for obj in existing_objects:
        dict_keys_validator(REQUIRED_KEYS_EXISTING, obj)
        positive_number_validator(obj["length"], obj["width"])

    for obj in new_objects:
        dict_keys_validator(REQUIRED_KEYS_NEW, obj)
        positive_number_validator(obj["length"], obj["width"])

    total_area = plot_width * plot_length
    print("Total area:", total_area)

    usable_area = ((plot_width - 2 * restricted_border) *
                   (plot_length - 2 * restricted_border))
    print("Usable area:", usable_area)

    existing_objects_areas = [
        obj.get("length") * obj.get("width") for obj in existing_objects
    ]
    print("Area of existing objects:", existing_objects_areas)

    free_space = round(usable_area - sum(existing_objects_areas), 2)
    print("Free space:", free_space)

    new_objects_areas = {
        elem.get("name"): (elem.get("width") * elem.get("length"))
        for elem in new_objects
    }
    print("Area for new objects:", new_objects_areas)

    result = {
        "free_space": free_space,
        "fitting_objects": [],
    }
    if free_space < 0:
        result["free_space"] = 0.0
        return result

    print("Result before iteration:", result)
    for key, value in new_objects_areas.items():
        if value <= result["free_space"]:
            result["free_space"] -= value
            result["fitting_objects"].append(key)
            print("Result in iteration:", result)
        else:
            continue

    # Create visualisation
    objects_locator(
        plot_width=plot_width,
        plot_length=plot_length,
        restricted_border=restricted_border,
        existing_objects=existing_objects,
        new_objects=new_objects,
        result=result
    )

    return result


if __name__ == "__main__":
    find_fitting_objects(
        plot_width=50,
        plot_length=100,
        restricted_border=4,
        existing_objects=[
            {"width": 10, "length": 20},
            {"width": 5, "length": 5}
        ],
        new_objects=[
            {"name": "Shed", "width": 10, "length": 10},
            {"name": "Garage", "width": 20, "length": 30},
            {"name": "Cabin", "width": 15, "length": 15}
        ]
    )
