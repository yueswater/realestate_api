from pathlib import Path
import requests
from src.config import REAL_ESTATE_ZIP_URL_TEMPLATE
from src.utils.converter import convert_to_roc_year


def real_estate_downloader(year: int, season: int) -> Path:
    roc_year = convert_to_roc_year(year)
    url = REAL_ESTATE_ZIP_URL_TEMPLATE.format(year=roc_year, season=season)
    response = requests.get(url)
    response.raise_for_status()

    zip_path = Path(f"{roc_year}S{season}.zip")
    with open(zip_path, "wb") as f:
        f.write(response.content)

    return zip_path