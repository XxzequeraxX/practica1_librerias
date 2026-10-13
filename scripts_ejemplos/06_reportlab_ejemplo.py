"""
06_reportlab_ejemplo.py
=======================
Demostración de la librería externa: reportlab
Incluye: estilos de párrafo, tabla con formato avanzado, colores, flowables y layout.
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.graphics.shapes import Drawing, Rect, String
from reportlab.graphics import renderPDF

SEP = "=" * 55

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)
ARCHIVO_PDF = os.path.join(OUTPUT_DIR, "reporte_reportlab.pdf")

# ── Colores del tema ──────────────────────────────────────────────────────────
NEGRO      = colors.HexColor("#0b0b0b")
ROJO_NEON  = colors.HexColor("#ff1e42")
BLANCO     = colors.white
GRIS_CLARO = colors.HexColor("#f0f0f0")
GRIS_MEDIO = colors.HexColor("#d0d0d0")
ROJO_SUAVE = colors.HexColor("#ff6680")


def crear_estilos():
    """Crea y retorna estilos de párrafo personalizados."""
    estilos = getSampleStyleSheet()

    estilos.add(ParagraphStyle(
        name="TituloPortada",
        fontSize=26,
        fontName="Helvetica-Bold",
        textColor=BLANCO,
        backColor=NEGRO,
        alignment=TA_CENTER,
        spaceAfter=8,
        spaceBefore=20,
    ))

    estilos.add(ParagraphStyle(
        name="SubtituloPortada",
        fontSize=13,
        fontName="Helvetica",
        textColor=ROJO_NEON,
        alignment=TA_CENTER,
        spaceAfter=4,
    ))

    estilos.add(ParagraphStyle(
        name="TituloSeccion",
        fontSize=14,
        fontName="Helvetica-Bold",
        textColor=BLANCO,
        backColor=ROJO_NEON,
        alignment=TA_LEFT,
        spaceBefore=12,
        spaceAfter=6,
        leftIndent=6,
    ))

    estilos.add(ParagraphStyle(
        name="CuerpoTexto",
        fontSize=10,
        fontName="Helvetica",
        textColor=colors.HexColor("#333333"),
        alignment=TA_LEFT,
        spaceAfter=4,
        leading=14,
    ))

    estilos.add(ParagraphStyle(
        name="Pie",
        fontSize=8,
        fontName="Helvetica-Oblique",
        textColor=colors.grey,
        alignment=TA_CENTER,
    ))

    return estilos


def crear_grafico_barras():
    """Crea un gráfico de barras simple usando reportlab graphics."""
    datos = [
        ("Python",      92),
        ("Java",        75),
        ("JavaScript",  88),
        ("C++",         65),
        ("Rust",        48),
    ]
    ancho, alto = 400, 130
    drawing = Drawing(ancho, alto)

    # Fondo
    drawing.add(Rect(0, 0, ancho, alto, fillColor=colors.HexColor("#f9f9f9"), strokeColor=None))

    max_val = 100
    barra_ancho = 55
    espacio = 20
    x_inicio = 30

    for i, (lenguaje, valor) in enumerate(datos):
        x = x_inicio + i * (barra_ancho + espacio)
        h = (valor / max_val) * 90
        y = 25

        # Barra
        color_barra = ROJO_NEON if valor == max(v for _, v in datos) else colors.HexColor("#cc1133")
        drawing.add(Rect(x, y, barra_ancho, h, fillColor=color_barra, strokeColor=None))

        # Etiqueta del lenguaje
        drawing.add(String(x + barra_ancho / 2, 10, lenguaje,
                           fontSize=8, fontName="Helvetica", fillColor=NEGRO,
                           textAnchor="middle"))
        # Valor
        drawing.add(String(x + barra_ancho / 2, y + h + 3, f"{valor}%",
                           fontSize=8, fontName="Helvetica-Bold", fillColor=NEGRO,
                           textAnchor="middle"))

    return drawing


def generar_pdf():
    doc = SimpleDocTemplate(
        ARCHIVO_PDF,
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=1.5 * cm,
        bottomMargin=2 * cm,
    )

    estilos = crear_estilos()
    elementos = []

    # ── Portada ───────────────────────────────────────────────────────────────
    elementos.append(Spacer(1, 1.5 * cm))
    elementos.append(Paragraph("REPORTE AVANZADO", estilos["TituloPortada"]))
    elementos.append(Paragraph("Generado con ReportLab — Práctica 1 Python", estilos["SubtituloPortada"]))
    elementos.append(HRFlowable(width="100%", thickness=2, color=ROJO_NEON, spaceAfter=12))
    elementos.append(Spacer(1, 0.5 * cm))

    # Tabla de portada
    portada_data = [
        ["Campo",           "Detalle"],
        ["Librería",        "ReportLab"],
        ["Versión",         "4.x"],
        ["Propósito",       "Generación de PDFs profesionales"],
        ["Tipo",            "Dependencia externa (pip)"],
        ["Fecha generación","Práctica 1 — 2026"],
    ]
    tabla_portada = Table(portada_data, colWidths=[4 * cm, 12 * cm])
    tabla_portada.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, 0), NEGRO),
        ("TEXTCOLOR",    (0, 0), (-1, 0), ROJO_NEON),
        ("FONTNAME",     (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",     (0, 0), (-1, 0), 11),
        ("ALIGN",        (0, 0), (-1, 0), "CENTER"),
        ("BACKGROUND",   (0, 1), (0, -1), NEGRO),
        ("TEXTCOLOR",    (0, 1), (0, -1), ROJO_NEON),
        ("FONTNAME",     (0, 1), (0, -1), "Helvetica-Bold"),
        ("FONTSIZE",     (0, 1), (-1, -1), 10),
        ("ROWBACKGROUNDS", (1, 1), (-1, -1), [BLANCO, GRIS_CLARO]),
        ("TEXTCOLOR",    (1, 1), (-1, -1), NEGRO),
        ("GRID",         (0, 0), (-1, -1), 0.5, GRIS_MEDIO),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",   (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 5),
        ("LEFTPADDING",  (0, 0), (-1, -1), 8),
    ]))
    elementos.append(tabla_portada)
    elementos.append(Spacer(1, 0.8 * cm))

    # ── Sección 1: Descripción ────────────────────────────────────────────────
    elementos.append(Paragraph("1. DESCRIPCIÓN DE REPORTLAB", estilos["TituloSeccion"]))
    elementos.append(Paragraph(
        "ReportLab es una potente y versátil librería Python para la creación de documentos PDF "
        "complejos. Utiliza un motor de layout de alto nivel llamado <b>Platypus</b> (Page Layout "
        "and Typography Using Scripts) que permite definir el contenido de manera abstracta y "
        "dejar que el motor gestione automáticamente la paginación, los saltos de página y el flujo "
        "del contenido.",
        estilos["CuerpoTexto"]
    ))
    elementos.append(Paragraph(
        "Es especialmente potente para la generación de <b>informes empresariales</b>, "
        "facturas, catálogos, certificados y cualquier documento que requiera un diseño "
        "preciso y profesional.",
        estilos["CuerpoTexto"]
    ))
    elementos.append(Spacer(1, 0.3 * cm))

    # ── Sección 2: Tabla de calificaciones ────────────────────────────────────
    elementos.append(Paragraph("2. TABLA DE CALIFICACIONES ACADÉMICAS", estilos["TituloSeccion"]))

    estudiantes = [
        ["Nombre",          "Carrera",       "Nota",  "Estado"],
        ["Ana García",      "Ingeniería",    "9.2",   "✓ Aprobado"],
        ["Luis Pérez",      "Medicina",      "7.8",   "✓ Aprobado"],
        ["María López",     "Derecho",       "5.1",   "✓ Aprobado"],
        ["Carlos Martín",   "Arquitectura",  "4.3",   "✗ Reprobado"],
        ["Sofía Rodríguez", "Psicología",    "8.6",   "✓ Aprobado"],
        ["Juan Torres",     "Informática",   "9.7",   "✓ Aprobado"],
        ["Paula Sánchez",   "Biología",      "3.5",   "✗ Reprobado"],
        ["Diego Morales",   "Química",       "6.4",   "✓ Aprobado"],
    ]

    tabla_est = Table(estudiantes, colWidths=[5.5 * cm, 4.5 * cm, 2.5 * cm, 3.5 * cm])
    estilos_tabla = [
        # Encabezado
        ("BACKGROUND",    (0, 0), (-1, 0), NEGRO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), ROJO_NEON),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, 0), 10),
        ("ALIGN",         (0, 0), (-1, 0), "CENTER"),
        # Filas de datos
        ("FONTSIZE",      (0, 1), (-1, -1), 9),
        ("FONTNAME",      (0, 1), (-1, -1), "Helvetica"),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [BLANCO, GRIS_CLARO]),
        ("TEXTCOLOR",     (0, 1), (-1, -1), NEGRO),
        ("ALIGN",         (2, 1), (2, -1), "CENTER"),
        ("ALIGN",         (3, 1), (3, -1), "CENTER"),
        # Bordes
        ("GRID",          (0, 0), (-1, -1), 0.5, GRIS_MEDIO),
        ("LINEBELOW",     (0, 0), (-1, 0), 1.5, ROJO_NEON),
        # Padding
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
    ]
    # Colorear celdas de estado
    for i, fila in enumerate(estudiantes[1:], 1):
        if "Reprobado" in fila[3]:
            estilos_tabla.append(("TEXTCOLOR", (3, i), (3, i), colors.red))
            estilos_tabla.append(("FONTNAME",  (3, i), (3, i), "Helvetica-Bold"))
        else:
            estilos_tabla.append(("TEXTCOLOR", (3, i), (3, i), colors.HexColor("#007700")))
            estilos_tabla.append(("FONTNAME",  (3, i), (3, i), "Helvetica-Bold"))

    tabla_est.setStyle(TableStyle(estilos_tabla))
    elementos.append(tabla_est)
    elementos.append(Spacer(1, 0.5 * cm))

    # ── Sección 3: Gráfico ────────────────────────────────────────────────────
    elementos.append(Paragraph("3. POPULARIDAD DE LENGUAJES DE PROGRAMACIÓN", estilos["TituloSeccion"]))
    elementos.append(Paragraph(
        "El siguiente gráfico de barras fue generado directamente con el módulo "
        "<b>reportlab.graphics</b>, sin librerías externas adicionales:",
        estilos["CuerpoTexto"]
    ))
    elementos.append(Spacer(1, 0.3 * cm))
    elementos.append(crear_grafico_barras())
    elementos.append(Spacer(1, 0.5 * cm))

    # ── Sección 4: Características clave ──────────────────────────────────────
    elementos.append(Paragraph("4. CARACTERÍSTICAS CLAVE DE REPORTLAB", estilos["TituloSeccion"]))
    caracteristicas = [
        ["Característica",          "Descripción"],
        ["SimpleDocTemplate",       "Plantilla de documento con paginación automática"],
        ["Platypus Flowables",      "Párrafos, tablas, imágenes que fluyen entre páginas"],
        ["TableStyle",              "Estilos granulares por celda, fila o columna"],
        ["ParagraphStyle",          "Estilos tipográficos completamente personalizables"],
        ["HRFlowable",              "Líneas horizontales decorativas"],
        ["Drawing / Graphics",      "Gráficos vectoriales sin dependencias externas"],
        ["Soporte de fuentes",      "TTF, OTF, PDF Type1 y fuentes embebidas"],
    ]
    tabla_car = Table(caracteristicas, colWidths=[5 * cm, 11 * cm])
    tabla_car.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), NEGRO),
        ("TEXTCOLOR",     (0, 0), (-1, 0), ROJO_NEON),
        ("FONTNAME",      (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE",      (0, 0), (-1, -1), 9),
        ("BACKGROUND",    (0, 1), (0, -1), NEGRO),
        ("TEXTCOLOR",     (0, 1), (0, -1), ROJO_NEON),
        ("FONTNAME",      (0, 1), (0, -1), "Helvetica-Bold"),
        ("ROWBACKGROUNDS",(1, 1), (-1, -1), [BLANCO, GRIS_CLARO]),
        ("TEXTCOLOR",     (1, 1), (-1, -1), NEGRO),
        ("GRID",          (0, 0), (-1, -1), 0.4, GRIS_MEDIO),
        ("TOPPADDING",    (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
    ]))
    elementos.append(tabla_car)
    elementos.append(Spacer(1, 1 * cm))

    # Pie de documento
    elementos.append(HRFlowable(width="100%", thickness=1, color=ROJO_NEON))
    elementos.append(Spacer(1, 0.2 * cm))
    elementos.append(Paragraph(
        "Documento generado con <b>ReportLab</b> — Práctica 1 de Librerías Python | 2026",
        estilos["Pie"]
    ))

    doc.build(elementos)
    return ARCHIVO_PDF


if __name__ == "__main__":
    print("\n" + SEP)
    print("  📊  LIBRERÍA: reportlab  (Externa)")
    print(SEP + "\n")

    print("  Generando PDF con ReportLab...")
    ruta = generar_pdf()
    print(f"  PDF creado en: {ruta}")

    print(SEP)
    print("  ✅  Demo completada exitosamente.")
    print(SEP + "\n")
