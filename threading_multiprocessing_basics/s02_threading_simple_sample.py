"""Module threading_multiprocessing_basics for multithreading programs"""

from time import sleep, perf_counter
from threading import Thread


def task():
    print('Starting task execution...')
    sleep(1)
    print('Done')


if __name__ == '__main__':
    start_time = perf_counter()

    # create two new threads
    t1 = Thread(target=task)
    t2 = Thread(target=task)

    # start the threads
    t1.start()
    t2.start()

    # the main thread will wait for the completion of t1, t2 threads
    t1.join()
    t2.join()

    end_time = perf_counter()

    print(f'Execution took {end_time - start_time} seconds.')
