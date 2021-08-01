def convert_into_hours_and_minutes(number):
    minutes = int(number % 60)
    hours = int((number - minutes) / 60)

    if hours > 1 or hours == 0:
        output = f"{hours} hours, "
    else:
        output = f"{hours} hour, "
    if minutes > 1 or minutes == 0:
        output = f"{output}{minutes} minutes."
    else:
        output = f"{output}{minutes} minute."
    return output


def main():
    print(convert_into_hours_and_minutes(71))


if __name__ == "__main__":
    main()
