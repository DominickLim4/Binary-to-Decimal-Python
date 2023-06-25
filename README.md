#  Binary to Decimal Conversion
 
This code snippet provides a function Conversion that converts a binary number into its decimal equivalent. The code is written in Python and can be used to perform binary-to-decimal conversions.

## Usage
To use this code, follow the steps below:

1. Call the Conversion function, passing the binary number as an argument.
2. The function will return the decimal equivalent of the binary number.
```
# Example Usage
result = Conversion(101011)
print(result)
```

## Code Explanation
The Conversion function takes a binary number as input and converts it to decimal. It follows the steps below:

1. Initialize a variable sum to store the cumulative sum
2. Convert the input number to a string for easier iteration through its digits
3. Set the initial value of power to 1
4. Iterate through each digit of the binary number in reverse order
5. Convert each digit from a string to an integer
6. If the digit is equal to 1, add its value multiplied by the current power to the sum
7. Multiply power by 2 to increment it for the next digit
8. After iterating through all the digits, return the final sum

## Examle
In the given example, the binary number 101011 is passed to the Conversion function. The function converts it to decimal and stores the result in the result variable. Finally, the result is printed, which should output 43 to the console.
