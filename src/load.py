import numpy as np
import matplotlib.pyplot as plt

def load(path):
    data = np.genfromtxt(
        path,       delimiter=",",
        names=True, dtype=None, encoding="utf-8"
    )

    return data["date"], data["price"]

def load_image(path):
    return plt.imread(path)