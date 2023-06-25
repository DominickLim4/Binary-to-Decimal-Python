def Conversion(numImput):
    sum = 0
    input_string = str(numImput)
    power = 1
    
    #Cycles through each digit of the binary number backwards
    for num in reversed(input_string):
        #Convert digit from string to int
        intNum = int(num)

        #Add the digit value to the cumulative sum
        if intNum ==  1:
            sum = sum + intNum*(intNum*power)

        #Increments the power of 2 to the next digit
        power *= 2
    return sum

#43
result = Conversion(101011)
print(result)


