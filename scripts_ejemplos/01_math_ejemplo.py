"""
01_math_ejemplo.py
==================
Demostración de la librería estándar: math
Incluye: trigonometría, logaritmos, constantes, potencias, raíces y factoriales.
"""

import math

# ─── Separador visual ────────────────────────────────────────────────────────
SEP = "=" * 55


def demo_constantes():
    print(SEP)
    print("  📐 CONSTANTES MATEMÁTICAS")
    print(SEP)
    print(f"  π  (pi)           = {math.pi:.10f}")
    print(f"  e  (euler)        = {math.e:.10f}")
    print(f"  τ  (tau = 2π)     = {math.tau:.10f}")
    print(f"  ∞  (infinito)     = {math.inf}")
    print(f"  nan               = {math.nan}")


def demo_redondeo():
    print(SEP)
    print("  🔢 REDONDEO Y VALOR ABSOLUTO")
    print(SEP)
    numero = -7.85
    print(f"  Número            = {numero}")
    print(f"  floor({numero})   = {math.floor(numero)}")
    print(f"  ceil({numero})    = {math.ceil(numero)}")
    print(f"  trunc({numero})   = {math.trunc(numero)}")
    print(f"  fabs({numero})    = {math.fabs(numero)}")


def demo_potencias_raices():
    print(SEP)
    print("  💪 POTENCIAS Y RAÍCES")
    print(SEP)
    x = 64
    print(f"  Número base       = {x}")
    print(f"  sqrt({x})         = {math.sqrt(x)}")
    print(f"  cbrt({x})         = {math.cbrt(x):.4f}")   # raíz cúbica (Python 3.11+)
    print(f"  pow(2, 10)        = {math.pow(2, 10):.0f}")
    print(f"  exp(3)            = {math.exp(3):.6f}")
    print(f"  log({x})          = {math.log(x):.6f}")
    print(f"  log10({x})        = {math.log10(x):.6f}")
    print(f"  log2({x})         = {math.log2(x):.6f}")


def demo_trigonometria():
    print(SEP)
    print("  📡 TRIGONOMETRÍA")
    print(SEP)
    angulos_grad = [0, 30, 45, 60, 90, 180]
    print(f"  {'Grados':>8} | {'Radianes':>10} | {'sin':>8} | {'cos':>8} | {'tan':>10}")
    print("  " + "-" * 53)
    for g in angulos_grad:
        r = math.radians(g)
        tan_val = f"{math.tan(r):.4f}" if g != 90 else "  ±∞  "
        print(f"  {g:>8}° | {r:>10.4f} | {math.sin(r):>8.4f} | {math.cos(r):>8.4f} | {tan_val:>10}")


def demo_combinatoria():
    print(SEP)
    print("  🎰 COMBINATORIA Y FACTORIAL")
    print(SEP)
    for n in [0, 5, 10, 15]:
        print(f"  {n}!               = {math.factorial(n):,}")
    print()
    print(f"  comb(10, 3)       = {math.comb(10, 3)}")   # combinaciones C(n,k)
    print(f"  perm(10, 3)       = {math.perm(10, 3)}")   # permutaciones P(n,k)


def demo_misc():
    print(SEP)
    print("  🔬 FUNCIONES ADICIONALES")
    print(SEP)
    print(f"  gcd(48, 18)       = {math.gcd(48, 18)}")
    print(f"  lcm(4, 6)         = {math.lcm(4, 6)}")
    print(f"  isfinite(1.0)     = {math.isfinite(1.0)}")
    print(f"  isinf(math.inf)   = {math.isinf(math.inf)}")
    print(f"  isnan(math.nan)   = {math.isnan(math.nan)}")
    print(f"  dist([0,0],[3,4]) = {math.dist([0, 0], [3, 4])}")   # distancia euclidiana
    print(f"  hypot(3, 4)       = {math.hypot(3, 4)}")


if __name__ == "__main__":
    print("\n" + SEP)
    print("  🧮  LIBRERÍA: math  (Estándar Python)")
    print(SEP + "\n")

    demo_constantes()
    demo_redondeo()
    demo_potencias_raices()
    demo_trigonometria()
    demo_combinatoria()
    demo_misc()

    print(SEP)
    print("  ✅  Demo completada exitosamente.")
    print(SEP + "\n")
