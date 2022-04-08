def task(**kwargs):

    if "action" in kwargs.keys():
        action = kwargs["action"]

        num1 = int(input("Insert the first number > "))
        num2 = int(input("Insert the second number > "))

        if action == "+":
            return num1 + num2
        elif action == "-":
            return num1 - num2
        elif action == "*":
            return num1 * num2
        elif action == "/":
            if num2 == 0:
                return "Error you can't divide by 0"
            return num1 / num2
        else:
            return "Wrong Command"


while True:
        operator = input("Insert math operator +,-,*,/  to stop insert 0 > ")
        if operator == "0":
                break

        result = task(action=operator)
        print (result)