def maximum(*numbers):
    largest= numbers[0]
    for x in numbers:
        if x>largest:
            largest=x   
    return largest
maximum(1,3,6,200,90)   
