def convert_into_hours_and_minutes(number):
    output=" "
    minutes= int(number%60)
    hours= int((number-minutes)/60)
    if(hours>1):
        output= str(hours)+ "hours, "
    else:
        output=str(hours)+ "hour, "
    if(minutes>1):
        output= output+ str(minutes)+ "minutes "
    else:
        output=output +str(minutes) + "minute"
    return output
print(convert_into_hours_and_minutes(71))