"""This program creates thumbnails of images in the images folder and saves them in the thumbs folder"""

import multiprocessing
import os
import time
from concurrent.futures import ProcessPoolExecutor

from PIL import Image, ImageFilter

filenames = [
    'images/1.jpg',
    'images/2.jpg',
    'images/3.jpg',
    'images/4.jpg',
    'images/5.jpg',
]


def create_thumbnail(filename, size=(50, 50), thumb_dir='thumbs'):
    """Creates a thumbnail of an image with the given filename, saves it to the thumb_dir."""
    img = Image.open(filename)
    img = img.filter(ImageFilter.GaussianBlur())
    img.thumbnail(size)
    img.save(f'{thumb_dir}/{os.path.basename(filename)}')
    print(f'File {filename} processed...')


if __name__ == '__main__':
    start = time.perf_counter()

    # single process execution
    # for filename in filenames:
    #     create_thumbnail(filename)

    # multiprocessing execution
    # processes = [multiprocessing.Process(target=create_thumbnail, args=[filename])
    #              for filename in filenames]
    # for process in processes:
    #     process.start()
    # for process in processes:
    #     process.join()

    # multiprocessing execution with ProcessPoolExecutor
    with ProcessPoolExecutor() as executor:
        executor.map(create_thumbnail, filenames)

    print(f'Execution took {time.perf_counter() - start} seconds.')
