def vowel(string):
    vowels= "aeiouAEIOU"
    print("Vowels: ", end="")
    for letters in string:
        if letters in vowels:
            print(letters, end =", ")
vowel("Umuzi")
