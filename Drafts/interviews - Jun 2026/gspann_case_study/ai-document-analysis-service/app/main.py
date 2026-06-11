from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd

from app.schemas import APIResponse
from app.services.data_cleaner import clean_data, generate_summary
from app.services.llm_service import analyze_with_llm
from app.services.qa_validator import validate_output
from app.utils.logger import logger

app = FastAPI(title="AI Document Analysis Service")


@app.post("/analyze", response_model=APIResponse)
async def analyze(file: UploadFile = File(...)):

    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Unsupported file format")

    try:
        logger.info(f"Received file: {file.filename}")

        if file.filename.endswith(".csv"):
            df = pd.read_csv(file.file)
        else:
            df = pd.read_excel(file.file)

        cleaned_df = clean_data(df)
        summary = generate_summary(cleaned_df)

        llm_result = analyze_with_llm(summary)
        validated = validate_output(llm_result, summary["total_revenue"])

        return {
            "status": "success",
            "data": validated
        }

    except Exception as e:
        logger.error(str(e))
        raise HTTPException(status_code=500, detail=str(e))
