from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import json
import time

BASE = Path("/opt/ota/ota_data")
API_KEY = "CHANGE_ME_LONG_RANDOM"

app = FastAPI(title="ESP32 OTA Server")
