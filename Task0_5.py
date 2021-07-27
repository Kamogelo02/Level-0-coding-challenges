def calc_triangle_area(length1, length2, length3):
    semi_parameter = (1 / 2) * (length1 + length2 + length3)
    area = (
        semi_parameter
        * (semi_parameter - length1)
        * (semi_parameter - length2)
        * (semi_parameter - length3)
    ) ** 0.5
    return area


def main():
    print(calc_triangle_area(3, 5, 4))


if __name__ == "__main__":
    main()

