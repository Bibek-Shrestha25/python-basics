# Simple for loop example in Python

# Print numbers from 1 to 5
for i in range(1, 6):
    print("Number:", i)


#
a  =  [1, 2, 3, 4, 5]
b =   [6, 7, 8, 9, 10]
c =  [11, 12, 13, 14, 15]
d = [16, 17, 18, 19, 20]
e = [21, 22, 23, 24, 25]
f = [26, 27, 28, 29, 30]
g = [31, 32, 33, 34, 35]
h = [36, 37, 38, 39, 40]
i_list = [41, 42, 43, 44, 45]
j = [46, 47, 48, 49, 50]

# Print all elements from all lists
for list in [a, b, c, d, e, f, g, h, i_list, j]:
    for num in list:
        print(num)
# Print all elements from all lists using while loops
lists = [a, b, c, d, e, f, g, h, i_list, j]
outer_idx = 0
while outer_idx < len(lists):
    inner_idx = 0
    while inner_idx < len(lists[outer_idx]):
        print(lists[outer_idx][inner_idx])
        inner_idx += 1
    outer_idx += 1
