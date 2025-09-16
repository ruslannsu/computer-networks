import threading


def printer(string):
    while (1):
      print(string)
      



thread1 = threading.Thread(target=printer, args=('hello world', ))


thread2 = threading.Thread(target=printer, args=('hello thread', ))


thread1.start()
thread2.start()
    