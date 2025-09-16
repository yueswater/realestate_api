import traceback
from pathlib import Path

from fastapi import FastAPI, Query, status
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse

from src.services.downloader import download_and_extract

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <h1>RealEstateHub API</h1>
    <ul>
        <li><a href="/ping">Health check</a></li>
        <li><a href="/docs">API Docs</a></li>
    </ul>
    """


@app.get("/download")
def download(year: int = Query(...), season: int = Query(...)):
    try:
        output_path = download_and_extract(year=year, season=season)
        return {"status": status.HTTP_200_OK, "path": str(output_path)}
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"status": "error", "detail": str(e)},
        )


@app.get("/download/file")
def download_file(year: int, season: int):
    zip_path = Path(f"data/{year - 1911}S{season}.zip")

    if zip_path.exists():
        return FileResponse(
            path=zip_path, media_type="application/zip", filename=zip_path.name
        )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": f"File not found: {zip_path}"},
    )


@app.get("/ping")
@app.head("/ping")
def ping():
    return {"status": "ok", "source": "api alive"}