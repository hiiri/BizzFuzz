for i in range(1,101): 
    fizz = 3
    buzz = 5
    moduloRemainder = 0
    if i % fizz == moduloRemainder and i % buzz == moduloRemainder:
        print("FizzBuzz")
    elif i % fizz == moduloRemainder:
        print("Fizz")
    elif i % buzz == moduloRemainder:
        print("Buzz")
    else:
        print(i)
    
