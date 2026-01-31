import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_surface():
    # Example data (replace with your actual vertex data)
    # Format: 3D points as (N, 3) array, and faces as (M, 3) array
    vertices = np.array([
        [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],  # Bottom face
        [-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1]      # Top face
    ])

    faces = np.array([
        [0, 1, 2], [0, 2, 3],  # Bottom face
        [4, 5, 6], [4, 6, 7],  # Top face
        [0, 1, 5], [0, 5, 4],  # Front face
        [2, 3, 7], [2, 7, 6],  # Back face
        [1, 2, 6], [1, 6, 5],  # Right face
        [0, 3, 7], [0, 7, 4]   # Left face
    ])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Create the triangulated surface using the vertices and faces
    ax.plot_trisurf(
        vertices[:, 0],  # x coordinates
        vertices[:, 1],  # y coordinates
        vertices[:, 2],  # z coordinates
        triangles=faces,
        cmap='viridis',
        linewidths=0.5
    )

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Surface Plot')

    plt.tight_layout()
    plt.show()

plot_3d_surface()