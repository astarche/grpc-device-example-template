Create and prepare venv:

```
poetry install
```

Generate stubs for nirfmxspecan using ../grpc-device:

```
poetry run python -m generatestubs nirfmxspecan
```

Note: `settings.json` is configured to enable `black` and `mypy` in vscode.
If not using vscode.

```
poetry run black .
poetry run mypy .
```

Develop examples in the root directory and copy to grpc-device examples.
