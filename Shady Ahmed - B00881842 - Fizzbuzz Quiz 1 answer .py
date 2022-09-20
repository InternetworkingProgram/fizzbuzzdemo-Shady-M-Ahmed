
# Making Initial code design

# Initial time range values
X_first = int(1)  
X_last = int(101)

def FizzBuzzHandler(first,last):
    
    for v in range(first,last):
        if v %3 ==0 and v%5 ==0:
            print("FizzBuzz")
        elif v%3 == 0:
            print("Fizz")
        elif v%5 == 0:
            print("Buzz")
        else:
            print(int(v))
    return()

FizzBuzzHandler(X_first,X_last)
            