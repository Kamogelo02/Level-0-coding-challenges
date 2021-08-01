def common_letters(string1,string2):
    output= []
    string1= string1.lower()
    string2= string2.lower()
    
    for letter in string1:
      if letter in string2:
        output.append(letter)
    
    output= ', '.join(output)
    print(f"Common letters: {output}")

def main():      
    common_letters("Eckard", "computers")

if __name__=="__main__":
  main()
