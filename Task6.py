def maximum(*numbers):
    largest= numbers[0]
    for a in numbers:
        if a>largest:
            largest=a   
    return largest
maximum(1,3,6,200,90)   