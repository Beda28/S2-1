import matplotlib.pyplot as plt
from pathlib import Path

def save_figure(fig, path):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    
def line(x, y, title, xl, yl, path):
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.plot(x, y)
    ax.set_title(title)
    ax.set_xlabel(xl)
    ax.set_ylabel(yl)
    ax.grid(alpha=0.3)

    save_figure(fig, path)

def plot(original, transform, title, path):
    fig, ax = plt.subplots(figsize=(6, 6))

    ax.plot(
        original[:, 0], original[:, 1],
        linestyle="--", label="Original"
    )

    ax.plot(
        transform[:, 0], transform[:, 1],
        label="Transform"
    )

    ax.scatter(*original[0],  color="tab:blue")
    ax.scatter(*transform[0], color="tab:orange")

    ax.axhline(0, color="gray", linewidth=0.5)
    ax.axvline(0, color="gray", linewidth=0.5)

    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_aspect("equal")

    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)

    ax.grid(alpha=0.3)
    ax.legend()

    save_figure(fig, path)