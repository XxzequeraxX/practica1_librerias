# 📦 Práctica 1 – Librerías de Python

> **Asignatura:** Programación Avanzada en Python  
> **Práctica:** Nro. 1 – Exploración de Librerías Fundamentales  
> **Tema:** Demostración práctica de 12 librerías esenciales de Python mediante una interfaz web con estética Cyberpunk.

---

## 📁 Estructura del Proyecto

```
practica1_librerias/
│
├── app.py                        # Servidor principal Flask (punto de entrada)
├── requirements.txt              # Dependencias externas del proyecto
├── README.md                     # Este archivo
├── .gitignore                    # Archivos y carpetas ignorados por Git
│
├── static/
│   └── style.css                 # Hoja de estilos: fondo negro, rojo neón, texto blanco
│
├── templates/
│   └── index.html                # Dashboard web interactivo (HTML + Jinja2)
│
├── outputs/                      # Archivos generados en tiempo de ejecución
│   ├── *.pdf                     # PDFs generados por fpdf2 y reportlab
│   ├── *.csv                     # Archivos CSV generados por la librería csv
│   └── *.png                     # Gráficos generados por matplotlib
│
└── scripts_ejemplos/             # Scripts individuales e independientes por librería
    ├── 01_math_ejemplo.py
    ├── 02_random_ejemplo.py
    ├── 03_datetime_ejemplo.py
    ├── 04_csv_ejemplo.py
    ├── 05_fpdf_ejemplo.py
    ├── 06_reportlab_ejemplo.py
    ├── 07_numpy_ejemplo.py
    ├── 08_pandas_ejemplo.py
    ├── 09_matplotlib_ejemplo.py
    ├── 10_requests_ejemplo.py
    ├── 11_flask_ejemplo.py
    └── 12_scikit_learn_ejemplo.py
```

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clonar o descargar el proyecto

```bash
git clone <url-del-repositorio>
cd practica1_librerias
```

### 2. Crear y activar un entorno virtual (recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación web Flask

```bash
python app.py
```

Luego abre tu navegador en: **http://127.0.0.1:5000**

### 5. Ejecutar scripts individuales (opcional)

Cada script en `scripts_ejemplos/` puede ejecutarse de manera independiente:

```bash
python scripts_ejemplos/01_math_ejemplo.py
python scripts_ejemplos/07_numpy_ejemplo.py
# ... etc.
```

---

## 📚 Librerías Utilizadas

### 1. 🔢 `math` (Estándar)
La librería `math` proporciona funciones matemáticas de bajo nivel definidas por el estándar C. Incluye operaciones trigonométricas, logarítmicas, exponenciales, constantes como π y e, y funciones de redondeo.

**Uso en el proyecto:** Cálculos de trigonometría, logaritmos, raíces cuadradas y uso de constantes matemáticas.

---

### 2. 🎲 `random` (Estándar)
La librería `random` implementa generadores de números pseudoaleatorios para diversas distribuciones. Permite generar enteros aleatorios, flotantes, escoger elementos de listas, barajar secuencias, etc.

**Uso en el proyecto:** Simulación de dados, generación de contraseñas, selección aleatoria de elementos y muestreo.

---

### 3. 📅 `datetime` (Estándar)
La librería `datetime` ofrece clases para manipular fechas y horas. Permite calcular diferencias de tiempo, formatear fechas, trabajar con zonas horarias y realizar operaciones aritméticas con fechas.

**Uso en el proyecto:** Mostrar la fecha y hora actual, calcular diferencias entre fechas, formatear fechas en distintos estilos.

---

### 4. 📄 `csv` (Estándar)
La librería `csv` permite leer y escribir archivos en formato CSV (Comma-Separated Values). Es esencial para el intercambio de datos tabulares con otras aplicaciones como Excel.

**Uso en el proyecto:** Escritura de datos de estudiantes en un archivo CSV y posterior lectura/presentación de los mismos.

---

### 5. 📝 `fpdf2` (Externa)
`fpdf2` es una librería de generación de PDFs en Python, pura y sin dependencias externas. Permite crear documentos PDF con texto, fuentes, colores, líneas, rectángulos e imágenes.

**Instalación:** `pip install fpdf2`

