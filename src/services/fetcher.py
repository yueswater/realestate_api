import requests
from utils.converter import convert_to_roc_year
from config import REAL_ESTATE_ZIP_URL_TEMPLATE

def real_estate_downloader(year: int, season: int) -> str:
    # convert AD to ROC year
    year = convert_to_roc_year(year)

    # download real estate zip file
    url = REAL_ESTATE_ZIP_URL_TEMPLATE.format(year=year, season=season)
    response = requests.get(url=url)
    response.raise_for_status()

    # validate zip format
    content_type = response.headers.get("Content-Type", "")
    if not content_type.lower().startswith(("application/zip", "application/octet-stream")):
        raise ValueError(f"Download failed: unexpected content type. Got: {content_type}")
    
    # save data
    zip_filename = f"{year}S{season}.zip"
    with open(zip_filename, "wb") as f:
        f.write(response.content)

    return zip_filename