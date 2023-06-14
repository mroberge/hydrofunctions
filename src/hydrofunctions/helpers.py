"""
hydrofunctions.helpers
~~~~~~~~~~~~~~~~~~~~~~

This module holds functions designed to help out the user in an IPython
session.

-----
"""
from IPython.core.display import HTML


def draw_map(width=700, height=400, url="http://hydrocloud.org"):
    """Draws a map of stream gages in a Jupyter Notebook.

    This function will draw an interactive map of stream gages from
    hydrocloud.org into an iframe and display it in a Jupyter Notebook.
    Each dot represents a stream gage. Click on the dot to learn its name,
    which you can use to request data.

    Args:
        width (int): The width of the map iframe.
        height (int): The height of the map iframe.
        url (str): The URL to put inside of the IFrame. Defaults to\
        https://hydrocloud.org

    Returns:
        HTML display object.

    **Example:**

        >>> import hydrofunctions as hf
        >>> hf.draw_map()

        A map appears.

        >>> hf.draw_map(width=900, height=600)

        Draws a larger map.
"""
    #    TODO:
    #        use ipywidgets to allow users to click on the map, and this will
    #        return a value that can be used in another IPython cell. This
    #        feature would allow the map to act as an interactive site selection
    #        tool.

    output = HTML(
        '<p>Use <a href="http://hydrocloud.org" target="_blank">'
        "HydroCloud.org</a> to find a stream gauge. "
        "Click on the dots to learn more about a site.</p>"
        "<iframe src=http://hydrocloud.org/ width={} height={}>"
        "</iframe>".format(width, height)
    )

    return output


def count_number_of_truthy(my_list):
    return sum(bool(item) for item in my_list)
