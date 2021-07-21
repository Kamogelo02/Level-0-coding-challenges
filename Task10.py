def common_letters(string1,string2):
    output=[]

    for letter in string1:
      if (letter in string2):
        output.append(letter)
    
    output= ', '.join(output)
    print(f"Common letters: {output}")

def main():      
    common_letters("house", "computers")

if __name__=="__main__":
  main()
