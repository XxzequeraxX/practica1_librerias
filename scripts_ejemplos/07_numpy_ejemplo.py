"""
07_numpy_ejemplo.py
===================
Demostración de la librería externa: NumPy
Incluye: arrays, matrices, operaciones matemáticas, álgebra lineal y estadísticas.
"""

import numpy as np

SEP = "=" * 55


def demo_arrays_basicos():
    print(SEP)
    print("  📦 ARRAYS BÁSICOS")
    print(SEP)

    # Creación de arrays
    a1 = np.array([1, 2, 3, 4, 5])
    a2 = np.array([10, 20, 30, 40, 50])
    print(f"  Array a1          = {a1}")
    print(f"  Array a2          = {a2}")
    print(f"  a1 + a2           = {a1 + a2}")
    print(f"  a1 * a2           = {a1 * a2}")
    print(f"  a1 ** 2           = {a1 ** 2}")
    print(f"  a2 / a1           = {a2 / a1}")
    print(f"  sqrt(a1)          = {np.sqrt(a1).round(4)}")
    print(f"  a1.sum()          = {a1.sum()}")
    print(f"  a1.prod()         = {a1.prod()}")
    print(f"  a1.cumsum()       = {a1.cumsum()}")


def demo_creacion_arrays():
    print(SEP)
    print("  🏗️  FORMAS DE CREAR ARRAYS")
    print(SEP)
    print(f"  zeros(5)          = {np.zeros(5)}")
    print(f"  ones(5)           = {np.ones(5)}")
    print(f"  full(5, 7)        = {np.full(5, 7)}")
    print(f"  arange(0,10,2)    = {np.arange(0, 10, 2)}")
    print(f"  linspace(0,1,6)   = {np.linspace(0, 1, 6).round(3)}")
    print(f"  eye(3):")
    print(np.eye(3))
    print(f"  random.rand(2,3):")
    np.random.seed(42)
    print(np.random.rand(2, 3).round(4))


def demo_matrices():
    print(SEP)
    print("  🔢 OPERACIONES CON MATRICES")
    print(SEP)

    A = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]], dtype=float)
    B = np.array([[9, 8, 7],
                  [6, 5, 4],
                  [3, 2, 1]], dtype=float)

    print("  Matriz A:")
    print(A)
    print("  Matriz B:")
    print(B)
    print("  A + B:")
    print(A + B)
    print("  A @ B (producto matricial):")
    print(A @ B)
    print("  A.T (transpuesta):")
    print(A.T)
    print(f"  Traza(A)          = {np.trace(A):.1f}")
    print(f"  Rango(A)          = {np.linalg.matrix_rank(A)}")


def demo_algebra_lineal():
    print(SEP)
    print("  📐 ÁLGEBRA LINEAL")
    print(SEP)

    # Matriz invertible
    M = np.array([[2, 1, 0],
                  [1, 3, 1],
                  [0, 1, 4]], dtype=float)

    print("  Matriz M:")
    print(M)
    print(f"  det(M)            = {np.linalg.det(M):.4f}")
    print("  inv(M):")
    print(np.linalg.inv(M).round(4))

    # Verificar M @ inv(M) ≈ I
    identidad = M @ np.linalg.inv(M)
    print("  M @ inv(M) ≈ I (verificación):")
    print(np.round(identidad, 10))

    # Valores y vectores propios
    vals, vecs = np.linalg.eig(M)
    print(f"\n  Eigenvalues       = {vals.round(4)}")
    print("  Eigenvectors:")
    print(vecs.round(4))

    # Solución de sistema lineal: Mx = b
    b = np.array([1, 2, 3], dtype=float)
    x = np.linalg.solve(M, b)
    print(f"\n  Solución Mx=b, b={b}")
    print(f"  x                 = {x.round(6)}")
    print(f"  Verificación M@x  = {(M @ x).round(6)}")


def demo_estadisticas():
    print(SEP)
    print("  📊 ESTADÍSTICAS CON NUMPY")
    print(SEP)
    np.random.seed(0)
    datos = np.random.normal(loc=50, scale=15, size=1000)
    print(f"  Muestra: 1000 valores ~ Normal(μ=50, σ=15)")
    print(f"  Media             = {np.mean(datos):.4f}")
    print(f"  Mediana           = {np.median(datos):.4f}")
    print(f"  Desv. estándar    = {np.std(datos):.4f}")
    print(f"  Varianza          = {np.var(datos):.4f}")
    print(f"  Mínimo            = {np.min(datos):.4f}")
    print(f"  Máximo            = {np.max(datos):.4f}")
    print(f"  Percentil 25      = {np.percentile(datos, 25):.4f}")
    print(f"  Percentil 75      = {np.percentile(datos, 75):.4f}")
    print(f"  IQR               = {np.percentile(datos, 75) - np.percentile(datos, 25):.4f}")


def demo_indexado_slicing():
    print(SEP)
    print("  🔍 INDEXADO Y SLICING AVANZADO")
    print(SEP)
    arr = np.arange(1, 26).reshape(5, 5)
    print("  Array 5×5:")
    print(arr)
    print(f"\n  arr[1, 3]         = {arr[1, 3]}")
    print(f"  arr[0, :]         = {arr[0, :]}")
    print(f"  arr[:, 2]         = {arr[:, 2]}")
    print(f"  arr[1:3, 1:4]:")
    print(arr[1:3, 1:4])
    print(f"\n  Elementos > 12:")
    print(arr[arr > 12])
    print(f"  Índices donde >12:")
    print(np.argwhere(arr > 12))


def demo_funciones_universales():
    print(SEP)
    print("  ⚡ FUNCIONES UNIVERSALES (ufuncs)")
    print(SEP)
    x = np.linspace(0, np.pi, 5)
    print(f"  x                 = {x.round(4)}")
    print(f"  sin(x)            = {np.sin(x).round(4)}")
    print(f"  cos(x)            = {np.cos(x).round(4)}")
    print(f"  exp(x/π)          = {np.exp(x / np.pi).round(4)}")
    print(f"  log1p(x)          = {np.log1p(x).round(4)}")

    a = np.array([3, -1, 5, -2, 8])
    b = np.array([1, 4, -3, 6, 2])
    print(f"\n  a                 = {a}")
    print(f"  b                 = {b}")
    print(f"  maximum(a,b)      = {np.maximum(a, b)}")
    print(f"  absolute(a)       = {np.absolute(a)}")
    print(f"  clip(a,-1,5)      = {np.clip(a, -1, 5)}")


if __name__ == "__main__":
    print("\n" + SEP)
    print("  🔢  LIBRERÍA: NumPy  (Externa)")
    print(f"  Versión: {np.__version__}")
    print(SEP + "\n")

    demo_arrays_basicos()
    demo_creacion_arrays()
    demo_matrices()
    demo_algebra_lineal()
    demo_estadisticas()
    demo_indexado_slicing()
    demo_funciones_universales()

    print(SEP)
    print("  ✅  Demo completada exitosamente.")
    print(SEP + "\n")
