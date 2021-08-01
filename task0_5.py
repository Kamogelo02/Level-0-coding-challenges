def calc_triangle_area(length1, length2, length3):
    semi_parimeter = (1 / 2) * (length1 + length2 + length3)
    area = (
        semi_parimeter
        * (semi_parimeter - length1)
        * (semi_parimeter - length2)
        * (semi_parimeter - length3)
    ) ** 0.5
    return area


def main():
    print(calc_triangle_area(3, 5, 4))


if __name__ == "__main__":
    main()


