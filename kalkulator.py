def add(a,b):
    answer = a + b
    return answer

def substract(a,b):
    answer = a-b
    return answer

def multiply(a,b):
    answer = a*b
    return answer

def divide(a,b):
    answer = a/b
    return answer

def modulo(a,b):
    answer = a%b
    return answer

mainLoop = True
actions = ["1", "2", "3", "4", "5", "6", "quit", "clear"]
while mainLoop:
    counter = 0
    wynik = []
    while counter == 0:
        print("Please type in what kind of action would you like to perform: ")
        action = input("1. add, 2. substact, 3. multiply, 4. divide, 5. modulo, or type quit to quit:\n")
        if action in actions:
            if action.lower() != "quit":
                num1 = int(input("Please type in first number: \n"))
                num2 = int(input("Please type in second number: \n"))
                if action == "1":
                    equals = add(num1, num2)
                    print(f"Answer: {equals}")
                    counter+=1
                    wynik.append(equals)
                elif action == "2":
                    equals = substract(num1, num2)
                    print(f"Answer: {equals}")
                    counter+=1
                    wynik.append(equals)
                elif action == "3":
                    equals = multiply(num1, num2)
                    print(f"Answer: {equals}")
                    counter+=1
                    wynik.append(equals)
                elif action == "4":
                    equals = divide(num1, num2)
                    print(f"Answer: {equals}")
                    counter+=1
                    wynik.append(equals)
                elif action == "5":
                    equals = modulo(num1, num2)
                    print(f"Answer: {equals}")
                    counter+=1
                    wynik.append(equals)
            else:
                mainLoop = False
        else:
            print("Please type in one of the options")

    while counter != 0:
        print("Please type in what kind of action would you like to perform: ")
        action = input("1. add, 2. substact, 3. multiply, 4. divide, 5. modulo, 6. clear or type quit to quit:\n")
        if action in actions:
            if action.lower() != "quit":
                if action != "6":
                    num1 = wynik[0]
                    num2 = int(input("Please type in number: \n"))
                    if action == "1":
                        equals = add(num1, num2)
                        print(f"Answer: {equals}")
                        counter+=1
                        wynik[0] = equals
                    elif action == "2":
                        equals = substract(num1, num2)
                        print(f"Answer: {equals}")
                        counter+=1
                        wynik[0] = equals
                    elif action == "3":
                        equals = multiply(num1, num2)
                        print(f"Answer: {equals}")
                        counter+=1
                        wynik[0] = equals
                    elif action == "4":
                        equals = divide(num1, num2)
                        print(f"Answer: {equals}")
                        counter+=1
                        wynik[0] = equals
                    elif action == "5":
                        equals = modulo(num1, num2)
                        print(f"Answer: {equals}")
                        counter+=1
                        wynik[0] = equals
                    else:
                        print("Type in one of the options")
                elif action == "6":
                    counter = 0
            else:
                mainLoop = False
        else:
            print("Please type in one of the options")