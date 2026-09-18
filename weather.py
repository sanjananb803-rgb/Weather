degree = int(input("Enter the degree: "))
if degree <=20:
    print("Cold weather!")
elif degree > 20 and degree <=38:
    print("Normal Weather!")
else:
    print("Hot Weather!")
fahrenheit = ((degree * 1.8) + 32)
print("The Fahrenheit value is: ",fahrenheit,"F")