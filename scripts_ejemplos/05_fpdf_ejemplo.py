"""
05_fpdf_ejemplo.py
==================
Demostración de la librería externa: fpdf2
Incluye: encabezado, pie de página, texto, colores, líneas, tabla simple y múltiples páginas.
"""

import os
from fpdf import FPDF

SEP = "=" * 55

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)
ARCHIVO_PDF = os.path.join(OUTPUT_DIR, "reporte_fpdf.pdf")

DATOS_ESTUDIANTES = [
    ("Ana García",      "Ingeniería",    9.2),
    ("Luis Pérez",      "Medicina",      7.8),
    ("María López",     "Derecho",       5.1),
    ("Carlos Martín",   "Arquitectura",  4.3),
    ("Sofía Rodríguez", "Psicología",    8.6),
    ("Juan Torres",     "Informática",   9.7),
    ("Paula Sánchez",   "Biología",      3.5),
    ("Diego Morales",   "Química",       6.4),
]


class ReportePDF(FPDF):
    """PDF personalizado con encabezado y pie de página."""

    def header(self):
        # Fondo del encabezado
        self.set_fill_color(11, 11, 11)      # Negro profundo
        self.rect(0, 0, 210, 25, "F")

        # Línea decorativa roja
        self.set_draw_color(255, 30, 66)
        self.set_line_width(1.2)
        self.line(10, 23, 200, 23)

        # Título
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(255, 255, 255)
        self.set_y(5)
        self.cell(0, 12, "REPORTE ACADEMICO - PRACTICA 1", align="C", new_x="LMARGIN", new_y="NEXT")

        # Subtítulo rojo
        self.set_font("Helvetica", "", 9)
        self.set_text_color(255, 30, 66)
        self.cell(0, 5, "Generado con fpdf2 | Python", align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        # Línea
        self.set_draw_color(255, 30, 66)
        self.set_line_width(0.5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(2)
        # Texto del pie
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 5, f"Página {self.page_no()} | Librería fpdf2 — Práctica Python", align="C")

    def titulo_seccion(self, texto: str):
        self.set_fill_color(255, 30, 66)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 11)
        self.cell(0, 9, f"  {texto}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def parrafo(self, texto: str):
        self.set_text_color(40, 40, 40)
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 6, texto)
        self.ln(2)

    def tabla_estudiantes(self, datos):
        # Encabezados
        self.set_fill_color(30, 30, 30)
        self.set_text_color(255, 30, 66)
        self.set_font("Helvetica", "B", 10)
        self.set_draw_color(255, 30, 66)
        self.cell(70, 8, "Nombre",   border=1, fill=True, align="C")
        self.cell(55, 8, "Carrera",  border=1, fill=True, align="C")
        self.cell(35, 8, "Nota",     border=1, fill=True, align="C")
        self.cell(30, 8, "Estado",   border=1, fill=True, align="C", new_x="LMARGIN", new_y="NEXT")

        # Filas alternas
        for i, (nombre, carrera, nota) in enumerate(datos):
            if i % 2 == 0:
                self.set_fill_color(240, 240, 240)
            else:
                self.set_fill_color(255, 255, 255)
            self.set_text_color(30, 30, 30)
            self.set_font("Helvetica", "", 10)
            estado = "Aprobado" if nota >= 5.0 else "Reprobado"

            self.cell(70, 7, nombre,    border=1, fill=True)
            self.cell(55, 7, carrera,   border=1, fill=True)
            self.cell(35, 7, f"{nota:.1f}", border=1, fill=True, align="C")

            # Color del estado
            if estado == "Aprobado":
                self.set_text_color(0, 150, 0)
            else:
                self.set_text_color(200, 0, 0)
            self.set_font("Helvetica", "B", 10)
            self.cell(30, 7, estado,    border=1, fill=True, align="C", new_x="LMARGIN", new_y="NEXT")
        self.ln(4)


def generar_pdf():
    pdf = ReportePDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # ── Sección 1: Introducción ────────────────────────────────────────────
    pdf.titulo_seccion("1. INTRODUCCIÓN A FPDF2")
    pdf.parrafo(
        "fpdf2 es una librería Python para generar documentos PDF de manera sencilla "
        "y sin dependencias externas. Permite crear documentos con texto, imágenes, "
        "tablas, colores y múltiples páginas de manera programática.\n\n"
        "Este documento fue generado automáticamente como parte de la Práctica 1 "
        "de Librerías Python, demostrando las capacidades de fpdf2."
    )

    # ── Sección 2: Tabla de estudiantes ───────────────────────────────────
    pdf.titulo_seccion("2. TABLA DE CALIFICACIONES")
    pdf.tabla_estudiantes(DATOS_ESTUDIANTES)

    # ── Sección 3: Estadísticas ────────────────────────────────────────────
    notas = [n for _, _, n in DATOS_ESTUDIANTES]
    aprobados = sum(1 for n in notas if n >= 5.0)
    reprobados = len(notas) - aprobados
    promedio = sum(notas) / len(notas)

    pdf.titulo_seccion("3. ESTADÍSTICAS GENERALES")
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(40, 40, 40)
    stats = [
        ("Total de estudiantes",    str(len(notas))),
        ("Promedio del grupo",       f"{promedio:.2f}"),
        ("Nota máxima",             f"{max(notas):.1f}"),
        ("Nota mínima",             f"{min(notas):.1f}"),
        ("Estudiantes aprobados",    f"{aprobados} ({aprobados/len(notas)*100:.0f}%)"),
        ("Estudiantes reprobados",   f"{reprobados} ({reprobados/len(notas)*100:.0f}%)"),
    ]
    for etiqueta, valor in stats:
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(75, 7, f"  {etiqueta}:")
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(255, 30, 66)
        pdf.cell(0, 7, valor, new_x="LMARGIN", new_y="NEXT")

    # ── Sección 4: Elementos gráficos ─────────────────────────────────────
    pdf.ln(5)
    pdf.titulo_seccion("4. ELEMENTOS GRÁFICOS")

    # Barras de progreso para cada nota
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(40, 40, 40)
    pdf.cell(0, 6, "  Gráfico de barras de notas:", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    for nombre, _, nota in DATOS_ESTUDIANTES:
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(50, 50, 50)
        pdf.cell(60, 6, f"  {nombre}")

        # Barra de fondo
        x, y = pdf.get_x(), pdf.get_y()
        pdf.set_fill_color(220, 220, 220)
        pdf.rect(x, y + 1, 100, 4, "F")

        # Barra de progreso
        ancho_barra = nota * 10    # 10 puntos = nota máx 10 → 100px
        if nota >= 5.0:
            pdf.set_fill_color(0, 180, 0)
        else:
            pdf.set_fill_color(220, 0, 0)
        pdf.rect(x, y + 1, ancho_barra, 4, "F")

        # Valor
        pdf.set_x(x + 105)
        pdf.set_text_color(255, 30, 66)
        pdf.set_font("Helvetica", "B", 9)
        pdf.cell(20, 6, f"{nota:.1f}/10.0", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1)

    pdf.output(ARCHIVO_PDF)
    return ARCHIVO_PDF


if __name__ == "__main__":
    print("\n" + SEP)
    print("  📄  LIBRERÍA: fpdf2  (Externa)")
    print(SEP + "\n")

    print("  Generando PDF...")
    ruta = generar_pdf()
    print(f"  PDF creado en: {ruta}")

    print(SEP)
    print("  ✅  Demo completada exitosamente.")
    print(SEP + "\n")
