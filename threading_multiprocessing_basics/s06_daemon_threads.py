"""
A daemon thread is a thread that runs in the background, performing tasks that are not critical.
The program does not wait for the daemon thread to finish before terminating,
and the daemon thread automatically terminates when the program exits.
"""

from threading import Thread
import time


def show_timer():
    """A function that continuously prints the number of seconds that have passed."""
    count = 0
    while True:
        count += 1
        time.sleep(1)
        print(f'{count} seconds have passed...')


if __name__ == '__main__':
    t = Thread(target=show_timer, daemon=True)  # compare with daemon=False
    t.start()

    answer = input('Do you want to exit?\n')
