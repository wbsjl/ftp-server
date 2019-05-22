import os

a=1

pid = os. fork()

if pid<0:
    print("error")
elif pid == 0:
    print("Child")
    a=100000
    print(a)
else:
    print("Parent")
    print(a)
print("All a =",a)