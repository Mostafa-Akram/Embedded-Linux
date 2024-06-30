

list = [1, 2, 3, 4, 5, 6, 3, 8, 9, 10]
num = 3
count = 0
for i in list:
    if i == num:
        count += 1
print("The number", num, "appears", count, "times in the list")
