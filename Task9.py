def vowel(str):
    vowels= "aeiouAEIOU"
    print("Vowels: ", end="")
    for letter in str:
        if letter in vowels:
            print(letter, end =", ")
vowel("Umuzi")