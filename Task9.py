def vowel(word):
    vowels= "aeiouAEIOU"
    print("Vowels: ", end="")
    for letter in word:
        if letter in vowels:
            print(letter, end =", ")
vowel("Umuzi")