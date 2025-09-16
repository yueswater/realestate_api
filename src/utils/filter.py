from pathlib import Path
from typing import List


def keep_only(folder: Path, suffix: str) -> List[str]:
    folder = Path(folder)
    kept_files = []

    for file in folder.iterdir():
        if file.is_file() and suffix in file.name.lower():
            kept_files.append(file)
        else:
            file.unlink()
    return kept_files
