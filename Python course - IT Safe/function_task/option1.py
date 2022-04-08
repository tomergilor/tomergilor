def task(operator, num1, num2):
        if operator == "+":
                return num1+ num2
        elif operator == "-":
                return num1-num2
        elif operator == "*":
                return num1 * num2
        elif operator == "/":
                if num2 == 0:
                        return "Error you can't divide by 0"
                return num1 / num2
        else:
                return "Wrong Command"

while True:
        operator = input("Insert math operator +,-,*,/  to stop insert 0 > ")
        if operator == "0":
                break

        num1 = int(input("Insert the first number > "))
        num2 = int(input("Insert the second number > "))
        result = task(operator, num1, num2)
        print (result)