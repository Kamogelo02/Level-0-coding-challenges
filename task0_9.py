def vowel(string):
    vowels = ["a", "e", "i", "o", "u"]
    output = list()
    string = string.lower()

    for letters in string:
        if (letters in vowels) and (letters not in output):
            output.append(letters)

    new_output = ", ".join(output)

    print(f"Vowels: {new_output}.")


def main():
    vowel("Umuzi")


if __name__ == "__main__":
    main()


