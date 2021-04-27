#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

def lightbox(images, titles=None, labels=None, column_num=5, **kwargs):
    """
    Show the images labels in a table

    Parameters
    ----------
    images: array-like or PIL images
            images to show

    titles: list of str
            the titles of the images

    labels: list of str
            the labels of the images

    column_num: int
                the number of columns, the default is 5

    Return
    ------
    None


    Other parameters
    ----------------
    **kwargs: the parameters for matplotlib.pyplot.figure()

    ### Output
    <matplotlib object>

    """
    def ceildiv(a, b):
        return -(-a // b)

    size = len(images)

    if titles is None:
        titles = [''] * size

    if labels is None:
        labels = [''] * size

    rownumber = ceildiv(len(images), column_num)

    fig = plt.figure(**kwargs)
    fig.set_size_inches(12, 3.0 * rownumber)
    fig.tight_layout()

    plt.subplots_adjust(left=0.125,
                bottom=0.1,
                right=0.9,
                top=0.9,
                wspace=0.2,
                hspace=0.35)

    for n, (img, title, label) in enumerate(zip(images, titles, labels)):
        ax = plt.subplot(rownumber, column_num, n+1)
        ax.imshow(img, cmap='gray')
        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel(label)
