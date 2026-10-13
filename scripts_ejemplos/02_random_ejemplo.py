"""
02_random_ejemplo.py
====================
Demostración de la librería estándar: random
Incluye: enteros aleatorios, flotantes, elección, barajado, muestras y semilla.
"""

import random
import string

SEP = "=" * 55


def demo_semilla():
    print(SEP)
    print("  🌱 SEMILLA (reproducibilidad)")
    print(SEP)
    random.seed(42)
    print(f"  Con semilla 42: {[random.randint(1, 100) for _ in range(5)]}")
    random.seed(42)
    print(f"  Repetido (=42): {[random.randint(1, 100) for _ in range(5)]}")
    random.seed()   # restablecer a semilla aleatoria del sistema
    print("  Semilla restablecida a estado del sistema.")


def demo_enteros():
    print(SEP)
    print("  🎲 NÚMEROS ENTEROS ALEATORIOS")
    print(SEP)
    print(f"  randint(1, 6)     = {random.randint(1, 6)}   ← simulación de dado")
    print(f"  randrange(0,100,5)= {random.randrange(0, 100, 5)}   ← múltiplo de 5")
    print(f"  getrandbits(8)    = {random.getrandbits(8)}   ← 8 bits aleatorios")


def demo_flotantes():
    print(SEP)
    print("  📉 FLOTANTES ALEATORIOS")
    print(SEP)
    print(f"  random()          = {random.random():.6f}   ← [0.0, 1.0)")
    print(f"  uniform(1.5, 9.5) = {random.uniform(1.5, 9.5):.6f}")
    print(f"  gauss(mu=0,σ=1)   = {random.gauss(0, 1):.6f}")
    print(f"  normalvariate      = {random.normalvariate(50, 10):.4f}")
    print(f"  expovariate(λ=1)  = {random.expovariate(1):.6f}")


def demo_secuencias():
    print(SEP)
    print("  🃏 OPERACIONES SOBRE SECUENCIAS")
    print(SEP)
    colores = ["Rojo", "Verde", "Azul", "Amarillo", "Naranja", "Violeta"]
    print(f"  Lista original    : {colores}")
    print(f"  choice()          : {random.choice(colores)}")
    print(f"  choices(k=3)      : {random.choices(colores, k=3)}")
    print(f"  sample(k=3)       : {random.sample(colores, k=3)}")

    baraja = list(range(1, 11))
    print(f"\n  Baraja antes      : {baraja}")
    random.shuffle(baraja)
    print(f"  Barajada (shuffle): {baraja}")


def demo_contrasena():
    print(SEP)
    print("  🔐 GENERADOR DE CONTRASEÑAS")
    print(SEP)
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
    for longitud in [8, 12, 16]:
        pwd = "".join(random.choices(caracteres, k=longitud))
        print(f"  Longitud {longitud:>2}:   {pwd}")


def demo_simulacion_dados():
    print(SEP)
    print("  🎯 SIMULACIÓN: 1000 lanzamientos de dado")
    print(SEP)
    conteo = {i: 0 for i in range(1, 7)}
    for _ in range(1000):
        conteo[random.randint(1, 6)] += 1
    for cara, veces in conteo.items():
        barra = "█" * (veces // 20)
        print(f"  [{cara}] {veces:>4}x  {barra}")


if __name__ == "__main__":
    print("\n" + SEP)
    print("  🎲  LIBRERÍA: random  (Estándar Python)")
    print(SEP + "\n")

    demo_semilla()
    demo_enteros()
    demo_flotantes()
    demo_secuencias()
    demo_contrasena()
    demo_simulacion_dados()

    print(SEP)
    print("  ✅  Demo completada exitosamente.")
    print(SEP + "\n")
