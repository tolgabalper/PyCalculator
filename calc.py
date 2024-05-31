import math
from reportlab.pdfgen import canvas
import csv

saved = []

Welcome = "Welcome to PyCalculator by Boran A."
Options = "SUM // MINUS // MULTIPLICATION (MULT) // DIVISION // PERMUTATION // COMBINATION // POWER"

print(Welcome + "\n")


def savedselectorfunc():
    print("Saved results are :", saved)
    isUserWantUseSaved = input("Do you wanna use any of the saved results : (y / N) ")
    if isUserWantUseSaved == "y":
        isUserWantUseOne = input("Do you wanna just use one of them : (y / N)")
        if isUserWantUseOne == "y":
            print("Saved results are :", saved)
            whichOne = input("Which one you wanna use : ").replace(",", ".")
            x = float(whichOne)
            y = input("Enter the second number: ").replace(",", ".")
            y = float(y)
        else:
            print("Saved results are :", saved)
            whichOne = input("Which one you wanna use for first number : ").replace(
                ",", "."
            )
            whichTwo = input("Which one you wanna use for two number : ").replace(
                ",", "."
            )
            x = float(whichOne)
            y = float(whichTwo)
    else:
        x = input("Enter the first number: ").replace(",", ".")
        x = float(x)
        y = input("Enter the second number: ").replace(",", ".")
        y = float(y)
    return x, y


def Calculate():
    while True:
        print(Options + "\n")
        operation = input("Please select the operation you wanna use : ").lower()
        result = ""
        if saved != []:
            x, y = savedselectorfunc()
        else:
            x = input("Enter the first number: ").replace(",", ".")
            x = float(x)
            y = input("Enter the second number: ").replace(",", ".")
            y = float(y)

        if operation == "sum":
            result = math.fsum([x, y])
        elif operation == "minus":
            result = math.fabs(x - y)
        elif operation == "multiplication" or operation == "mult":
            result = math.prod([x, y])
        elif operation == "division":
            if y == 0:
                return "Error: Division by zero is not allowed."
            else:
                result = x / y
        elif operation == "permutation":
            x = int(x)
            y = int(y)
            result = math.perm(x, y)
        elif operation == "combination":
            x = int(x)
            y = int(y)
            result = math.comb(x, y)
        elif operation == "power":
            result = math.pow(x, y)
        else:
            print("please select according to the list")
            break

        print(result)
        saveopt = input("Do you wanna save the result : (y / n) ").lower()
        if saveopt == "y":
            saved.append(result)
            print("Result saved.")
            savecomp = input(
                "Do you wanna save the result to your computer : (y / N) "
            ).lower()
            if savecomp == "y":
                savepath = input("Enter the path where you want to save : ")
                saveformat = input(
                    "Which format do you wanna save results : (txt, csv, pdf) "
                )
                if saveformat == "pdf":
                    c = canvas.Canvas(savepath + "/result.pdf").drawString(
                        100, 750, "Result: " + str(result)
                    )
                    c.save()
                    isWanting = input("Do you wanna do another calculation : (y / n)")
                    if isWanting != "y":
                        break
                if saveformat == "txt":
                    with open(savepath + "/result.txt", "x") as f:
                        f.write("Results" + "\n" + str(result))
                    isWanting = input("Do you wanna do another calculation : (y / n)")
                    if isWanting != "y":
                        break
                if saveformat == "csv":
                    with open(savepath + "/result.csv", "x", newline="") as f:
                        csv.writer(f).writerow("Results")
                        csv.writer(f).writerow([result])
                    isWanting = input("Do you wanna do another calculation : (y / n)")
                    if isWanting != "y":
                        break
            else:
                isWanting = input("Do you wanna do another calculation : (y / n)")
                if isWanting != "y":
                    break
        else:
            isWanting = input("Do you wanna do another calculation : (y / n)")
            if isWanting != "y":
                break


Calculate()
