import numpy as np

def min_max_scalar(X):
    """
    Min-Max Scalar normalization function for a numpy array.
    """
    X_norm = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
    return X_norm

# Example usage
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
X_norm = min_max_scalar(X)
print(X_norm)
