try:
    fd = open("/home/tarena/Project/homework_05/Change.py",mode='w')
except FileNotFoundError as a:
    print("no")
else:
    print("yes")

fd.write("print('Hello earth')")

fd.close()
fd = open("/home/tarena/Project/homework_05/Change.py",mode='a')
fd.write("/")
fd.write("print('Hello world')")