# Validación del portafolio público

## Ejecutar pruebas disponibles

```powershell
uv sync --locked --group ui
uv run --group ui pytest -m "not integration"
uv run --group ui ruff check .
uv run --group ui ruff format --check .
```

El conjunto público omite de forma explícita los casos que necesitan el universo sintético privado `design-data/restricted/` o el exportador utilizado únicamente para crear esta distribución. La suite pública **no equivale** a la suite completa del repositorio de desarrollo, que anteriormente obtuvo 287 pruebas offline aprobadas en Windows.

## Demostración

```powershell
uv run --group ui streamlit run app/control_tower.py
```

La interfaz opera con el ledger sintético observable y no requiere credenciales de Atlas.

Para la presentación, inicia en otra terminal:

```powershell
py -m http.server 8765 --bind 127.0.0.1 --directory presentation-showcase
```

Navega a `http://127.0.0.1:8765/`.

## Límites

No se entrega el universo de verdad sintética, ni se afirma que la reconstrucción del simulador sea reproducible desde la edición pública. No se han demostrado ventas, retorno real ni impacto causal. Para verificar los hashes del paquete, consulta `PUBLIC-EXPORT-MANIFEST.json`.
