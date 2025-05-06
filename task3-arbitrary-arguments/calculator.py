"""
this program works as calculator by using arguments and parameters. it contains functions and error handling found if we compute
"""
def process_inputs(*args):# this is function definition
    numbers = []
    for arg in args:
        if isinstance(arg, (int, float)):
            numbers.append(arg)
        else:
            raise ValueError(f"Invalid input: {arg} is not a number.")
    return numbers

#function arguments, args and kwargs
def calculate(*args, **kwargs):
    numbers = process_inputs(*args)
    
    if not numbers:
        raise ValueError("At least one numeric input is required.")

    result = numbers[0]
#the following are helper functios and parameters used in computation
    for op, do_op in kwargs.items():
        if not do_op:
            continue

        if op == 'add':
            result = sum(numbers)
        elif op == 'subtract':
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
        elif op == 'multiply':
            result = 1
            for num in numbers:
                result *= num
        elif op == 'divide':
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    raise ValueError("Division by zero is not allowed.")
                result /= num
        else:
            raise ValueError(f"Unsupported operation: {op}")

    return result
#error handling and outputing the result
if __name__ == "__main__":
    try:
        print(calculate(10, 5, 2, add=True))         #here Output is: 17
        print(calculate(10, 5, 2, subtract=True))    #here  Output is: 3
        print(calculate(10, 5, 2, multiply=True))    #here Output is : 100
        print(calculate(100, 5, 2, divide=True))     #here Output is: 10.0
    except Exception as e:
        print("Error:", e)