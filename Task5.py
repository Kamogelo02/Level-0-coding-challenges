import cmath
def calc_triangle_area(length_one, length_two, length_three):
    s= (1/2)*(length_one+ length_two+ length_three) 
    area= cmath.sqrt(s*(s-length_one)*(s-length_two)*(s-length_three))
    return area

print(calc_triangle_area(10,5,4))
