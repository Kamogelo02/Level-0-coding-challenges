def common_letters(string_one,string_two):
    words= list(set(string_one) &set(string_two))
    print("Common letters: ", end=" ")
    for letter in words:
      print(letter, end= ", ")
    
common_letters("house", "computers")
