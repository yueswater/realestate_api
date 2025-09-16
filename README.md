# Real Estate Crawler API

This project is a FastAPI-based backend service for downloading, extracting, and accessing Taiwan real estate transaction data published by the Ministry of the Interior (內政部). The service provides a RESTful API that automates the retrieval of seasonal zip archives and extracts only the relevant CSV files.

## Features

* Download quarterly transaction data ZIP files via API call
* Automatically extract and retain only `x_lvr_land_a.csv`
* Return extracted file paths and status in structured JSON
* Clean architecture with clear separation of logic
* Integrated format and linting tools (autoflake, isort, flake8)

## Tech Stack

* Python 3.12+
* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/) (ASGI server)
* [Poetry](https://python-poetry.org/) for dependency and virtual environment management

## Project Structure

```
realestate_api/
├── src/
│   ├── app/
│   │   ├── main.py              # FastAPI entry point
│   │   ├── downloader.py        # Core logic for download and unzip
│   ├── services/
│   │   └── utils/               # Optional helpers and tools
├── .gitignore
├── Makefile                    # Dev command shortcuts
├── pyproject.toml              # Poetry project configuration
```

## Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/realestate_api.git
cd realestate_api

# Install poetry and dependencies
poetry install
```

## Running the API Server

```bash
poetry shell
make run
```

Then open your browser to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Available Endpoints

| Method | Path        | Description                                              |
| ------ | ----------- | -------------------------------------------------------- |
| GET    | `/ping`     | Health check                                             |
| GET    | `/download` | Trigger download and unzip for specified year and season |

Example:

```http
GET /download?year=112&season=2
```

Response:

```json
{
  "status": 200,
  "path": "data/112S2/x_lvr_land_a.csv"
}
```

## Makefile Commands

```bash
make run       # Start FastAPI with uvicorn
make clean     # Remove all __pycache__ folders
make format    # Run autoflake and isort on src/
make lint      # Run flake8 static code checks
make check     # Run both format and lint
```

## Deployment / Monitoring

This API can be triggered periodically by services like:

* [UptimeRobot](https://uptimerobot.com/) (for HTTP GET pings)
* `cron` + `curl`
* GitHub Actions or cloud functions

## License

MIT License. See `LICENSE` for details.