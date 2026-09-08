import numpy as np
class ShapeError(Exception):
    """Raised when array dimensions are incompatible for matrix multiplication."""
    pass


def matrix_multiply(A, B):
    """Multiplies two matrices after verifying inner dimensions match."""
    # Assert dimensions exist and inner shapes match
    if A.shape[1] != B.shape[0]:
        raise ShapeError(
            f"Cannot multiply matrices! Inner dimensions mismatch: "
            f"A.shape={A.shape} (cols={A.shape[1]}) vs B.shape={B.shape} (rows={B.shape[0]})."
        )
    return A @ B


# Demonstrating try / except / else / finally
def run_safely(A, B):
    try:
        print("📐 Attempting matrix multiplication...")
        result = matrix_multiply(A, B)
    except ShapeError as e:
        print(f"❌ Handled expected error: {e}")
    else:
        print(f"✅ Multiplication successful! Result shape: {result.shape}")
    finally:
        print("🧹 Cleanup complete (runs every time).\n")


a = np.array([
    [1,2,4],
    [3,2,4]
])
b = np.array([
    [1, 2, 4],
    [2, 3, 9]
])

run_safely(a, b)
