largest = int(input("Enter a number: "))

for i in range(4):
    n = int(input("Enter a number: "))

    if n > largest:
        largest = n

print("Largest number:", largest)