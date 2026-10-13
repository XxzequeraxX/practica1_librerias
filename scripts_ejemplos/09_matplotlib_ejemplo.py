"""
09_matplotlib_ejemplo.py
========================
Demostración de la librería externa: Matplotlib
Genera 4 gráficos con tema oscuro/cyberpunk y los guarda como PNG.
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")   # backend sin pantalla (para uso en servidor)
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

SEP = "=" * 55

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Paleta cyberpunk ─────────────────────────────────────────────────────────
BG_COLOR   = "#0b0b0b"
RED_NEON   = "#ff1e42"
WHITE      = "#ffffff"
RED_SOFT   = "#ff6680"
RED_DARK   = "#990020"
GRAY_LIGHT = "#888888"
CYAN_GLOW  = "#00e5ff"
PINK_GLOW  = "#ff00aa"


def aplicar_estilo_base(ax, titulo: str, xlabel: str = "", ylabel: str = ""):
    """Aplica el estilo cyberpunk oscuro a un eje."""
    ax.set_facecolor(BG_COLOR)
    ax.set_title(titulo, color=WHITE, fontsize=13, fontweight="bold", pad=12)
    if xlabel:
        ax.set_xlabel(xlabel, color=GRAY_LIGHT, fontsize=10)
    if ylabel:
        ax.set_ylabel(ylabel, color=GRAY_LIGHT, fontsize=10)
    ax.tick_params(colors=GRAY_LIGHT, labelsize=9)
    for spine in ax.spines.values():
        spine.set_edgecolor("#333333")
    ax.grid(True, color="#1e1e1e", linestyle="--", linewidth=0.7, alpha=0.8)


def grafico_barras():
    """Gráfico de barras: notas de estudiantes."""
    nombres = ["Ana", "Luis", "María", "Carlos", "Sofía", "Juan", "Paula", "Diego"]
    notas   = [9.2, 7.8, 5.1, 4.3, 8.6, 9.7, 3.5, 6.4]
    colores = [RED_NEON if n >= 5.0 else "#ff000088" for n in notas]

    fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG_COLOR)
    barras = ax.bar(nombres, notas, color=colores, edgecolor="#00000044", linewidth=0.8, zorder=3)

    # Línea de aprobación
    ax.axhline(y=5.0, color=CYAN_GLOW, linewidth=1.5, linestyle="--", alpha=0.8, label="Mínimo aprobatorio (5.0)", zorder=4)

    # Etiquetas en barras
    for barra, nota in zip(barras, notas):
        ax.text(barra.get_x() + barra.get_width() / 2, barra.get_height() + 0.15,
                f"{nota:.1f}", ha="center", va="bottom", color=WHITE, fontsize=9, fontweight="bold")

    aplicar_estilo_base(ax, "📊 NOTAS DE ESTUDIANTES", "Estudiante", "Calificación (0–10)")
    ax.set_ylim(0, 11)
    ax.legend(facecolor="#1a1a1a", edgecolor=RED_NEON, labelcolor=WHITE, fontsize=9)

    plt.tight_layout()
    ruta = os.path.join(OUTPUT_DIR, "grafico_barras.png")
    fig.savefig(ruta, dpi=120, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    print(f"  Gráfico de barras guardado: {ruta}")
    return ruta


def grafico_lineas():
    """Gráfico de líneas: funciones matemáticas."""
    x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

    fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG_COLOR)

    ax.plot(x, np.sin(x),    color=RED_NEON,  linewidth=2.0, label="sin(x)",     zorder=3)
    ax.plot(x, np.cos(x),    color=CYAN_GLOW, linewidth=2.0, label="cos(x)",     zorder=3, linestyle="--")
    ax.plot(x, np.sin(2*x),  color=PINK_GLOW, linewidth=1.5, label="sin(2x)",    zorder=3, linestyle=":")
    ax.plot(x, np.tanh(x),   color="#88ff00", linewidth=1.5, label="tanh(x)",    zorder=3, linestyle="-.")

    ax.axhline(0, color="#555555", linewidth=0.8)
    ax.axvline(0, color="#555555", linewidth=0.8)

    aplicar_estilo_base(ax, "📈 FUNCIONES MATEMÁTICAS", "x (radianes)", "f(x)")
    ax.legend(facecolor="#1a1a1a", edgecolor=RED_NEON, labelcolor=WHITE, fontsize=9, ncol=2)

    plt.tight_layout()
    ruta = os.path.join(OUTPUT_DIR, "grafico_lineas.png")
    fig.savefig(ruta, dpi=120, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    print(f"  Gráfico de líneas guardado: {ruta}")
    return ruta


def grafico_histograma():
    """Histograma de distribución normal."""
    np.random.seed(0)
    datos = np.random.normal(loc=65, scale=12, size=500)

    fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG_COLOR)

    n, bins, patches = ax.hist(datos, bins=25, color=RED_NEON, edgecolor=BG_COLOR,
                               linewidth=0.5, alpha=0.85, zorder=3)

    # Curva de densidad aproximada
    from scipy.stats import norm as scipy_norm
    try:
        mu, sigma = scipy_norm.fit(datos)
        x_curva = np.linspace(datos.min(), datos.max(), 200)
        p = scipy_norm.pdf(x_curva, mu, sigma)
        # Escalar a frecuencia
        ax.plot(x_curva, p * len(datos) * (bins[1] - bins[0]),
                color=CYAN_GLOW, linewidth=2.5, label=f"Normal(μ={mu:.1f}, σ={sigma:.1f})", zorder=4)
        ax.legend(facecolor="#1a1a1a", edgecolor=RED_NEON, labelcolor=WHITE, fontsize=9)
    except ImportError:
        pass   # scipy no disponible

    ax.axvline(np.mean(datos), color=WHITE, linewidth=1.5, linestyle="--",
               label=f"Media = {np.mean(datos):.1f}")

    aplicar_estilo_base(ax, "📉 HISTOGRAMA — DISTRIBUCIÓN DE NOTAS", "Nota", "Frecuencia")
    plt.tight_layout()
    ruta = os.path.join(OUTPUT_DIR, "grafico_histograma.png")
    fig.savefig(ruta, dpi=120, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    print(f"  Histograma guardado: {ruta}")
    return ruta


def grafico_circular():
    """Gráfico circular: distribución de carreras."""
    carreras = ["Ingeniería", "Medicina", "Derecho", "Arquitectura", "Psicología",
                "Informática", "Biología", "Química"]
    valores  = [23, 18, 15, 12, 11, 10, 7, 4]

    paleta = [
        RED_NEON, "#cc0033", RED_SOFT, "#ff4466",
        PINK_GLOW, "#cc0066", "#990044", "#660022"
    ]
    explotar = [0.05 if i == 0 else 0 for i in range(len(carreras))]

    fig, ax = plt.subplots(figsize=(9, 6), facecolor=BG_COLOR)
    wedges, texts, autotexts = ax.pie(
        valores,
        labels=None,
        autopct="%1.1f%%",
        colors=paleta,
        explode=explotar,
        startangle=140,
        pctdistance=0.75,
        wedgeprops={"edgecolor": BG_COLOR, "linewidth": 2},
    )
    for autotext in autotexts:
        autotext.set_color(WHITE)
        autotext.set_fontsize(9)
        autotext.set_fontweight("bold")

    ax.set_facecolor(BG_COLOR)
    ax.set_title("🎓 DISTRIBUCIÓN POR CARRERA", color=WHITE, fontsize=13,
                 fontweight="bold", pad=15)

    # Leyenda personalizada
    leyenda = [mpatches.Patch(color=p, label=f"{c} ({v}%)") for c, p, v in
               zip(carreras, paleta, valores)]
    ax.legend(handles=leyenda, loc="center left", bbox_to_anchor=(1, 0.5),
              facecolor="#1a1a1a", edgecolor=RED_NEON, labelcolor=WHITE, fontsize=8)

    plt.tight_layout()
    ruta = os.path.join(OUTPUT_DIR, "grafico_circular.png")
    fig.savefig(ruta, dpi=120, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    print(f"  Gráfico circular guardado: {ruta}")
    return ruta


def grafico_dispersion():
    """Gráfico de dispersión: horas de estudio vs nota."""
    np.random.seed(7)
    horas = np.random.randint(5, 50, 40)
    notas = np.clip(horas * 0.18 + np.random.normal(0, 1.2, 40), 0, 10)

    fig, ax = plt.subplots(figsize=(9, 5), facecolor=BG_COLOR)

    scatter = ax.scatter(horas, notas, c=notas, cmap="RdYlGn", vmin=0, vmax=10,
                         s=70, edgecolors=WHITE, linewidths=0.4, alpha=0.9, zorder=3)

    # Línea de tendencia
    m, b = np.polyfit(horas, notas, 1)
    x_trend = np.linspace(horas.min(), horas.max(), 100)
    ax.plot(x_trend, m * x_trend + b, color=CYAN_GLOW, linewidth=2,
            linestyle="--", label=f"Tendencia: y={m:.3f}x+{b:.2f}", zorder=4)

    cb = fig.colorbar(scatter, ax=ax, pad=0.01)
    cb.set_label("Nota final", color=GRAY_LIGHT)
    cb.ax.yaxis.set_tick_params(color=GRAY_LIGHT)
    plt.setp(cb.ax.yaxis.get_ticklabels(), color=GRAY_LIGHT)

    aplicar_estilo_base(ax, "🔵 HORAS DE ESTUDIO vs NOTA FINAL", "Horas de Estudio", "Nota Final")
    ax.legend(facecolor="#1a1a1a", edgecolor=RED_NEON, labelcolor=WHITE, fontsize=9)

    plt.tight_layout()
    ruta = os.path.join(OUTPUT_DIR, "grafico_dispersion.png")
    fig.savefig(ruta, dpi=120, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    print(f"  Gráfico de dispersión guardado: {ruta}")
    return ruta


if __name__ == "__main__":
    print("\n" + SEP)
    print("  📈  LIBRERÍA: Matplotlib  (Externa)")
    print(f"  Versión: {matplotlib.__version__}")
    print(SEP + "\n")

    rutas = []
    rutas.append(grafico_barras())
    rutas.append(grafico_lineas())
    rutas.append(grafico_histograma())
    rutas.append(grafico_circular())
    rutas.append(grafico_dispersion())

    print(f"\n  Total de gráficos generados: {len(rutas)}")
    print(SEP)
    print("  ✅  Demo completada exitosamente.")
    print(SEP + "\n")
