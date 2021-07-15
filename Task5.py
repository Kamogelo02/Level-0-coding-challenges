import cmath
def calc_triangle_area(length1, length2, length3):
    s= (1/2)*(length1+ length2+ length3) 
    area= cmath.sqrt(s*(s-length1)*(s-length2)*(s-length3))
    return area
print(calc_triangle_area(10,5,4))
