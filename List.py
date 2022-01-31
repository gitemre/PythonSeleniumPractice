values = [1, 2, "rahul", 4, 5]

print(values[0])  # 1

print(values[3])  # 4

print(values[-1])  # 5 (Last index)

print(values[1:3])  # 2 rahul

print(values)
values.insert(3, "shetty")
print(values)
values.append("End")
print(values)

values[2] = "Emre"  # Updating

del values[0]
print(values)

val = (1, 2, "emre", 4.5)
print(val[1])

# val[2] = "Emre Öztürk"

print(val)

# Dictionary

dic = {"a": 2, 4: "bcd", "c": "Hello World"}

print(dic[4])
print(dic["c"])

dict = {}

dict["firstname"] = "Emre"

dict["lastname"] = "Öztürk"

dict["gender"] = "Male"

print(dict)
print(dict["lastname"])
