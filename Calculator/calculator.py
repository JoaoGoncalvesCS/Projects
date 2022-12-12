from multiprocessing.sharedctypes import Value
import csv
import sys

def main():
    addiction()
    subtraction()
    multiplication()
    division()



global calculation
calculation = input("Numbers: ").strip(" ")


def addiction():
    global calculation
    if "+" in calculation:
        x,y = calculation.split("+")
        try:
            x = float(x)
        except ValueError:
            sys.exit("Has to be a number")
        try:
            y = float(y)
        except ValueError:
            sys.exit("Has to be a number")

        global result
        result = (x + y)
        with open("history.csv", "a") as file:
            file.write(f"{result}\n")
        print(f"Result: {result}")
        return result


def subtraction():
    if "-" in calculation:
        x,y = calculation.split("-")
        try:
            x = float(x)
        except ValueError:
            sys.exit("Has to be a number")
        try:
            y = float(y)
        except ValueError:
            sys.exit("Has to be a number")

        global result
        result = (x - y)
        with open("history.csv", "a") as file:
            file.write(f"{result}\n")
        print(f"Result: {result}")
        return result


def multiplication():
    if "*" in calculation:
        x,y = calculation.split("*")
        try:
            x = float(x)
        except ValueError:
            sys.exit("Has to be a number")
        try:
            y = float(y)
        except ValueError:
            sys.exit("Has to be a number")

        global result
        result = (x * y)
        with open("history.csv", "a") as file:
            file.write(f"{result}\n")
        print(f"Result: {result}")
        return result


def division():
    if "/" in calculation:
        x,y = calculation.split("/")
        try:
            x = float(x)
        except ValueError:
            sys.exit("Has to be a number")
        try:
            y = float(y)
        except ValueError:
            sys.exit("Has to be a number")

        global result
        result = (x / y)
        with open("history.csv", "a") as file:
            file.write(f"{result}\n")
        print(f"Result: {result}")
        return result

if __name__ == "__main__":
    main()