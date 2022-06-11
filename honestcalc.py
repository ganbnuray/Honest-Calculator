messages = {
"msg_0" : "Enter an equation",
"msg_1" : "Do you even know what numbers are? Stay focused!",
"msg_2" : "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
"msg_3" : "Yeah... division by zero. Smart move...",
"msg_4" : "Do you want to store the result? (y / n):" ,
"msg_5" : "Do you want to continue calculations? (y / n):",
"msg_6" : " ... lazy",
"msg_7" : " ... very lazy",
"msg_8" : " ... very, very lazy",
"msg_9" : "You are",
"msg_10" : "Are you sure? It is only one digit! (y / n)",
"msg_11" : "Don't be silly! It's just one number! Add to the memory? (y / n)",
"msg_12" : "Last chance! Do you really want to embarrass yourself? (y / n)"
}
operators = ["+", "-", "*", "/"]
memory = 0
def ask():
    print(messages["msg_0"])
    operation = input().split()
    num1 = operation[0]
    num2 = operation[2]
    if num1 == "M":
        num1 = memory
    if num2 == "M":
        num2 = memory
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print(messages["msg_1"])
        ask()
    else:
        operator = operation[1]
        if operator in operators:
            check(num1, num2, operator)
            calc(num1, operator, num2)
        else:
            print(messages["msg_2"])
            ask()
def is_one_digit(number):
    if (number > -10 and number < 10) and number.is_integer():
        return True
    else:
        return False
def check(num1, num2, operator):
    msg = ""
    if is_one_digit(num1) and is_one_digit(num2):
        msg += messages["msg_6"]
    if (num1 == 1 or num2 == 1) and operator == "*":
        msg += messages["msg_7"]
    if (num1 == 0 or num2 == 0) and (operator == "*" or operator == "+" or operator == "-"):
        msg += messages["msg_8"]
    if msg != "":
        msg = messages["msg_9"] + msg
    else:
        pass
    print(msg)

def memory_assign(result):
    answer = input(messages["msg_4"])
    if answer == "y":
        if is_one_digit(result):
            msg_index = 10
            while msg_index <= 12:
                variable = "msg_{}".format(msg_index)
                answer = input(messages[variable])
                if answer == "y":
                    msg_index +=1
                else:
                    global memory
                    memory = result
            else:
                memory = result
        else:
            memory = result
    else:
        memory = result


def continue_calc():
    reply = input(messages["msg_5"])
    if reply == "y":
        ask()
    elif reply == "n":
        pass

def calc(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
        print(result)
        memory_assign(result)
        continue_calc()
    elif operator == "-":
        result = num1 - num2
        print(result)
        memory_assign(result)
        continue_calc()
    elif operator == "*":
        result = num1 * num2
        print(result)
        memory_assign(result)
        continue_calc()
    elif operator == "/":
        try:
            result = num1 / num2
            print(result)
            memory_assign(result)
            continue_calc()
        except ZeroDivisionError:
            print(messages["msg_3"])
            ask()
ask()
