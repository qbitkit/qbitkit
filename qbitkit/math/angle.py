from math import pi as __pi__


def deg2rad(degrees=180):
    """Converts :math:`x` degrees to :math:`y` radians using: :math:`x*\pi/180=y`"""
    # Multiply the specified number of degrees by pi/180.
    radians = degrees * __pi__ / 180
    return radians