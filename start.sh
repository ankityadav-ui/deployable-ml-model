#!/bin/bash

# Terminate all background processes on exit
trap "exit" INT TERM
trap "kill 0" EXIT

# Start FastAPI (Backend) in the background
echo "🚀 Starting FastAPI Backend on port 8000..."
uvicorn app:app --host 0.0.0.0 --port 8000 &

# Wait a few seconds for backend to initialize
sleep 2

# Start Streamlit (Frontend) in the foreground
echo "🎨 Starting Streamlit Frontend on port 8501..."
streamlit run frontend.py --server.port 8501 --server.address 0.0.0.0
