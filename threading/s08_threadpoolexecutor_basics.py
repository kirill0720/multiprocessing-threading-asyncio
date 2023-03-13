"""
The ThreadPoolExecutor class extends the Executor class and returns a Future object.

The Executor class has three methods for managing a thread pool:
- submit() - submits a function for execution and returns a Future object. It takes a function and executes it asynchronously.
- map() - asynchronously executes functions for each element of an iterable table.
- shutdown() - terminates the executor. You can use a context manager to avoid having to explicitly call it.

Future is an object that represents the eventual result of an asynchronous operation.
The Future class has two useful methods:
- result() - returns the result of the asynchronous operation.
- exception() - returns the exception of the asynchronous operation in case of an exception.
"""

from concurrent.futures import ThreadPoolExecutor
from time import sleep, perf_counter


def task(task_id):
    print(f'Starting task {task_id}...')
    sleep(1)
    return f'Finished task {task_id}'


if __name__ == '__main__':
    start = perf_counter()

    # with ThreadPoolExecutor() as executor:
    #     f1 = executor.submit(task, 1)
    #     f2 = executor.submit(task, 2)
    #
    #     print(f1.result())
    #     print(f2.result())

    # alternative with map() instead of submit()
    with ThreadPoolExecutor() as executor:
        results = executor.map(task, [1, 2])
        for result in results:
            print(result)

    print(f"Execution took {perf_counter() - start} seconds.")
