from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from ai_analyzer import analyze_idea, generate_ideas
from web_search import gather_for_analysis, gather_for_generation

# Load environment variables from .env
load_dotenv()

app = FastAPI(title="AGI Idea Analyzer", version="3.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FIELDS = [
    # Engineering
    "Computer Science & IT",
    "Artificial Intelligence & ML",
    "Electronics & Communication",
    "Electrical Engineering",
    "Mechanical Engineering",
    "Civil & Structural Engineering",
    "Robotics & Automation",
    "IoT & Embedded Systems",
    "Cybersecurity",
    "Data Science & Analytics",
    "Chemical Engineering",
    "Biomedical Engineering",
    "Aerospace Engineering",
    "Environmental Engineering",
    "Game Development",
    "AR / VR & Metaverse",
    "Blockchain & Web3",
    "Cloud & DevOps",
    "Automotive & EV Technology",
    "Nanotechnology & Materials",
    # Other domains
    "Healthcare & MedTech",
    "Education & EdTech",
    "Finance & Fintech",
    "Agriculture & AgriTech",
    "Manufacturing & Industry 4.0",
    "Retail & E-Commerce",
    "Sustainability & Clean Energy",
    "Space Technology",
    "Logistics & Supply Chain",
    "Other / Custom",
]


class AnalyzeRequest(BaseModel):
    field: str = Field(min_length=2, max_length=80)
    idea: str = Field(min_length=20, max_length=6000)


class GenerateRequest(BaseModel):
    field: str = Field(min_length=2, max_length=80)
    context: str = Field(default="", max_length=500)


@app.get("/api/health")
async def health():
    return {"status": "ok", "version": "3.0.0"}


@app.get("/api/fields")
async def fields_list():
    return {"fields": FIELDS}


@app.post("/api/analyze")
async def analyze(payload: AnalyzeRequest):
    try:
        search_data = await gather_for_analysis(payload.field, payload.idea)
        result = await analyze_idea(payload.field, payload.idea, search_data)
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.post("/api/generate")
async def generate(payload: GenerateRequest):
    try:
        search_data = await gather_for_generation(payload.field, payload.context)
        ideas = await generate_ideas(payload.field, payload.context, search_data)
        return {"field": payload.field, "ideas": ideas}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


# ── Serve built React frontend ────────────────────────────────────────────────
DIST_DIR = Path(__file__).parent.parent / "dist"

if DIST_DIR.exists():
    app.mount("/assets", StaticFiles(directory=str(DIST_DIR / "assets")), name="assets")

    @app.get("/{full_path:path}")
    async def serve_frontend(full_path: str):
        fp = DIST_DIR / full_path
        if fp.is_file():
            return FileResponse(str(fp))
        return FileResponse(str(DIST_DIR / "index.html"))
