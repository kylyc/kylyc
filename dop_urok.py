#Функции
# def div(num1:int, num2:int):
#     print(num1 / num2)
# div(10, 2)
# div(20, 3)

# def add(num1:int=10, num2:int=20):
#     print(num1 + num2)
# add(20, 5)

# def mult(num1:int=5, num2:int=5) -> int:
#     print(num1 * num2)
# mult()

#Оператор return
# def welcome(name:str="Nurbolot") -> str:
#     return "Welcome " + name
# print(welcome("Jakshylyck"))
# print(welcome())

def calculator(num1:int=1, num2:int=1, operator:str="+") -> int:
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Такого оператора нету"
print(calculator(30, 30, "-"))

print("Hello GitHub")