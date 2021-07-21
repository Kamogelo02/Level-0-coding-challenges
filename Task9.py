def vowel(string):
    vowels= ['a', 'e', 'i', 'o', 'u']
    output= list()
    
    for letters in string:
        if (letters in vowels) and (letters not in output):
            output.append(letters)
    
    output_str=str(output)[1:-1]
    new_str_output= output_str.replace("'", "")

    print(new_str_output)

def main():
    vowel("Umuzi")

if __name__=="__main__":
    main()
