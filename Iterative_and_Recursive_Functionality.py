#Jay George
#CIS261


def factorialc_recursive(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorialc_recursive(num - 1)
    
def factorial_iterative(num):
    fact = 1
    for number in range(2, num + 1):
        fact = number * fact 
        
    return fact

def main():
    print("Factorial results using iterative function")
    print("0!" , factorial_iterative(0))
    print("5!" , factorial_iterative(5))
    print("10!" , factorial_iterative(10))
    print("25!" , factorial_iterative(25))
    print("50!" , factorial_iterative(50))
    print("100!" , factorial_iterative(100))
    print("Factorial result using recursive function")
    print("0!" , factorialc_recursive(0))
    print("5!" , factorialc_recursive(5))
    print("10!" , factorialc_recursive(10))
    print("25!" , factorialc_recursive(25))
    print("50!" , factorialc_recursive(50))
    print("100!" , factorialc_recursive(100))
    
if __name__ == "__main__":
    main() 
    
    
