'''
Created on Oct 23, 2016

@author: physicalattraction
'''

import os.path
from PIL import Image


def get_img_dir() -> str:
    '''
    Return the full path to the image directory

    :return: string
    '''
    pkg_dir = os.path.dirname(__file__)
    img_dir = os.path.join(pkg_dir, '..', '..', 'img')
    return img_dir


def open_img(img_name: str) -> Image:
    '''
    Open the given file form the image directory

    :param img_name: Name including extension of the image
    :return: Image object
    '''
    img_dir = get_img_dir()
    full_img_path = os.path.join(img_dir, img_name)
    return Image.open(full_img_path)


def save_img(img: Image, img_name: str):
    '''
    Save the given image to the image directory

    :param img: Image object
    :param img_name: Name including the extension of the image
    '''
    img_dir = get_img_dir()
    full_img_path = os.path.join(img_dir, img_name)
    img.save(full_img_path)


def overlay(img: Image, overlay_color: tuple):
    '''
    Place an overlay over an existing image

    :param img: Image opened with PIL.Image
    :param overlay_color: four-tuple with color to add to your image
    '''
    assert len(overlay_color) == 4, 'Overlay color shall be a 4-tuple'

    img_overlay = Image.new(size=img.size, color=overlay_color, mode='RGBA')
    img.paste(img_overlay, None, mask=img_overlay)

    color_string = '_'.join([str(c) for c in overlay_color])
    filename = 'amsterdam_{color}.jpg'.format(color=color_string)
    save_img(img, filename)


if __name__ == '__main__':
    ams = open_img('amsterdam.jpg')
    green = (0, 50, 0, 128)
    overlay(ams, green)