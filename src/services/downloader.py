import logging
from pathlib import Path
import requests

from src.config import REAL_ESTATE_ZIP_URL_TEMPLATE
from src.utils.converter import convert_to_roc_year

logging.basicConfig(level=logging.WARNING)


def real_estate_downloader(year: int, season: int) -> Path:
    roc_year = convert_to_roc_year(year)

    url = REAL_ESTATE_ZIP_URL_TEMPLATE.format(year=roc_year, season=season)
    response = requests.get(url=url)
    response.raise_for_status()

    content_type = response.headers.get("Content-Type", "")
    if not content_type.lower().startswith(
        ("application/zip", "application/octet-stream")
    ):
        raise ValueError(
            f"Download failed: unexpected content type. Got: {content_type}"
        )

    zip_path = Path(f"{roc_year}S{season}.zip")
    with open(zip_path, "wb") as f:
        f.write(response.content)

    return zip_path


def download_and_extract(year: int, season: int) -> Path:
    zip_path = real_estate_downloader(year=year, season=season)
    return zip_path
