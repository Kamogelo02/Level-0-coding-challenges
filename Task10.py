def common_letters(s1,s2):
 words= list(set(s1) &set(s2))
 print("Common letters: ", end=" ")
 for letter in words:
  print(letter, end= ", ")
common_letters("house", "computers")