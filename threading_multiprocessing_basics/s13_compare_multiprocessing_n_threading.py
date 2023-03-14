import os
import time
from multiprocessing import Process
from threading import Thread
from typing import Callable

# in cmd: WMIC CPU Get DeviceID,NumberOfCores,NumberOfLogicalProcessors
NUMBER_OF_LOGICAL_PROCESSORS = os.cpu_count()


# Multiprocessing needs to import your script in each subprocess. Uncomment print to see it
# print(f'NUMBER_OF_LOGICAL_PROCESSORS = {NUMBER_OF_LOGICAL_PROCESSORS}')


def calculate_squares() -> None:
    for i in range(10_000_000):
        _ = i * i


def execute_with_threads(func: Callable, num_threads: int) -> None:
    """Execute a function with multiple threads."""
    threads = []

    for _ in range(num_threads):
        t = Thread(target=func)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


def execute_with_processes(func: Callable, num_processes: int) -> None:
    """Execute a function with multiple processes."""
    processes = []

    for _ in range(num_processes):
        p = Process(target=func)
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()


def main():
    """Execute the functions and measure the time they take."""
    start = time.perf_counter()
    execute_with_threads(calculate_squares, NUMBER_OF_LOGICAL_PROCESSORS)
    print(f'Execution with treading took {time.perf_counter() - start} seconds.')

    start = time.perf_counter()
    execute_with_processes(calculate_squares, NUMBER_OF_LOGICAL_PROCESSORS)
    print(f'Execution with multiprocessing took {time.perf_counter() - start} seconds.')


if __name__ == '__main__':
    main()
