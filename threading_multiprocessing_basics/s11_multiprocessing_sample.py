"""How multiprocessing works."""

import multiprocessing
import time


def task(n=100_000_000):
    while n:
        n -= 1


if __name__ == '__main__':
    start = time.perf_counter()

    # task()
    # task()

    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'Execution took {time.perf_counter() - start:} seconds.')
