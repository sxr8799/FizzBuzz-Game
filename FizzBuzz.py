for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0: # checking if the number is divisible by 3 and 5.
        number = "FizzBuzz"
    elif number % 3 == 0: # checking if the number is divisible by 3.
        number = "Fizz"
    elif number % 5 == 0: # checking if the number is divisible by 5.
        number = "Buzz"
    else:
        number = number # to make sure all other numbers that dont fit the criteria are also printed.
    print(number)