**Uso en el proyecto:** Generación de un reporte PDF simple con encabezado, contenido y pie de página personalizado.

---

### 6. 📊 `reportlab` (Externa)
`ReportLab` es una potente librería para crear documentos PDF complejos en Python. Soporta platillas (Platypus), estilos de párrafo, tablas con formato avanzado, imágenes y gráficos vectoriales.

**Instalación:** `pip install reportlab`

**Uso en el proyecto:** Generación de un PDF profesional con estilos, colores de fondo en celdas, tabla de datos y logo textual.

---

### 7. 🔢 `numpy` (Externa)
`NumPy` (Numerical Python) es la librería fundamental para el cómputo científico en Python. Proporciona soporte para arrays multidimensionales de alto rendimiento, junto con una gran colección de funciones matemáticas para operar sobre estos arrays.

**Instalación:** `pip install numpy`

**Uso en el proyecto:** Creación de matrices, operaciones matriciales (multiplicación, transpuesta, inversa), estadísticas descriptivas y álgebra lineal.

---

### 8. 🐼 `pandas` (Externa)
`Pandas` es una librería de análisis y manipulación de datos de código abierto. Ofrece estructuras de datos flexibles (Series y DataFrame) optimizadas para trabajar con datos relacionales o etiquetados.

**Instalación:** `pip install pandas`

**Uso en el proyecto:** Creación de DataFrames con datos de estudiantes, filtrado, agrupación, estadísticas descriptivas y exportación.

---

### 9. 📈 `matplotlib` (Externa)
`Matplotlib` es la librería de visualización de datos más popular de Python. Permite crear una amplia variedad de gráficos estáticos, animados e interactivos: líneas, barras, tortas, dispersión, histogramas, etc.

**Instalación:** `pip install matplotlib`

**Uso en el proyecto:** Generación de gráfico de barras, gráfico de líneas, histograma y gráfico circular, guardados como imágenes PNG.

---

### 10. 🌐 `requests` (Externa)
`Requests` es una librería HTTP elegante y simple para Python. Permite realizar peticiones HTTP/HTTPS (GET, POST, PUT, DELETE) de manera sencilla, manejar parámetros, cabeceras, autenticación y respuestas JSON.

**Instalación:** `pip install requests`

**Uso en el proyecto:** Consumo de la API pública de JSONPlaceholder para obtener datos de usuarios, publicaciones y álbumes.

---

### 11. 🌍 `flask` (Externa)
`Flask` es un microframework web para Python, ligero y fácil de usar. Es la base de la aplicación principal de este proyecto. Permite definir rutas, manejar peticiones HTTP, renderizar plantillas HTML con Jinja2 y servir archivos estáticos.

**Instalación:** `pip install flask`

**Uso en el proyecto:** Servidor web principal que integra y muestra los resultados de todas las demás librerías en un dashboard interactivo.

---

### 12. 🤖 `scikit-learn` (Externa)
`scikit-learn` es la librería de Machine Learning más popular de Python. Proporciona herramientas simples y eficientes para análisis predictivo: clasificación, regresión, clustering, reducción de dimensionalidad, selección de modelos y preprocesamiento.

**Instalación:** `pip install scikit-learn`

**Uso en el proyecto:** Entrenamiento de un modelo de Regresión Lineal para predecir calificaciones de estudiantes basándose en horas de estudio, con métricas de evaluación (R², MSE, MAE).

---

## 🎨 Tema Visual

La interfaz web implementa una estética **Cyberpunk / Neón** con:

| Elemento | Color | Código Hex |
|----------|-------|------------|
| Fondo principal | Negro profundo | `#0b0b0b` |
| Acentos y botones | Rojo neón | `#ff1e42` |
| Texto y títulos | Blanco | `#ffffff` |
| Bordes luminosos | Rojo neón con glow | `#ff1e42` + `box-shadow` |

---

## 📋 Requisitos del Sistema

- **Python:** 3.9 o superior
- **pip:** 21.0 o superior
- **Navegador:** Chrome, Firefox, Edge (versión moderna)
- **Conexión a internet:** Requerida para la demo de `requests` (API pública)

---

## 👨‍💻 Autor

> Práctica desarrollada como parte de la asignatura de Programación Avanzada.  
> Universidad — Semestre Académico 2026.
