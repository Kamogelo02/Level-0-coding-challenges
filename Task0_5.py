def calc_triangle_area(length1, length2, length3):
    s= (1/2)*(length1+length2+length3)
    area= (s*(s-length1)*(s-length2)*(s-length3))**0.5
    return area

def main():
    print(calc_triangle_area(3,5,4))

if __name__=="__main__":
    main()
