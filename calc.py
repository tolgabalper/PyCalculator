welcome = "welcome to python calculator"
rules = "do not use letters just rational numbers"
xinput = "what is the first value do you want to use"
yinput = "what is the second value do you want to use"
# lets write hello page
print(welcome)
print(rules)
# lets get out first value
x = float(input(xinput))
# lets get our second value
y = float(input(yinput))
# lets define or operation
sum = x + y
minus = x - y
multiplication = x * y
division = x / y
# lets do operation
print("Here all the possibilities that you might use")
print(
    f"sum, {sum:,}",
    f"minus, {minus:,}",
    f"multiplication, {multiplication:,}",
    f"division, {division:,}",
    f"division only 2 digit after 0, {division:.2f}",
    ":)",
    sep="\n"
)
