for i in range(1,101): 
    fizz = 3
    buzz = 5
    moduloRemainder = 0
    if i % fizz == moduloRemainder and i % buzz == moduloRemainder:
        print("BizzFuzz")
    elif i % fizz == moduloRemainder:
        print("Bizz")
    elif i % buzz == moduloRemainder:
        print("Fuzz")
    else:
        print(i)
    
