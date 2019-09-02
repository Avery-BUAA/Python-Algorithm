import threading
import time
def job():
    print("start")
    time.sleep(2)
    print("done")
def job1():
    print("start1")
    time.sleep(2)
    print("done1")
def main():
    print("as")
    add_Thread = threading.Thread(target=job())
    add_Thread = threading.Thread(target=job1())


    add_Thread.start()

    print("gou")
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())


main()
