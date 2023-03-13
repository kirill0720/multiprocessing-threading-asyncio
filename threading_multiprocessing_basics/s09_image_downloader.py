"""Downloads multiple images from Wikipedia using a thread pool."""

import os
import time
from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen


def download_image(url: str) -> None:
    """Downloads an image from a given URL and saves it locally"""

    image_data = None
    with urlopen(url) as f:
        image_data = f.read()

    if not image_data:
        raise Exception(f"Error: cannot download image {url}")

    filename = os.path.basename(url)
    with open(filename, 'wb') as image_file:
        image_file.write(image_data)
        print(f'{filename} downloaded...')


if __name__ == '__main__':
    start = time.perf_counter()

    urls = ['https://upload.wikimedia.org/wikipedia/commons/9/9d/Python_bivittatus_1701.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/4/48/Python_Regius.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/d/d3/Baby_carpet_python_caudal_luring.jpg',
            'https://upload.wikimedia.org/wikipedia/commons/f/f0/Rock_python_pratik.JPG',
            'https://upload.wikimedia.org/wikipedia/commons/0/07/Dulip_Wilpattu_Python1.jpg']

    with ThreadPoolExecutor() as executor:
        executor.map(download_image, urls)

    print(f'Execution time: {time.perf_counter() - start} seconds.')
