import traceback
from fastapi import FastAPI, Query, status
from fastapi.responses import JSONResponse
from src.services.downloader import download_and_extract

app = FastAPI()

@app.get("/download")
def download(year: int = Query(...), season: int = Query(...)):
    try:
        output_path = download_and_extract(year=year, season=season)
        return {
            "status": status.HTTP_200_OK,
            "path": str(output_path)
        }
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status": "error",
                "detail": str(e)
            }
        )

@app.get("/ping", status_code=status.HTTP_200_OK)
def ping():
    return {"status": "ok", "source": "api alive"}