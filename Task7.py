def celsius_to_fahrenheit(celsius):
    fahrenheit= (celsius*1.8) +32
    return fahrenheit

def main():
    print(celsius_to_fahrenheit(23))

def fahrenheit_to_celsius(fahrenheit):
    celsius= (fahrenheit -32) *(5/9)
    return celsius
    
def main():
    print(fahrenheit_to_celsius(23))

if __name__=="__main__":
    main()
