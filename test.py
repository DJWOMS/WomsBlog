# coding=utf-8
# d1 = {"key1": 1, "key2": 2}
# d2 = {"key3":3, "key4": 4}
# arr = [d1, d2]
# for k in arr[0]:
#     print(arr[0][k])

msg = "Ваше возраст - "
age = ""
while True:
    age = input("Ваше возраст - ")
    if age == "quit":
        break
    age = int(age)
    if age <= 3:
        print("10$")
    elif age <= 12:
        print("15$")
    else:
        print("25$")
        