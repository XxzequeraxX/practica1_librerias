"""
03_datetime_ejemplo.py
======================
Demostración de la librería estándar: datetime
Incluye: fecha/hora actual, aritmética de fechas, formateo, timedelta y zonas horarias.
"""

from datetime import datetime, date, time, timedelta, timezone

SEP = "=" * 55


def demo_ahora():
    print(SEP)
    print("  🕐 FECHA Y HORA ACTUAL")
    print(SEP)
    ahora = datetime.now()
    hoy = date.today()
    print(f"  datetime.now()    = {ahora}")
    print(f"  date.today()      = {hoy}")
    print(f"  Año               = {ahora.year}")
    print(f"  Mes               = {ahora.month}")
    print(f"  Día               = {ahora.day}")
    print(f"  Hora              = {ahora.hour}")
    print(f"  Minuto            = {ahora.minute}")
    print(f"  Segundo           = {ahora.second}")
    print(f"  Microsegundo      = {ahora.microsecond}")


def demo_utc():
    print(SEP)
    print("  🌍 FECHA/HORA UTC")
    print(SEP)
    utc_ahora = datetime.now(timezone.utc)
    print(f"  UTC ahora         = {utc_ahora}")
    print(f"  UTC ISO format    = {utc_ahora.isoformat()}")


def demo_formateo():
    print(SEP)
    print("  🎨 FORMATEO DE FECHAS (strftime)")
    print(SEP)
    ahora = datetime.now()
    formatos = {
        "DD/MM/AAAA":           ahora.strftime("%d/%m/%Y"),
        "MM-DD-AAAA":           ahora.strftime("%m-%d-%Y"),
        "Día Mes AAAA":         ahora.strftime("%A, %d de %B de %Y"),
        "Hora 12h":             ahora.strftime("%I:%M:%S %p"),
        "Hora 24h":             ahora.strftime("%H:%M:%S"),
        "ISO 8601":             ahora.isoformat(),
        "Timestamp UNIX":       str(int(ahora.timestamp())),
        "Semana del año":       ahora.strftime("Semana %W del año %Y"),
    }
    for nombre, valor in formatos.items():
        print(f"  {nombre:<22} = {valor}")


def demo_parsing():
    print(SEP)
    print("  🔍 PARSEO DE CADENAS (strptime)")
    print(SEP)
    cadenas = [
        ("25/12/2025", "%d/%m/%Y"),
        ("2025-01-15 08:30:00", "%Y-%m-%d %H:%M:%S"),
        ("15 Enero 2025", "%d %B %Y"),
    ]
    for cadena, fmt in cadenas:
        try:
            dt = datetime.strptime(cadena, fmt)
            print(f"  '{cadena}' → {dt}")
        except ValueError:
            print(f"  No se pudo parsear '{cadena}' con '{fmt}'")


def demo_aritmetica():
    print(SEP)
    print("  ➕ ARITMÉTICA CON TIMEDELTA")
    print(SEP)
    hoy = datetime.now()
    deltas = [
        ("+ 7 días",    timedelta(days=7)),
        ("+ 30 días",   timedelta(days=30)),
        ("+ 1 año",     timedelta(days=365)),
        ("- 100 días",  timedelta(days=-100)),
        ("+ 3h 30min",  timedelta(hours=3, minutes=30)),
    ]
    for desc, delta in deltas:
        resultado = hoy + delta
        print(f"  {desc:<16} = {resultado.strftime('%d/%m/%Y %H:%M')}")


def demo_diferencia_fechas():
    print(SEP)
    print("  📅 DIFERENCIA ENTRE FECHAS")
    print(SEP)
    nacimiento = datetime(2000, 6, 15)
    ahora = datetime.now()
    diferencia = ahora - nacimiento
    print(f"  Fecha nacimiento  = {nacimiento.strftime('%d/%m/%Y')}")
    print(f"  Fecha hoy         = {ahora.strftime('%d/%m/%Y')}")
    print(f"  Diferencia total  = {diferencia.days:,} días")
    print(f"  En años aprox.    = {diferencia.days // 365} años")
    print(f"  En horas          = {int(diferencia.total_seconds() // 3600):,} horas")
    print(f"  En segundos       = {int(diferencia.total_seconds()):,} segundos")


def demo_tiempo_puro():
    print(SEP)
    print("  ⏱  OBJETO time PURO")
    print(SEP)
    t = time(14, 30, 45, 500000)
    print(f"  Hora              = {t.hour}")
    print(f"  Minuto            = {t.minute}")
    print(f"  Segundo           = {t.second}")
    print(f"  Formato 12h       = {t.strftime('%I:%M:%S %p')}")
    print(f"  Formato 24h       = {t.strftime('%H:%M:%S')}")


if __name__ == "__main__":
    print("\n" + SEP)
    print("  📅  LIBRERÍA: datetime  (Estándar Python)")
    print(SEP + "\n")

    demo_ahora()
    demo_utc()
    demo_formateo()
    demo_parsing()
    demo_aritmetica()
    demo_diferencia_fechas()
    demo_tiempo_puro()

    print(SEP)
    print("  ✅  Demo completada exitosamente.")
    print(SEP + "\n")
