from fastapi import FastAPI, UploadFile, File
import shutil
from resume_parser import extract_text_from_pdf
from ai_analyzer import analyze_resume
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Resume Analyzer API running"}

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_location = "resume.pdf"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text_from_pdf(file_location)

    analysis = analyze_resume(resume_text[:3000])  # Limit to first 3000 characters for analysis

    return {
        "message": "Resume analyzed successfully",
        "analysis": analysis
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)