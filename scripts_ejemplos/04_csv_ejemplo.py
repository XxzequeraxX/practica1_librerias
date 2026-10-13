"""
04_csv_ejemplo.py
=================
Demostración de la librería estándar: csv
Incluye: escritura, lectura, DictWriter, DictReader, delimitadores y manejo de errores.
"""

import csv
import os
from datetime import datetime

SEP = "=" * 55

# Carpeta de salida
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)
ARCHIVO_CSV = os.path.join(OUTPUT_DIR, "estudiantes.csv")


ESTUDIANTES = [
    {"nombre": "Ana García",      "carrera": "Ingeniería",    "nota": 9.2, "aprobado": True},
    {"nombre": "Luis Pérez",      "carrera": "Medicina",      "nota": 7.8, "aprobado": True},
    {"nombre": "María López",     "carrera": "Derecho",       "nota": 5.1, "aprobado": True},
    {"nombre": "Carlos Martín",   "carrera": "Arquitectura",  "nota": 4.3, "aprobado": False},
    {"nombre": "Sofía Rodríguez", "carrera": "Psicología",    "nota": 8.6, "aprobado": True},
    {"nombre": "Juan Torres",     "carrera": "Informática",   "nota": 9.7, "aprobado": True},
    {"nombre": "Paula Sánchez",   "carrera": "Biología",      "nota": 3.5, "aprobado": False},
    {"nombre": "Diego Morales",   "carrera": "Química",       "nota": 6.4, "aprobado": True},
]


def demo_escritura_basica():
    """Escritura simple con writer."""
    print(SEP)
    print("  ✍️  ESCRITURA BÁSICA (writer)")
    print(SEP)
    archivo = os.path.join(OUTPUT_DIR, "basico.csv")
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Producto", "Precio", "Stock"])
        writer.writerows([
            ["Laptop",  1299.99, 15],
            ["Monitor",  349.50, 42],
            ["Teclado",   89.00, 78],
            ["Ratón",     45.75, 120],
        ])
    print(f"  Archivo creado: {archivo}")
    print("  Contenido escrito: Producto, Precio, Stock (4 filas)")


def demo_dictwriter():
    """Escritura usando DictWriter."""
    print(SEP)
    print("  📝 ESCRITURA CON DictWriter")
    print(SEP)
    campos = ["nombre", "carrera", "nota", "aprobado"]
    with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(ESTUDIANTES)
    print(f"  Archivo creado   : {ARCHIVO_CSV}")
    print(f"  Total de filas   : {len(ESTUDIANTES)} estudiantes")
    print(f"  Campos           : {', '.join(campos)}")


def demo_lectura_basica():
    """Lectura simple con reader."""
    print(SEP)
    print("  📖 LECTURA BÁSICA (reader)")
    print(SEP)
    with open(ARCHIVO_CSV, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        encabezado = next(reader)
        print(f"  Encabezado: {encabezado}")
        print()
        for i, fila in enumerate(reader, 1):
            print(f"  Fila {i:>2}: {fila}")


def demo_dictreader():
    """Lectura usando DictReader."""
    print(SEP)
    print("  📚 LECTURA CON DictReader")
    print(SEP)
    with open(ARCHIVO_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print(f"  {'Nombre':<22} {'Carrera':<15} {'Nota':>6} {'Estado':>10}")
        print("  " + "-" * 57)
        for fila in reader:
            estado = "✅ Aprobado" if fila["aprobado"] == "True" else "❌ Reprobado"
            print(f"  {fila['nombre']:<22} {fila['carrera']:<15} {float(fila['nota']):>6.1f} {estado:>10}")


def demo_estadisticas():
    """Estadísticas calculadas desde el CSV."""
    print(SEP)
    print("  📊 ESTADÍSTICAS DESDE CSV")
    print(SEP)
    notas = []
    aprobados = reprobados = 0
    carreras = {}

    with open(ARCHIVO_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            nota = float(fila["nota"])
            notas.append(nota)
            if fila["aprobado"] == "True":
                aprobados += 1
            else:
                reprobados += 1
            carrera = fila["carrera"]
            carreras[carrera] = carreras.get(carrera, 0) + 1

    total = len(notas)
    print(f"  Total estudiantes : {total}")
    print(f"  Promedio notas    : {sum(notas)/total:.2f}")
    print(f"  Nota más alta     : {max(notas)}")
    print(f"  Nota más baja     : {min(notas)}")
    print(f"  Aprobados         : {aprobados} ({aprobados/total*100:.1f}%)")
    print(f"  Reprobados        : {reprobados} ({reprobados/total*100:.1f}%)")
    print(f"\n  Carreras representadas:")
    for carrera, n in carreras.items():
        print(f"    - {carrera}: {n} estudiante(s)")


def demo_delimitadores():
    """CSV con diferentes delimitadores."""
    print(SEP)
    print("  🔧 CSV CON DELIMITADORES DISTINTOS")
    print(SEP)
    archivo_tsv = os.path.join(OUTPUT_DIR, "datos_tab.tsv")
    with open(archivo_tsv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter="\t")
        writer.writerow(["Ciudad", "País", "Población"])
        writer.writerows([
            ["Madrid",   "España",    "3.3M"],
            ["Lima",     "Perú",      "9.7M"],
            ["Buenos Aires", "Argentina", "15.2M"],
        ])
    print(f"  Archivo TSV creado: {archivo_tsv}")

    # Lectura del TSV
    with open(archivo_tsv, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for fila in reader:
            print(f"    {' | '.join(fila)}")


if __name__ == "__main__":
    print("\n" + SEP)
    print("  📄  LIBRERÍA: csv  (Estándar Python)")
    print(SEP + "\n")

    demo_escritura_basica()
    demo_dictwriter()
    demo_lectura_basica()
    demo_dictreader()
    demo_estadisticas()
    demo_delimitadores()

    print(SEP)
    print("  ✅  Demo completada exitosamente.")
    print(SEP + "\n")
