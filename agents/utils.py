from pathlib import Path
import json
from typing import Any

DATA_DIR = Path('.localdata')


def _resolve(path: str | Path) -> Path:
    p = Path(path)
    if not p.is_absolute():
        p = DATA_DIR / p
    return p


def read_json(path: str | Path, default: Any | None = None) -> Any:
    file_path = _resolve(path)
    if file_path.exists():
        with file_path.open('r', encoding='utf-8') as f:
            return json.load(f)
    return default


def write_json(path: str | Path, data: Any) -> None:
    file_path = _resolve(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
