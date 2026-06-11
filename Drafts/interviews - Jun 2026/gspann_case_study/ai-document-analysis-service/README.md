# AI-Powered Document Analysis Service

## Overview
This service ingests CSV/Excel business documents, cleans and normalizes data,
performs LLM-based analysis using OpenAI, and exposes results via FastAPI.

## Dataset Used
Online Retail II (Kaggle)
https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci

## Setup

1. Clone repo
2. Create virtual environment
3. Install requirements:
   pip install -r requirements.txt
4. Add OpenAI key in .env
5. Run:
   uvicorn app.main:app --reload

## Endpoint

POST /analyze

Upload CSV or Excel file.

Returns structured JSON insights.

## Architecture

FastAPI → pandas cleaning → Aggregation → OpenAI analysis → QA validation → JSON response

## Production Enhancements

- Schema enforcement
- Guardrails
- Logging
- Token optimization
- Structured outputs

## How to Run

```bash
cd ai-document-analysis-service
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000/docs
