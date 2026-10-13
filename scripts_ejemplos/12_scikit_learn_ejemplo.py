"""
12_scikit_learn_ejemplo.py
==========================
Demostración de la librería externa: scikit-learn
Modelo de Regresión Lineal: predice notas de estudiantes según horas de estudio.
Incluye: split, entrenamiento, evaluación (R², MSE, MAE), predicción y visualización.
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

SEP = "=" * 55

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Paleta cyberpunk
BG_COLOR  = "#0b0b0b"
RED_NEON  = "#ff1e42"
CYAN_GLOW = "#00e5ff"
WHITE     = "#ffffff"
GRAY      = "#888888"


def generar_datos():
    """Genera un dataset sintético realista de estudiantes."""
    np.random.seed(2024)
    n = 150

    horas_estudio   = np.random.uniform(2, 50, n)
    horas_suenio    = np.random.uniform(4, 10, n)
    asistencia_pct  = np.random.uniform(50, 100, n)

    # Nota es una combinación lineal + ruido
    nota = (
        0.15 * horas_estudio
        + 0.10 * horas_suenio
        + 0.04 * asistencia_pct
        + np.random.normal(0, 1.0, n)
    )
    nota = np.clip(nota, 0, 10)

    return horas_estudio, horas_suenio, asistencia_pct, nota


def demo_regresion_simple():
    """Regresión Lineal Simple: horas_estudio → nota."""
    print(SEP)
    print("  📏 REGRESIÓN LINEAL SIMPLE")
    print("      horas_estudio → nota_final")
    print(SEP)

    horas, _, _, notas = generar_datos()
    X = horas.reshape(-1, 1)
    y = notas

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"  Datos totales     : {len(X)}")
    print(f"  Train / Test      : {len(X_train)} / {len(X_test)}")

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)

    r2  = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"\n  Coeficiente (m)   : {modelo.coef_[0]:.6f}")
    print(f"  Intercepto (b)    : {modelo.intercept_:.6f}")
    print(f"  Ecuación          : nota = {modelo.coef_[0]:.4f} × horas + {modelo.intercept_:.4f}")
    print(f"\n  📊 Métricas de evaluación:")
    print(f"  R²  (R-cuadrado)  : {r2:.4f}  {'★ Muy bueno' if r2 > 0.85 else '✓ Aceptable' if r2 > 0.6 else '◈ Mejorable'}")
    print(f"  MSE (Error cuadr.)  : {mse:.4f}")
    print(f"  RMSE              : {np.sqrt(mse):.4f}")
    print(f"  MAE (Error medio) : {mae:.4f}")

    # Predicciones de ejemplo
    print(f"\n  💡 Predicciones:")
    ejemplos = [5, 10, 20, 30, 40, 50]
    print(f"  {'Horas':>6} → {'Nota predicha':>14}")
    print("  " + "-" * 25)
    for h in ejemplos:
        pred = modelo.predict([[h]])[0]
        pred = np.clip(pred, 0, 10)
        print(f"  {h:>6} horas → {pred:>12.2f}/10")

    return modelo, X_train, X_test, y_train, y_test, y_pred, horas, notas


def demo_regresion_multiple():
    """Regresión Lineal Múltiple: múltiples variables → nota."""
    print(SEP)
    print("  📐 REGRESIÓN LINEAL MÚLTIPLE")
    print("      horas + sueño + asistencia → nota_final")
    print(SEP)

    horas, suenio, asistencia, notas = generar_datos()
    X = np.column_stack([horas, suenio, asistencia])
    y = notas

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Pipeline con escalado
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("modelo", LinearRegression()),
    ])
    pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)

    r2  = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    modelo = pipeline.named_steps["modelo"]
    variables = ["Horas estudio", "Horas sueño", "Asistencia %"]

    print(f"  Variables usadas  : {', '.join(variables)}")
    print(f"\n  Coeficientes:")
    for var, coef in zip(variables, modelo.coef_):
        direccion = "↑" if coef > 0 else "↓"
        print(f"    {var:<20}: {coef:>8.5f} {direccion}")
    print(f"    {'Intercepto':<20}: {modelo.intercept_:>8.5f}")

    print(f"\n  📊 Métricas:")
    print(f"  R²                : {r2:.4f}")
    print(f"  MSE               : {mse:.4f}")
    print(f"  RMSE              : {np.sqrt(mse):.4f}")
    print(f"  MAE               : {mae:.4f}")

    print(f"\n  💡 Predicción de ejemplo:")
    ejemplo = np.array([[35, 7.5, 85]])
    pred = np.clip(pipeline.predict(ejemplo)[0], 0, 10)
    print(f"    35h estudio, 7.5h sueño, 85% asistencia → {pred:.2f}/10")

    return y_test, y_pred


def generar_grafico(modelo, X_train, X_test, y_train, y_test, y_pred_simple,
                    y_test_multi, y_pred_multi, horas_full, notas_full):
    """Genera gráfico comparativo de los modelos."""
    fig, axes = plt.subplots(2, 2, figsize=(12, 9), facecolor=BG_COLOR)
    fig.suptitle("🤖 MACHINE LEARNING — REGRESIÓN LINEAL\nLibrería: scikit-learn",
                 color=WHITE, fontsize=14, fontweight="bold", y=0.98)

    # ─ Subplot 1: Datos + línea de regresión ─────────────────────────────────
    ax1 = axes[0, 0]
    ax1.set_facecolor(BG_COLOR)
    ax1.scatter(X_train, y_train, color="#ff6680", alpha=0.5, s=25, label="Train", zorder=3)
    ax1.scatter(X_test,  y_test,  color=CYAN_GLOW, alpha=0.8, s=35, label="Test",  zorder=4)
    x_linea = np.linspace(horas_full.min(), horas_full.max(), 100).reshape(-1, 1)
    y_linea = modelo.predict(x_linea)
    ax1.plot(x_linea, y_linea, color=RED_NEON, linewidth=2.5, label="Regresión", zorder=5)
    ax1.set_title("Regresión Simple: Horas → Nota", color=WHITE, fontsize=11, fontweight="bold")
    ax1.set_xlabel("Horas de estudio", color=GRAY, fontsize=9)
    ax1.set_ylabel("Nota final", color=GRAY, fontsize=9)
    ax1.tick_params(colors=GRAY)
    ax1.legend(facecolor="#1a1a1a", edgecolor=RED_NEON, labelcolor=WHITE, fontsize=8)
    ax1.grid(True, color="#1e1e1e", linewidth=0.7)
    for sp in ax1.spines.values(): sp.set_edgecolor("#333")

    # ─ Subplot 2: Real vs Predicho (modelo simple) ───────────────────────────
    ax2 = axes[0, 1]
    ax2.set_facecolor(BG_COLOR)
    rango = [min(y_test.min(), y_pred_simple.min()), max(y_test.max(), y_pred_simple.max())]
    ax2.scatter(y_test, y_pred_simple, color=RED_NEON, alpha=0.7, s=40, zorder=3)
    ax2.plot(rango, rango, color=CYAN_GLOW, linewidth=1.5, linestyle="--", label="y=ŷ ideal", zorder=4)
    ax2.set_title("Real vs Predicho (Simple)", color=WHITE, fontsize=11, fontweight="bold")
    ax2.set_xlabel("Nota real", color=GRAY, fontsize=9)
    ax2.set_ylabel("Nota predicha", color=GRAY, fontsize=9)
    ax2.tick_params(colors=GRAY)
    ax2.legend(facecolor="#1a1a1a", edgecolor=RED_NEON, labelcolor=WHITE, fontsize=8)
    ax2.grid(True, color="#1e1e1e", linewidth=0.7)
    for sp in ax2.spines.values(): sp.set_edgecolor("#333")

    # ─ Subplot 3: Real vs Predicho (modelo múltiple) ─────────────────────────
    ax3 = axes[1, 0]
    ax3.set_facecolor(BG_COLOR)
    rango2 = [min(y_test_multi.min(), y_pred_multi.min()),
              max(y_test_multi.max(), y_pred_multi.max())]
    ax3.scatter(y_test_multi, y_pred_multi, color=CYAN_GLOW, alpha=0.7, s=40, zorder=3)
    ax3.plot(rango2, rango2, color=RED_NEON, linewidth=1.5, linestyle="--", label="y=ŷ ideal", zorder=4)
    ax3.set_title("Real vs Predicho (Múltiple)", color=WHITE, fontsize=11, fontweight="bold")
    ax3.set_xlabel("Nota real", color=GRAY, fontsize=9)
    ax3.set_ylabel("Nota predicha", color=GRAY, fontsize=9)
    ax3.tick_params(colors=GRAY)
    ax3.legend(facecolor="#1a1a1a", edgecolor=RED_NEON, labelcolor=WHITE, fontsize=8)
    ax3.grid(True, color="#1e1e1e", linewidth=0.7)
    for sp in ax3.spines.values(): sp.set_edgecolor("#333")

    # ─ Subplot 4: Residuos ────────────────────────────────────────────────────
    ax4 = axes[1, 1]
    ax4.set_facecolor(BG_COLOR)
    residuos = y_test - y_pred_simple
    ax4.scatter(y_pred_simple, residuos, color=RED_NEON, alpha=0.7, s=40, zorder=3)
    ax4.axhline(0, color=CYAN_GLOW, linewidth=1.5, linestyle="--", zorder=4)
    ax4.set_title("Gráfico de Residuos", color=WHITE, fontsize=11, fontweight="bold")
    ax4.set_xlabel("Valor predicho", color=GRAY, fontsize=9)
    ax4.set_ylabel("Residuo (real − predicho)", color=GRAY, fontsize=9)
    ax4.tick_params(colors=GRAY)
    ax4.grid(True, color="#1e1e1e", linewidth=0.7)
    for sp in ax4.spines.values(): sp.set_edgecolor("#333")

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    ruta = os.path.join(OUTPUT_DIR, "grafico_ml.png")
    fig.savefig(ruta, dpi=120, bbox_inches="tight", facecolor=BG_COLOR)
    plt.close(fig)
    return ruta


if __name__ == "__main__":
    import sklearn
    print("\n" + SEP)
    print("  🤖  LIBRERÍA: scikit-learn  (Externa)")
    print(f"  Versión: {sklearn.__version__}")
    print(SEP + "\n")

    modelo, X_train, X_test, y_train, y_test, y_pred_s, horas_f, notas_f = demo_regresion_simple()
    y_test_m, y_pred_m = demo_regresion_multiple()

    print(SEP)
    print("  🎨 Generando gráficos...")
    ruta_grafico = generar_grafico(
        modelo, X_train, X_test, y_train, y_test, y_pred_s,
        y_test_m, y_pred_m, horas_f, notas_f
    )
    print(f"  Gráfico guardado en: {ruta_grafico}")

    print(SEP)
    print("  ✅  Demo completada exitosamente.")
    print(SEP + "\n")
