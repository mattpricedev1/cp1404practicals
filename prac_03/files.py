name = input("Enter your name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Your name is {name}")

in_file = open("numbers.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
in_file.close()
print(number1 + number2)

total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    total += int(line)
print(total)
