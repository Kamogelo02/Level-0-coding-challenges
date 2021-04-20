import math
def calc_triangle_area(length1, length2, length3):
    s= (1/2)*(length1+ length2+ length3)        # calculate the semi parameter of the triangle
    area= math.sqrt(s*(s-length1)*(s-length2)*(s-length3))      # set up Heron's formula
    return area
print(calc_triangle_area(3,4,5))