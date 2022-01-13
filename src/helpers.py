from pathlib import Path

import imageio as iio
import matplotlib.pyplot as plt
import numpy as np
from skimage import exposure, transform


def plot_hist(img, chan=None, xlims=(0, 1), cumul=False, vlines=None):
    fig, ax = plt.subplots()
    if len(img.shape) == 2:
        ax.hist(img.ravel())
    elif chan is not None:
        ax.hist(img[:, :, chan].ravel(), bins=256, cumulative=cumul)
    else:
        for chan in range(3):
            ax.hist(img[:, :, chan].ravel(), bins=256)
    ax.set_xlim(xlims[0], xlims[1])
    if vlines is not None:
        try:
            iter(vlines)
        except TypeError:
            vlines = [vlines]
        for v in vlines:
            ax.axvline(v, color='r')
    return fig, ax

def resize_by_row(img_to_resize, img_to_match):
    rows_match = img_to_match.shape[0]
    rows_resize = img_to_resize.shape[0]
    img_resized = transform.resize(
        img_to_resize, 
        (rows_match, img_to_resize.shape[1] * rows_match / rows_resize), 
        anti_aliasing=True
    )
    return img_resized
