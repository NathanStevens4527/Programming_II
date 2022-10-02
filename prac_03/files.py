#task 1
name = input("Name: ")
out_file = open('name.txt', 'w')
print(f"{name}", file=out_file)
out_file.close()

#task 2
in_file = open('name.txt', 'r')
name_from_file = in_file.readline()
print(f"Your name is {name_from_file}")
in_file.close()

#task 3
result = 0
in_file = open("numbers.txt")
for i in range(0, 2):
    line = int(in_file.readline())
    result += line
print(result)
in_file.close()

#task 4
result = 0
in_file = open("numbers.txt")
numbers = in_file.readlines()
for i in range (0, len(numbers)):
    int(numbers[i])
for i in range(0, len(numbers)):
    number = int(numbers[i])
    result += number
print(result)
in_file.close()