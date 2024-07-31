import numpy as np

def standard_scalar(X):
    """
    Standard Scalar normalization function for a numpy array.
    """
    X_norm = (X - X.mean(axis=0)) / X.std(axis=0)
    return X_norm

# Example usage
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
X_norm = standard_scalar(X)
print(X_norm)

