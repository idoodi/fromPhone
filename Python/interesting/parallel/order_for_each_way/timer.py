import threading


def hello():
    print("hello, world")


t = threading.Timer(1, hello)
t.start()  # after 30 seconds, "hello, world" will be printed
