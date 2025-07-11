import pytest
import threading
import random

NUM_THREADS = 10


def run():
    pass


def test_ok_1():
    assert 1 == 1


def test_ok_2():
    my_thread = threading.Thread(target=run)
    my_thread.start()
    my_thread2 = threading.Thread(target=run)
    my_thread2.start()


def test_ok_3():
    threads = []
    for i in range(NUM_THREADS):
        threads.append(threading.Thread(target=run))
    # start all threads
    for thread in threads:
        thread.start()

def test_ok_4():
    my_thread = threading.Thread(target=run)
    my_thread.start()
    my_thread.join()


def test_ok_5():
    threads = []
    for i in range(NUM_THREADS):
        threads.append(threading.Thread(target=run))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def test_violation_1():
    my_thread = threading.Thread(target=run)
    my_thread.start()
    my_thread2 = threading.Thread(target=run)
    my_thread2.start()
    try:
        my_thread2.start()
    except RuntimeError:
        pass


def test_violation_2():
    threads = []
    for i in range(NUM_THREADS):
        threads.append(threading.Thread(target=run))
    # start all threads
    for thread in threads:
        thread.start()

    random.shuffle(threads)
    try:
        threads[0].start()
    except RuntimeError:
        pass
