from multiprocessing import Process
import os

filename = "123.jpg"

size = os.path .getsize(filename)

def top():
    f = open (filename,'rb')
    n = size//2
    fw = open('top.jpg','wb')
    fw.write(f.read(n))
    f.close()
    fw.close()

def bot():
    f = open(filename, 'rb')
    n = size // 2
    fw = open('bot.jpg', 'wb')
    f.seek(size//2,0)
    fw.write(f.read())
    f.close()
    fw.close()
p = Process(target=top)
q = Process(target=bot)
p.start()
q.start()
p.join()
q.join()


