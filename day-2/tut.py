message = "Hello world"
print(message[1])
print(message[-4])
print(message[-4:])
m="Hello World"
print(m[2])
message = "Hello world"
for i in message[2:7]:
    print(i)
m1="Hello"
m2="World"
message=m1+m2
print(message*10)
print("H" in message)
print("w" not in message)
print(len(message))
print(bool(message))
print(type(message))

result=message.capitalize()
print(result)
result=message.upper()
print(result)
result=message.lower()
print(result)
result=message.split()
print(result)
result=message.find("R")
print(result)
