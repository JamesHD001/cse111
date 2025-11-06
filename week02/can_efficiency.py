import math
def main():
    print("We'll get back here")
    
def can_volume(radius, height):
    """Compute and return the volume of a can given its
    radius and height.
    Parameters
    radius: The radius of the can in centimeters.
    height: The height of the can in centimeters.
    Return: The volume of the can in cubic centimeters.
    """
    volume = math.pi * (radius ** 2) * height
    return volume
main()