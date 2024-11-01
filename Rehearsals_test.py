#1
num_students:int=int(input("number of students:"))

Full_classes_30_students=num_students//30
last_class_students=num_students%30

print(f"The number of students who will remain in the last class is {Full_classes_30_students}")
print(f"How many students will remain in the last class is {last_class_students}")

#2
num_10_99=0
while True:
    try:
        num_10_99:int=int(input("10-99:"))
        if 10 <= num_10_99 <= 99:
            break
    except ValueError:
        print("its o.k, continue")
ahadot=num_10_99 %10
asarot = num_10_99 // 10
if ahadot > asarot:
    reverse_number = ahadot*10+asarot
    print(f"reverse the number, the new number is {reverse_number}")
else:
    print(f"Do not change the number, the number that remains is {num_10_99}")

#3
list_rishoni: list[int] = []
add_list_rishoni: list[int] = []

for x in range(2, 200 + 1):

    list_divs: list[int] = []

    for i in range(2, x):
        list_divs.append(x % i)
    if all(list_divs):
        list_rishoni.append(x)
    if all([x % i for i in range(2, x)]):
        add_list_rishoni.append(x)

print(list_rishoni)




