"""There is a list of text files. Replace the text in all files."""

from pathlib import Path
from threading import Thread
from time import perf_counter


def replace_text(file_path: Path, old_str: str, new_str: str) -> None:
    """Replaces instances of a string in a file."""
    print(f'Processing file {file_path}...')

    with file_path.open('r') as f:
        content = f.read()

    content = content.replace(old_str, new_str)

    with file_path.open('w') as f:
        f.write(content)


def single_thread(filenames: list) -> None:
    """Runs the replace function on each file in a list, sequentially."""
    for filename in filenames:
        replace_text(filename, 'lorem', 'lorems')


def multi_thread(filenames: list) -> None:
    """Runs the replace function on each file in a list, using multithreading."""
    # create threads
    threads = [Thread(target=replace_text, args=(filename, 'lorems', 'lorem')) for filename in filenames]

    # start threads
    for thread in threads:
        thread.start()

    # wait for threads to finish
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    filenames = [Path(f'archive/test{i}.txt') for i in range(1, 11)]

    # test single-threaded execution
    start_time = perf_counter()
    single_thread(filenames)
    end_time = perf_counter()
    print(f'Single-threaded execution took {end_time - start_time} seconds.')

    # test multi-threaded execution
    start_time = perf_counter()
    multi_thread(filenames)
    end_time = perf_counter()
    print(f'Multi-threaded execution took {end_time - start_time} seconds.')
