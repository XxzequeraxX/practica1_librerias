"""
11_flask_ejemplo.py
===================
Demostración de la librería externa: Flask (mini-aplicación independiente)
Este script muestra los conceptos básicos de Flask: rutas, métodos HTTP,
plantillas inline, parámetros de URL y respuestas JSON.
Corre en el puerto 5001 para no conflictuar con app.py (puerto 5000).
"""

from flask import Flask, jsonify, request, abort
from datetime import datetime
import random
import math

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

# ── Datos en memoria ──────────────────────────────────────────────────────────
LIBROS = [
    {"id": 1, "titulo": "Python Crash Course",  "autor": "Eric Matthes",      "año": 2019},
    {"id": 2, "titulo": "Clean Code",           "autor": "Robert C. Martin",  "año": 2008},
    {"id": 3, "titulo": "The Pragmatic Programmer","autor": "David Thomas",   "año": 2019},
    {"id": 4, "titulo": "Fluent Python",         "autor": "Luciano Ramalho",  "año": 2022},
    {"id": 5, "titulo": "Design Patterns",       "autor": "Gang of Four",     "año": 1994},
]

# ─────────────────────────────────────────────────────────────────────────────
# Rutas
# ─────────────────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Página de inicio con HTML inline."""
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Flask Demo — Práctica 1</title>
        <style>
            body { background:#0b0b0b; color:#fff; font-family:monospace; padding:30px; }
            h1   { color:#ff1e42; border-bottom:2px solid #ff1e42; padding-bottom:10px; }
            a    { color:#ff6680; text-decoration:none; display:block; margin:6px 0; }
            a:hover { color:#ff1e42; text-decoration:underline; }
            code { background:#1a1a1a; padding:2px 6px; border-radius:3px; color:#ff1e42; }
            .ruta{ background:#111; border-left:3px solid #ff1e42; padding:8px 14px; margin:4px 0; }
        </style>
    </head>
    <body>
        <h1>🌐 Flask Mini-Demo</h1>
        <p>Librería: <strong>Flask</strong> | Práctica 1 de Python</p>
        <h2>Rutas disponibles:</h2>
        <div class="ruta"><a href="/info">/info</a> — Información del servidor</div>
        <div class="ruta"><a href="/libros">/libros</a> — Lista de libros (JSON)</div>
        <div class="ruta"><a href="/libros/1">/libros/&lt;id&gt;</a> — Libro por ID</div>
        <div class="ruta"><a href="/calculadora/15/3">/calculadora/&lt;a&gt;/&lt;b&gt;</a> — Operaciones</div>
        <div class="ruta"><a href="/aleatorio">/aleatorio</a> — Datos aleatorios</div>
        <div class="ruta"><a href="/eco?mensaje=Hola+Flask">/eco?mensaje=...</a> — Eco de parámetro</div>
        <div class="ruta"><a href="/ping">/ping</a> — Health check</div>
    </body>
    </html>
    """
    return html


@app.route("/info")
def info():
    """Información del servidor y de la aplicación."""
    return jsonify({
        "aplicacion": "Flask Mini-Demo",
        "version":    "1.0.0",
        "autor":      "Práctica 1 — Python",
        "servidor":   "Flask Development Server",
        "python":     "3.x",
        "timestamp":  datetime.now().isoformat(),
        "rutas":      [str(rule) for rule in app.url_map.iter_rules()
                       if str(rule) != "/static/<path:filename>"],
    })


@app.route("/libros")
def listar_libros():
    """Devuelve todos los libros en formato JSON."""
    return jsonify({
        "total":  len(LIBROS),
        "libros": LIBROS,
    })


@app.route("/libros/<int:libro_id>")
def obtener_libro(libro_id: int):
    """Devuelve un libro por su ID."""
    libro = next((l for l in LIBROS if l["id"] == libro_id), None)
    if libro is None:
        abort(404)
    return jsonify(libro)


@app.route("/libros", methods=["POST"])
def crear_libro():
    """Crea un nuevo libro (requiere JSON en el body)."""
    datos = request.get_json()
    if not datos or "titulo" not in datos or "autor" not in datos:
        return jsonify({"error": "Se requieren 'titulo' y 'autor'"}), 400

    nuevo = {
        "id":     max(l["id"] for l in LIBROS) + 1,
        "titulo": datos["titulo"],
        "autor":  datos["autor"],
        "año":    datos.get("año", datetime.now().year),
    }
    LIBROS.append(nuevo)
    return jsonify({"mensaje": "Libro creado", "libro": nuevo}), 201


@app.route("/calculadora/<float:a>/<float:b>")
def calculadora(a: float, b: float):
    """Realiza operaciones matemáticas con dos números."""
    resultado = {
        "operandos": {"a": a, "b": b},
        "suma":      a + b,
        "resta":     a - b,
        "producto":  a * b,
        "cociente":  round(a / b, 6) if b != 0 else "División por cero",
        "modulo":    round(a % b, 6) if b != 0 else "División por cero",
        "potencia":  round(a ** b, 6) if abs(b) < 20 else "Número muy grande",
        "sqrt_a":    round(math.sqrt(abs(a)), 6),
        "sqrt_b":    round(math.sqrt(abs(b)), 6),
    }
    return jsonify(resultado)


@app.route("/aleatorio")
def aleatorio():
    """Genera datos aleatorios en cada petición."""
    return jsonify({
        "numero_entero":   random.randint(1, 1000),
        "numero_flotante": round(random.uniform(0, 100), 4),
        "color_hex":       f"#{random.randint(0, 0xFFFFFF):06x}",
        "dado_6":          random.randint(1, 6),
        "dado_20":         random.randint(1, 20),
        "lista_loteria":   sorted(random.sample(range(1, 50), 6)),
        "timestamp":       datetime.now().isoformat(),
    })


@app.route("/eco")
def eco():
    """Devuelve el mensaje enviado como parámetro."""
    mensaje = request.args.get("mensaje", "¡Hola, Flask!")
    return jsonify({
        "mensaje_original": mensaje,
        "mayusculas":       mensaje.upper(),
        "minusculas":       mensaje.lower(),
        "longitud":         len(mensaje),
        "invertido":        mensaje[::-1],
        "palabras":         mensaje.split(),
    })


@app.route("/ping")
def ping():
    """Health check endpoint."""
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat()})


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Recurso no encontrado", "codigo": 404}), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Método no permitido", "codigo": 405}), 405


if __name__ == "__main__":
    print("\n" + "=" * 55)
    print("  🌍  LIBRERÍA: Flask  (Externa)")
    print("  Puerto: 5001")
    print("  URL:    http://127.0.0.1:5001")
    print("=" * 55 + "\n")
    app.run(debug=True, port=5001, use_reloader=False)
