"""
Thread-Safe Queue in Python

Learn how to use a synchronized queue for safe data exchange between multiple threads.

The built-in queue module allows for safe data exchange between multiple threads.
The Queue class from the queue module implements all the necessary locking semantics.
"""

import time
from queue import Empty, Queue
from threading import Thread


def producer(queue: Queue) -> None:
    """Inserts integer elements 1-5 into a given queue and sleeps for 1 second after each insertion."""
    for i in range(1, 6):
        print(f'Inserting element {i} into the queue')
        time.sleep(1)
        queue.put(i)


def consumer(queue: Queue) -> None:
    """Takes elements from a given queue and sleeps for 2 seconds after processing each element."""
    while True:
        try:
            item = queue.get()
        except Empty:
            continue
        else:
            print(f'Processing element {item}')
            time.sleep(2)
            queue.task_done()


def main() -> None:
    """
    Creates a queue and two threads, one producer and one consumer, and starts them.
    Waits for all tasks to be added to the queue and for all tasks in the queue to be completed.
    """
    queue = Queue()

    # create and start the producer thread
    producer_thread = Thread(
        target=producer,
        args=(queue,)
    )
    producer_thread.start()

    # create and start the consumer thread
    consumer_thread = Thread(
        target=consumer,
        args=(queue,),
        daemon=True
    )
    consumer_thread.start()

    # wait for all tasks to be added to the queue
    producer_thread.join()

    # wait for all tasks in the queue to be completed
    queue.join()


if __name__ == '__main__':
    main()
