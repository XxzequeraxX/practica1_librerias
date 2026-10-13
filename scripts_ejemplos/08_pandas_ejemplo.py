"""
08_pandas_ejemplo.py
====================
Demostración de la librería externa: Pandas
Incluye: Series, DataFrame, filtrado, agrupación, estadísticas y exportación.
"""

import pandas as pd
import numpy as np
import os

SEP = "=" * 55

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def demo_series():
    print(SEP)
    print("  📈 SERIES DE PANDAS")
    print(SEP)
    # Series con índice personalizado
    temperaturas = pd.Series(
        [22.5, 19.0, 25.3, 21.8, 28.1, 16.4, 23.7],
        index=["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"],
        name="Temperatura (°C)"
    )
    print(f"  Serie de temperaturas semanales:\n{temperatures_display(temperaturas)}")
    print(f"\n  Máximo: {temperaturas.max():.1f}°C ({temperaturas.idxmax()})")
    print(f"  Mínimo: {temperaturas.min():.1f}°C ({temperaturas.idxmin()})")
    print(f"  Promedio: {temperaturas.mean():.2f}°C")
    print(f"  Días con >22°C: {list(temperaturas[temperaturas > 22].index)}")


def temperatures_display(serie):
    """Formatea la serie para mostrar en consola."""
    lines = []
    for idx, val in serie.items():
        lines.append(f"    {idx}: {val}")
    return "\n".join(lines)


def crear_dataframe():
    """Crea y retorna el DataFrame principal de estudiantes."""
    np.random.seed(42)
    n = 20
    nombres = [
        "Ana García", "Luis Pérez", "María López", "Carlos Martín",
        "Sofía Rodríguez", "Juan Torres", "Paula Sánchez", "Diego Morales",
        "Elena Castro", "Miguel Fernández", "Laura Jiménez", "Pedro Ruiz",
        "Carmen Vargas", "Antonio Díaz", "Rosa Méndez", "Francisco Herrera",
        "Isabel Guerrero", "Javier Navarro", "Marta Ríos", "David Blanco"
    ]
    carreras = ["Ingeniería", "Medicina", "Derecho", "Arquitectura", "Psicología",
                "Informática", "Biología", "Química"]
    ciudades  = ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao", "Lima", "Bogotá"]

    df = pd.DataFrame({
        "nombre":       nombres,
        "carrera":      np.random.choice(carreras, n),
        "ciudad":       np.random.choice(ciudades, n),
        "nota_final":   np.round(np.random.uniform(2.0, 10.0, n), 2),
        "horas_estudio":np.random.randint(5, 50, n),
        "edad":         np.random.randint(18, 30, n),
        "semestre":     np.random.randint(1, 10, n),
    })
    df["aprobado"] = df["nota_final"] >= 5.0
    return df


def demo_dataframe_basico(df):
    print(SEP)
    print("  📋 DATAFRAME — VISTA GENERAL")
    print(SEP)
    print(f"  Shape              : {df.shape}  ({df.shape[0]} filas × {df.shape[1]} columnas)")
    print(f"  Columnas           : {list(df.columns)}")
    print(f"  Tipos de datos:\n{df.dtypes.to_string()}")
    print(f"\n  Primeras 5 filas:\n{df.head().to_string(index=False)}")
    print(f"\n  Estadísticas descriptivas:")
    print(df[["nota_final", "horas_estudio", "edad", "semestre"]].describe().round(2).to_string())


def demo_filtrado(df):
    print(SEP)
    print("  🔍 FILTRADO Y SELECCIÓN")
    print(SEP)
    aprobados = df[df["aprobado"] == True]
    print(f"  Total estudiantes  : {len(df)}")
    print(f"  Aprobados          : {len(aprobados)}")
    print(f"  Reprobados         : {len(df) - len(aprobados)}")

    # Filtro combinado
    alto_rendimiento = df[(df["nota_final"] >= 8.0) & (df["horas_estudio"] >= 30)]
    print(f"\n  Alto rendimiento (nota≥8 Y horas≥30):")
    if len(alto_rendimiento) > 0:
        print(alto_rendimiento[["nombre", "nota_final", "horas_estudio"]].to_string(index=False))
    else:
        print("  (Ningún estudiante cumple el criterio)")

    # Estudiantes de ingeniería
    ing = df[df["carrera"] == "Ingeniería"]
    print(f"\n  Estudiantes de Ingeniería: {len(ing)}")


