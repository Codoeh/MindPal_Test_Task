import random
import matplotlib.pyplot as plt
from matplotlib.patches import Patch


def place_object(
        width,
        length,
        plot_width,
        plot_length,
        restricted_border
):
    """
    Choose random (x, y) coordinates to place an object inside the plot,
    ensuring it stays within the restricted border area.
    Note: This function does not check for collisions with other objects.
    """
    x = random.uniform(
        restricted_border,
        plot_width - restricted_border - width
    )
    y = random.uniform(
        restricted_border,
        plot_length - restricted_border - length
    )

    return x, y


def objects_locator(
        plot_width: float,
        plot_length: float,
        restricted_border: float,
        existing_objects: list[dict],
        new_objects: list[dict],
        result: dict
):
    """
    Visualize existing and newly fitting objects on a plot.

    The function draws:
    - outline of the land plot,
    - existing objects placed randomly,
    - new objects that fit (based on `result["fitting_objects"]`),
    - the inner restricted border area.
    """

    # Create a plot
    plt.figure(figsize=(plot_width / 5, plot_length / 5))
    ax = plt.gca()
    ax.set_xlim(0, plot_width)
    ax.set_ylim(0, plot_length)
    ax.set_aspect("equal")

    # Create a land plot
    plot_rect = plt.Rectangle(
        (0, 0),
        plot_width,
        plot_length,
        edgecolor="black",
        facecolor="none",
        linewidth=2
    )
    ax.add_patch(plot_rect)

    # Create restricted border
    border_rect = plt.Rectangle(
        (restricted_border, restricted_border),
        plot_width - 2 * restricted_border,
        plot_length - 2 * restricted_border,
        edgecolor="red",
        facecolor="none",
        linewidth=2
    )
    ax.add_patch(border_rect)

    # Existing objects
    for obj in existing_objects:
        # Chose random placement for objects
        x, y = place_object(
            width=obj["width"],
            length=obj["length"],
            plot_width=plot_width,
            plot_length=plot_length,
            restricted_border=restricted_border
        )

        # Create existing object
        existing_rect = plt.Rectangle(
            (x, y),
            width=obj["width"],
            height=obj["length"],
            edgecolor="blue",
            facecolor="none",
            linewidth=2,
        )
        ax.add_patch(existing_rect)

    # New objects
    for obj in new_objects:
        if obj["name"] in result["fitting_objects"]:
            print(obj)
            # Chose random placement for new objects
            x, y = place_object(
                width=obj["width"],
                length=obj["length"],
                plot_length=plot_length,
                plot_width=plot_width,
                restricted_border=restricted_border,
            )

            # Create new objects
            new_rect = plt.Rectangle(
                (x, y),
                width=obj["width"],
                height=obj["length"],
                edgecolor="green",
                facecolor="none",
            )
            center_x = x + obj["width"] / 2
            center_y = y + obj["length"] / 2
            ax.text(
                center_x,
                center_y,
                obj["name"],
                color="green",
                ha="center",
                va="center",
                fontsize=8
            )
            ax.add_patch(new_rect)


    # Create legend on plot
    legend_elements = [
        Patch(
            facecolor="none",
            edgecolor="blue",
            label="Existing objects"
        ),
        Patch(
            facecolor="none",
            edgecolor="green",
            label="Fitting new objects"
        ),
        Patch(
            facecolor="none",
            edgecolor="red",
            label="Restricted border"
        ),
    ]

    ax.legend(handles=legend_elements, loc="upper right")
    plt.show()
