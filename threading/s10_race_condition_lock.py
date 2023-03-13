"""
Imagine we have two threads. One thread reads a value from a shared variable, and then the second thread does the same.

Both threads then try to change the value of the shared variable.
They start competing to see which thread will write the value to the variable last.

Only the value from the thread that writes the value to the shared variable last will be saved,
because it will overwrite the previous value.

To prevent race conditions, you can use the Lock class from the threading module.
"""
from threading import Thread, Lock
from time import sleep


class Counter:
    """A class that implements a counter with thread safety."""

    def __init__(self) -> None:
        self.value = 0
        self.lock = Lock()

    def increase(self, by: int) -> None:
        """Increases the counter by a given amount."""
        self.lock.acquire()

        current_value = self.value
        current_value += by

        sleep(0.1)

        self.value = current_value
        print(f'Counter value: {self.value}')

        self.lock.release()


if __name__ == '__main__':
    counter = Counter()

    # create threads
    t1 = Thread(target=counter.increase, args=(10,))
    t2 = Thread(target=counter.increase, args=(20,))

    # start threads
    t1.start()
    t2.start()

    # wait for threads to finish
    t1.join()
    t2.join()

    print(f'Final counter value: {counter.value}')
