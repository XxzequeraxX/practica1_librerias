"""
app.py  —  Servidor principal Flask
====================================
Dashboard interactivo: integra y ejecuta de manera dinámica los 12 scripts de
librerías Python mediante llamadas AJAX desde el frontend cyberpunk.

Uso:
    python app.py
    → Abrir http://127.0.0.1:5000
"""

import os
import sys
import io
import subprocess
import traceback
import math
import random
import csv
import json
from datetime import datetime, timedelta
from pathlib import Path

import flask
from flask import Flask, render_template, jsonify, send_from_directory, abort

# ─────────────────────────────────────────────────────────────────────────────
# Configuración de rutas
# ─────────────────────────────────────────────────────────────────────────────
BASE_DIR    = Path(__file__).parent.resolve()
OUTPUT_DIR  = BASE_DIR / "outputs"
SCRIPTS_DIR = BASE_DIR / "scripts_ejemplos"
OUTPUT_DIR.mkdir(exist_ok=True)

app = Flask(__name__)
app.secret_key = "practica1-cyberpunk-2026"

# ─────────────────────────────────────────────────────────────────────────────
# Mapa de librerías → scripts
# ─────────────────────────────────────────────────────────────────────────────
SCRIPT_MAP = {
    "math":       "01_math_ejemplo.py",
    "random":     "02_random_ejemplo.py",
    "datetime":   "03_datetime_ejemplo.py",
    "csv":        "04_csv_ejemplo.py",
    "fpdf":       "05_fpdf_ejemplo.py",
    "reportlab":  "06_reportlab_ejemplo.py",
    "numpy":      "07_numpy_ejemplo.py",
    "pandas":     "08_pandas_ejemplo.py",
    "matplotlib": "09_matplotlib_ejemplo.py",
    "requests":   "10_requests_ejemplo.py",
    "flask":      None,   # Especial: info del servidor
    "sklearn":    "12_scikit_learn_ejemplo.py",
}

# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────

def _tamanio_legible(bytes_: int) -> str:
    """Convierte bytes a formato legible."""
    for unidad in ["B", "KB", "MB", "GB"]:
        if bytes_ < 1024:
            return f"{bytes_:.1f} {unidad}"
        bytes_ /= 1024
    return f"{bytes_:.1f} TB"


def _ejecutar_script(nombre_archivo: str) -> tuple[bool, str]:
    """
    Ejecuta un script Python como subproceso y captura su stdout/stderr.
    Retorna (exito: bool, salida: str).
    """
    ruta = SCRIPTS_DIR / nombre_archivo
    if not ruta.exists():
        return False, f"Script no encontrado: {ruta}"

    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "utf-8"
    env["PYTHONUTF8"] = "1"

    resultado = subprocess.run(
        [sys.executable, str(ruta)],
        capture_output=True,
        text=True,
        timeout=60,
        encoding="utf-8",
        errors="replace",
        env=env,
    )
    salida = resultado.stdout
    if resultado.stderr:
        salida += f"\n[STDERR]\n{resultado.stderr}"

    exito = resultado.returncode == 0
    return exito, salida


def _info_flask() -> str:
    """Genera información sobre el servidor Flask actual."""
    rutas = [str(r) for r in app.url_map.iter_rules()
             if str(r) != "/static/<path:filename>"]
    lineas = [
        "=" * 55,
        "  🌍  LIBRERÍA: Flask  (Externa)",
        f"  Versión Flask     : {flask.__version__}",
        f"  Versión Python    : {sys.version.split()[0]}",
        "=" * 55,
        "",
        "  📋 RUTAS REGISTRADAS:",
        "",
    ]
    for ruta in sorted(rutas):
        lineas.append(f"    {ruta}")

    lineas += [
        "",
        "  📊 CARACTERÍSTICAS DEMOSTRADAS:",
        "    ✅ Rutas estáticas y dinámicas",
        "    ✅ Plantillas Jinja2 (render_template)",
        "    ✅ Respuestas JSON (jsonify)",
        "    ✅ Parámetros de URL (<int:id>, <float:n>)",
        "    ✅ Archivos estáticos (CSS, imágenes)",
        "    ✅ Manejadores de error (404, 500)",
        "    ✅ Flask Secret Key y sesiones",
        "    ✅ Subprocesos (ejecución de scripts)",
        "    ✅ send_from_directory (descarga de archivos)",
        "",
        "  🔗 ENDPOINTS DISPONIBLES:",
        "    GET  /                  → Dashboard principal",
        "    GET  /ejecutar/<lib>    → Ejecuta librería (JSON)",
        "    GET  /grafico/<nombre>  → Sirve imagen PNG",
        "    GET  /descargar/<arch>  → Descarga archivo",
        "    GET  /api/flask-info    → Info del servidor (JSON)",
        "",
        "=" * 55,
        "  ✅  Demo completada exitosamente.",
        "=" * 55,
    ]
    return "\n".join(lineas)


def _listar_archivos_outputs():
    """Lista los archivos en la carpeta outputs/."""
    archivos = []
    extensiones_validas = {".pdf", ".csv", ".png", ".json", ".xlsx", ".tsv"}
    for archivo in sorted(OUTPUT_DIR.iterdir()):
        if archivo.is_file() and archivo.suffix.lower() in extensiones_validas:
            archivos.append({
                "nombre":  archivo.name,
                "ext":     archivo.suffix.lstrip(".").lower(),
                "tamanio": _tamanio_legible(archivo.stat().st_size),
            })
    return archivos


