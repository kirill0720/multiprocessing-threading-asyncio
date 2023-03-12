"""Single-threaded programs"""

from time import sleep, perf_counter


def task():
    print('Started executing task...')
    sleep(1)
    print('Done')


if __name__ == '__main__':
    start_time = perf_counter()

    task()
    task()

    end_time = perf_counter()

    print(f'Execution took {end_time - start_time} seconds.')
