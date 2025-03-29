import ast

def multiply_by_6(n):
    return n * 6

if __name__ == "__main__":
    user_input = input("Введите число: ")
    number = ast.literal_eval(user_input)
    print(multiply_by_6(number))