def _dependencias():
    """Retorna versiones de las dependencias instaladas."""
    deps = []
    checks = [
        ("Flask",        "flask"),
        ("fpdf2",        "fpdf"),
        ("ReportLab",    "reportlab"),
        ("NumPy",        "numpy"),
        ("Pandas",       "pandas"),
        ("Matplotlib",   "matplotlib"),
        ("requests",     "requests"),
        ("scikit-learn", "sklearn"),
    ]
    for nombre, modulo in checks:
        try:
            mod = __import__(modulo)
            version = getattr(mod, "__version__", "desconocida")
        except ImportError:
            version = "no instalada"
        deps.append({"nombre": nombre, "version": version})
    return deps


# ─────────────────────────────────────────────────────────────────────────────
# Rutas Flask
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Página principal — Dashboard."""
    graficos = [
        ("grafico_barras.png",     "📊 Barras — Notas de Estudiantes"),
        ("grafico_lineas.png",     "📈 Líneas — Funciones Matemáticas"),
        ("grafico_histograma.png", "📉 Histograma — Distribución de Notas"),
        ("grafico_circular.png",   "🎯 Circular — Distribución por Carrera"),
        ("grafico_dispersion.png", "🔵 Dispersión — Horas vs Nota"),
        ("grafico_ml.png",         "🤖 ML — Regresión Lineal (scikit-learn)"),
    ]
    return render_template(
        "index.html",
        graficos=graficos,
        archivos_generados=_listar_archivos_outputs(),
        dependencias=_dependencias(),
        flask_version=flask.__version__,
        fecha_actual=datetime.now().strftime("%d/%m/%Y"),
    )


@app.route("/ejecutar/<lib>")
def ejecutar(lib: str):
    """
    Ejecuta el script correspondiente a la librería solicitada.
    Retorna JSON con {exito, salida, error?}.
    """
    if lib not in SCRIPT_MAP:
        return jsonify({"exito": False, "error": f"Librería desconocida: '{lib}'"}), 404

    # Caso especial: Flask
    if lib == "flask":
        salida = _info_flask()
        return jsonify({"exito": True, "salida": salida, "libreria": lib})

    script = SCRIPT_MAP[lib]
    try:
        exito, salida = _ejecutar_script(script)
        if exito:
            return jsonify({"exito": True, "salida": salida, "libreria": lib})
        else:
            return jsonify({"exito": False, "error": salida, "libreria": lib})
    except subprocess.TimeoutExpired:
        return jsonify({"exito": False, "error": "Timeout: el script tardó más de 60 segundos.", "libreria": lib})
    except Exception as e:
        return jsonify({"exito": False, "error": traceback.format_exc(), "libreria": lib})


@app.route("/grafico/<nombre>")
def servir_grafico(nombre: str):
    """Sirve un gráfico PNG desde la carpeta outputs/."""
    ruta = OUTPUT_DIR / nombre
    if not ruta.exists() or ruta.suffix.lower() not in (".png", ".jpg", ".jpeg"):
        abort(404)
    return send_from_directory(OUTPUT_DIR, nombre, mimetype="image/png")


@app.route("/descargar/<nombre>")
def descargar(nombre: str):
    """Descarga un archivo desde la carpeta outputs/."""
    ruta = OUTPUT_DIR / nombre
    if not ruta.exists():
        abort(404)
    extensiones_validas = {".pdf", ".csv", ".png", ".json", ".xlsx", ".tsv"}
    if ruta.suffix.lower() not in extensiones_validas:
        abort(403)
    return send_from_directory(OUTPUT_DIR, nombre, as_attachment=True)


@app.route("/api/flask-info")
def api_flask_info():
    """Endpoint JSON con información del servidor Flask."""
    rutas = []
    for rule in app.url_map.iter_rules():
        if str(rule) == "/static/<path:filename>":
            continue
        rutas.append({
            "ruta":    str(rule),
            "metodos": sorted([m for m in rule.methods if m not in ("HEAD", "OPTIONS")]),
        })
    return jsonify({
        "app":           "Práctica 1 — Librerías Python",
        "flask_version": flask.__version__,
        "python":        sys.version.split()[0],
        "debug":         app.debug,
        "timestamp":     datetime.now().isoformat(),
        "rutas":         sorted(rutas, key=lambda r: r["ruta"]),
        "archivos_outputs": [a["nombre"] for a in _listar_archivos_outputs()],
    })


@app.errorhandler(404)
def pagina_no_encontrada(e):
    return jsonify({"error": "Recurso no encontrado", "codigo": 404}), 404


@app.errorhandler(500)
def error_interno(e):
    return jsonify({"error": "Error interno del servidor", "codigo": 500}), 500


# ─────────────────────────────────────────────────────────────────────────────
# Punto de entrada
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print()
    print("═" * 60)
    print("  🐍  PRÁCTICA 1 — LIBRERÍAS PYTHON")
    print("  🌍  Dashboard Flask con tema Cyberpunk")
    print("═" * 60)
    print(f"  URL:    http://127.0.0.1:5000")
    print(f"  Salida: {OUTPUT_DIR}")
    print(f"  Flask:  v{flask.__version__}")
    print("═" * 60)
    print("  Presiona Ctrl+C para detener el servidor.")
    print()

    app.run(
        debug=True,
        port=5000,
        use_reloader=True,
        host="127.0.0.1",
    )
