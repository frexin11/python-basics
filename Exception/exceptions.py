try:
    age =int(input("Age:" ))
    income = int(input("Income: "))
    risk = income/age
    print(risk)
    print(age)
except ZeroDivisionError:
    print("age cant be zero")
except ValueError:
    print("Invalid input")
