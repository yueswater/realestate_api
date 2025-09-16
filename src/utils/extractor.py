import zipfile
from pathlib import Path


def extract_zip_to_folder(zip_path: Path, output_dir: Path):
    if not zip_path.exists():
        raise FileNotFoundError(f"Cannot find zip file {zip_path}")
    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(output_dir)
