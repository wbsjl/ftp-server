s = input(">>")
print("bytes:", b"1")
print("bytes:", s.encode())
print("bytes:", bytes((0, 2, 3, )))
byte = s.encode()
print(byte)
s = byte.decode()
print(s)

