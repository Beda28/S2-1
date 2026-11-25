import matplotlib.pyplot as plt
from pathlib import Path

def line(x, y, title, xl, yl, path):
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(xl)
    ax.set_ylabel(yl)
    ax.grid(alpha=0.3)

    save_figure(fig, path)

def save_figure(fig, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
