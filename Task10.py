def common_letters(string1,string2):
    words= list(set(string1) &set(string2))
    print("Common letters: ", end=" ")
    for letter in words:
      print(letter, end= ", ") 
common_letters("house", "computers")