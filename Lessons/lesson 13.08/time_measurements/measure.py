import time

start_time = 0
run = False

def start():
    global start_time, run
    run = True
    start_time = time.time()

def finish():
    global start_time, run
    if run:
        finish_time = time.time()
        res = finish_time - start_time
        start_time, run = 0, False
        return res