"""
10_requests_ejemplo.py
======================
Demostración de la librería externa: requests
Incluye: GET, manejo de respuestas JSON, headers, parámetros de query y errores HTTP.
"""

import requests
import json
import time

SEP = "=" * 55

BASE_URL = "https://jsonplaceholder.typicode.com"


def demo_get_basico():
    print(SEP)
    print("  🌐 PETICIÓN GET BÁSICA")
    print(SEP)
    url = f"{BASE_URL}/posts/1"
    response = requests.get(url, timeout=10)

    print(f"  URL               : {url}")
    print(f"  Código de estado  : {response.status_code}")
    print(f"  Tipo de contenido : {response.headers.get('Content-Type', 'N/A')}")
    print(f"  Tamaño respuesta  : {len(response.content)} bytes")
    print(f"  Tiempo respuesta  : {response.elapsed.total_seconds() * 1000:.0f} ms")

    datos = response.json()
    print(f"\n  Datos recibidos:")
    for clave, valor in datos.items():
        if isinstance(valor, str) and len(valor) > 60:
            valor = valor[:57] + "..."
        print(f"    {clave:<12}: {valor}")


def demo_lista_usuarios():
    print(SEP)
    print("  👥 LISTA DE USUARIOS (API JSONPlaceholder)")
    print(SEP)
    response = requests.get(f"{BASE_URL}/users", timeout=10)
    usuarios = response.json()

    print(f"  Usuarios encontrados: {len(usuarios)}\n")
    print(f"  {'#':<4} {'Nombre':<25} {'Username':<15} {'Email':<30}")
    print("  " + "-" * 77)
    for u in usuarios[:8]:   # Solo los primeros 8
        nombre   = u.get("name", "")[:24]
        username = u.get("username", "")[:14]
        email    = u.get("email", "")[:29]
        print(f"  {u['id']:<4} {nombre:<25} {username:<15} {email:<30}")


def demo_query_params():
    print(SEP)
    print("  🔧 PETICIONES CON PARÁMETROS")
    print(SEP)
    # Filtrar posts por usuario
    for user_id in [1, 2, 3]:
        resp = requests.get(
            f"{BASE_URL}/posts",
            params={"userId": user_id},
            timeout=10
        )
        posts = resp.json()
        print(f"  Usuario {user_id}: {len(posts)} publicaciones")

    # Álbumes del usuario 1
    resp = requests.get(f"{BASE_URL}/albums", params={"userId": 1}, timeout=10)
    albumes = resp.json()
    print(f"\n  Álbumes del usuario 1: {len(albumes)}")
    for album in albumes[:3]:
        titulo = album.get("title", "")[:50]
        print(f"    [{album['id']}] {titulo}")


def demo_headers_y_metadata():
    print(SEP)
    print("  📋 HEADERS Y METADATA")
    print(SEP)
    resp = requests.get(
        f"{BASE_URL}/posts/1",
        headers={
            "Accept": "application/json",
            "User-Agent": "Practica1-Python/1.0",
        },
        timeout=10
    )

    print("  Headers de respuesta relevantes:")
    claves_interes = [
        "Content-Type", "Content-Encoding", "Cache-Control",
        "Access-Control-Allow-Origin", "Pragma"
    ]
    for clave in claves_interes:
        valor = resp.headers.get(clave, "(no presente)")
        print(f"    {clave:<35}: {valor}")


def demo_post_simulado():
    print(SEP)
    print("  📤 SIMULACIÓN POST (envío de datos)")
    print(SEP)
    nuevo_post = {
        "title":  "Práctica 1 – Python Libraries",
        "body":   "Demostración de las 12 librerías fundamentales de Python.",
        "userId": 1,
    }
    resp = requests.post(
        f"{BASE_URL}/posts",
        json=nuevo_post,
        headers={"Content-Type": "application/json"},
        timeout=10,
    )
    print(f"  Status Code       : {resp.status_code}")
    datos = resp.json()
    print(f"  ID asignado       : {datos.get('id')}")
    print(f"  Título recibido   : {datos.get('title')}")
    print(f"  Body recibido     : {datos.get('body')[:60]}...")


def demo_manejo_errores():
    print(SEP)
    print("  ⚠️  MANEJO DE ERRORES HTTP")
    print(SEP)

    # 404 Not Found
    urls_prueba = [
        (f"{BASE_URL}/posts/9999",   "Recurso inexistente (404)"),
        (f"{BASE_URL}/users/1",      "Recurso existente (200)"),
        ("https://httpbin.org/status/500", "Error servidor (500)"),
    ]
    for url, desc in urls_prueba:
        try:
            resp = requests.get(url, timeout=8)
            emoji = "✅" if resp.ok else "❌"
            print(f"  {emoji} {desc:<35} → {resp.status_code}")
        except requests.exceptions.Timeout:
            print(f"  ⏱️  {desc:<35} → TIMEOUT")
        except requests.exceptions.ConnectionError:
            print(f"  🔌 {desc:<35} → SIN CONEXIÓN")


def demo_api_externa():
    """Consume la API pública de Open Joke para obtener un chiste."""
    print(SEP)
    print("  😄 API PÚBLICA ADICIONAL — CHISTE ALEATORIO")
    print(SEP)
    try:
        resp = requests.get(
            "https://official-joke-api.appspot.com/random_joke",
            timeout=8
        )
        if resp.status_code == 200:
            joke = resp.json()
            print(f"  Tipo    : {joke.get('type', 'general').capitalize()}")
            print(f"  Setup   : {joke.get('setup', '')}")
            print(f"  Punchline: {joke.get('punchline', '')}")
        else:
            print(f"  API respondió con status {resp.status_code}")
    except Exception as e:
        print(f"  No se pudo conectar a la API de chistes: {e}")


if __name__ == "__main__":
    print("\n" + SEP)
    print("  🌍  LIBRERÍA: requests  (Externa)")
    print("  ⚠️  Requiere conexión a internet")
    print(SEP + "\n")

    try:
        demo_get_basico()
        demo_lista_usuarios()
        demo_query_params()
        demo_headers_y_metadata()
        demo_post_simulado()
        demo_manejo_errores()
        demo_api_externa()
    except requests.exceptions.ConnectionError:
        print("  ❌ Sin conexión a internet. Conecta y vuelve a intentarlo.")
    except requests.exceptions.Timeout:
        print("  ⏱️  Las peticiones tardaron demasiado (timeout).")

    print(SEP)
    print("  ✅  Demo completada exitosamente.")
    print(SEP + "\n")