def demo_agrupacion(df):
    print(SEP)
    print("  📊 AGRUPACIÓN (groupby)")
    print(SEP)
    resumen = df.groupby("carrera").agg(
        total=("nombre", "count"),
        nota_promedio=("nota_final", "mean"),
        nota_max=("nota_final", "max"),
        nota_min=("nota_final", "min"),
        aprobados=("aprobado", "sum"),
        horas_promedio=("horas_estudio", "mean"),
    ).round(2).sort_values("nota_promedio", ascending=False)

    print(f"\n  Resumen por carrera:")
    print(resumen.to_string())


def demo_manipulacion(df):
    print(SEP)
    print("  🔧 MANIPULACIÓN DE DATOS")
    print(SEP)

    # Nueva columna calculada
    df = df.copy()
    df["rendimiento"] = pd.cut(
        df["nota_final"],
        bins=[0, 4.9, 6.9, 8.4, 10.0],
        labels=["Deficiente", "Suficiente", "Notable", "Sobresaliente"]
    )
    print("  Distribución por nivel de rendimiento:")
    conteo = df["rendimiento"].value_counts().sort_index()
    for nivel, n in conteo.items():
        barra = "▓" * n
        print(f"    {str(nivel):<15}: {n:>2}  {barra}")

    # Ordenar por nota
    top5 = df.nlargest(5, "nota_final")[["nombre", "carrera", "nota_final", "horas_estudio"]]
    print(f"\n  🏆 Top 5 estudiantes:")
    print(top5.to_string(index=False))


def demo_exportacion(df):
    print(SEP)
    print("  💾 EXPORTACIÓN DE DATOS")
    print(SEP)

    # CSV
    ruta_csv = os.path.join(OUTPUT_DIR, "pandas_estudiantes.csv")
    df.to_csv(ruta_csv, index=False, encoding="utf-8")
    print(f"  CSV guardado en    : {ruta_csv}")

    # Excel (solo si openpyxl está disponible)
    try:
        ruta_excel = os.path.join(OUTPUT_DIR, "pandas_estudiantes.xlsx")
        df.to_excel(ruta_excel, index=False, sheet_name="Estudiantes")
        print(f"  Excel guardado en  : {ruta_excel}")
    except ImportError:
        print("  (Excel omitido: instala openpyxl para exportar)")

    # JSON
    ruta_json = os.path.join(OUTPUT_DIR, "pandas_estudiantes.json")
    df.to_json(ruta_json, orient="records", force_ascii=False, indent=2)
    print(f"  JSON guardado en   : {ruta_json}")


def demo_valores_nulos():
    print(SEP)
    print("  ❓ MANEJO DE VALORES NULOS")
    print(SEP)
    datos_con_nulos = pd.DataFrame({
        "nombre": ["Alice", "Bob", "Carol", "Dan", "Eve"],
        "nota":   [8.5, None, 7.2, None, 9.1],
        "ciudad": ["Lima", None, "Bogotá", "Madrid", None],
    })
    print("  DataFrame con nulos:")
    print(datos_con_nulos.to_string())
    print(f"\n  Nulos por columna:\n{datos_con_nulos.isnull().sum().to_string()}")

    # Rellenar nulos
    relleno = datos_con_nulos.copy()
    relleno["nota"].fillna(relleno["nota"].mean(), inplace=True)
    relleno["ciudad"].fillna("Sin especificar", inplace=True)
    print(f"\n  Después de rellenar nulos:")
    print(relleno.to_string())


if __name__ == "__main__":
    print("\n" + SEP)
    print("  🐼  LIBRERÍA: Pandas  (Externa)")
    print(f"  Versión: {pd.__version__}")
    print(SEP + "\n")

    df = crear_dataframe()
    demo_series()
    demo_dataframe_basico(df)
    demo_filtrado(df)
    demo_agrupacion(df)
    demo_manipulacion(df)
    demo_exportacion(df)
    demo_valores_nulos()

    print(SEP)
    print("  ✅  Demo completada exitosamente.")
    print(SEP + "\n")
