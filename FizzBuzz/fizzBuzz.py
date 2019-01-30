for num in range(1,101):                    # Gets all numbers in range and iterates over each one
    if num % 3 == 0 and num % 5 == 0:       # If number is a multiple of 3 and 5 immediately return FizzBuzz
        print("FizzBuzz")
    elif num % 3 == 0:                      # Multiple of 3 = Fizz
        print("Fizz")
    elif num % 5 == 0:                      # Multiple of 5 = Buzz
        print("Buzz")
    else:                                   # Other numbers
        print(num)