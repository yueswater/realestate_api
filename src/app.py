from fastapi import FastAPI, Query
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
import traceback

from src.services.downloader import real_estate_downloader

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index():
    return """
    <h1>RealEstateHub API</h1>
    <ul>
        <li><a href="/ping">Health check</a></li>
        <li><a href="/docs">API Docs</a></li>
        <li><a href="/download?year=2020&season=2">Sample download (2020 S2)</a></li>
    </ul>
    """


@app.get("/download")
def download(year: int = Query(...), season: int = Query(...)):
    try:
        zip_path = real_estate_downloader(year=year, season=season)
        return FileResponse(
            path=zip_path,
            media_type="application/zip",
            filename=zip_path.name,
        )
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"error": str(e)})


@app.get("/ping")
@app.head("/ping")
def ping():
    return {"status": "ok", "source": "api alive"}
