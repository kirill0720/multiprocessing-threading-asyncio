"""Passing arguments to threads"""

from time import sleep, perf_counter
from threading import Thread


def task(task_id):
    print(f'Starting task {task_id}...')
    sleep(1)
    print(f'Task {task_id} done.')


if __name__ == '__main__':
    start_time = perf_counter()

    # Create and start 10 threads
    threads = []
    for n in range(1, 11):
        t = Thread(target=task, args=(n,))
        threads.append(t)
        t.start()

    # Wait for threads to finish
    for t in threads:
        t.join()

    end_time = perf_counter()

    print(f'Execution took {end_time - start_time} seconds.')
