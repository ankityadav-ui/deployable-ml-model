#!/bin/bash

echo "🚀 Starting FastAPI Backend..."

uvicorn app:app --host 0.0.0.0 --port $PORT