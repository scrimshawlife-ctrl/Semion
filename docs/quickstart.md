# Quickstart

```bash
pip install -e ".[dev]"
python -m semion classify '{"sign_form":"national flag","object_candidate":"nation-state","classification":"symbol"}'
pytest -q
```

Expected: `sign_class=symbol`, `phenomenal=false`, `forecast_eligible=false`.
