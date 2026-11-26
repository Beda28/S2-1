import numpy as np

def unit_circle(n=100):
    theta = np.linspace(0, 2 * np.pi, n)

    x = np.cos(theta)
    y = np.sin(theta)
    
    return np.column_stack([x, y])

def rotation(degree):
    theta = np.radians(degree)

    return np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

def scaling(sx, sy):
    return np.array([
        [sx, 0],
        [0, sy]
    ])

def shearing(k):
    return np.array([
        [1, k],
        [0, 1]
    ])

def transform(points, matrix):
    return points @ matrix.T