from services.fetcher import real_estate_downloader
from utils.extractor import extract_zip_to_folder
from pathlib import Path
from utils.filter import keep_only
from utils.converter import convert_to_roc_year
import logging

logging.basicConfig(level=logging.WARNING)

def download_and_extract(year: int, season: int) -> Path:
    roc_year = convert_to_roc_year(year=year)
    zip_filename = real_estate_downloader(year=year, season=season)
    zip_path = Path(zip_filename)

    output_dir = Path(f"data/{roc_year}S{season}")
    if output_dir.exists():
        logging.warning(f"Folder already exists: {output_dir}. Skip unzip")
    else:
        extract_zip_to_folder(zip_path=zip_path, output_dir=output_dir)
        _ = keep_only(folder=output_dir, suffix="_lvr_land_a.csv")

    try:
        zip_path.unlink()
        logging.info(f"Delete zip: {zip_path}")
    except Exception:
        logging.exception("Failed to delete zip")

    return output_dir