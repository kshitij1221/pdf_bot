🧠 PDF Extraction appliction

A lightweight Streamlit app built with pdf4llm that converts PDFs into structured, markdown-style text — perfect for developers, data analysts, and AI workflows.

🚀 Overview

This project demonstrates practical AI-developer skills in:

Natural-language-ready PDF parsing

Data extraction automation

Python + Streamlit UI design

Integration with AI preprocessing pipelines (via pdf4llm)

You upload a PDF (e.g., reports, resumes, contracts), click Convert, and instantly get a clean .txt file for analysis or feeding into LLMs.

⚙️ Tech Stack
Component	Purpose
🐍 Python 3.10+	Core language
🎈 Streamlit	Interactive UI for easy uploads and downloads
📘 pdf4llm	Extracts readable, markdown-style text optimized for AI models
🧱 pathlib	File-safe path handling
💡 Exception-safe processing	Graceful error handling and progress feedback
🧩 Features

✅ 1-Click PDF Conversion
Upload any .pdf → convert to .txt instantly

✅ AI-Friendly Markdown Output
Text formatted for easy ingestion by LLMs and NLP pipelines

✅ Download + Preview
Get a .txt file and preview the extracted content inside the app

✅ Lightweight & Fast
No heavy OCR or external APIs — runs locally in seconds

✅ Error-Resilient UX
Includes success messages, spinners, and clean UI interactions

🖥️ Demo (How It Works)
Step 1 — Upload a File

Upload any PDF report or document:

📄 my_report.pdf

Step 2 — Click Convert

The app extracts and cleans the content:

## Executive Summary
This report explores data-driven insights into performance...

Step 3 — Download or Preview

Download output.txt or view the converted text right inside the Streamlit app.

🧰 Installation
# Clone this repo
git clone https://github.com/<yourusername>/pdf-extractor-ai.git
cd pdf-extractor-ai

# Create virtual environment
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

# Install dependencies
pip install streamlit pdf4llm

▶️ Run the App
streamlit run app.py


Then open the app in your browser — usually at
👉 http://localhost:8501

📁 Output

Each conversion creates a output.txt file, containing clean text extracted from your uploaded PDF.

Example output:

# Behavioral Competency Analysis Report
- Competency: Hunger (92%)
- Trait: Enthusiastic (10.0)
- Trait: Takes Initiative (9.9)


This project highlights:

Skill Area	Demonstration
AI/LLM Integration	Used pdf4llm to prepare text for downstream language models
Data Pre-Processing	Extracts and structures unstructured PDF data for AI consumption
Python Engineering	Clean, modular, production-ready code with robust error handling
UI/UX for AI Tools	Built an interactive app with Streamlit for non-technical users
End-to-End Pipeline	Handles file input → processing → output download seamlessly
🌍 Use Cases

🧠 Feeding business reports into LLMs for summarization

📄 Preparing HR assessments for NLP models

📚 Academic paper extraction for research assistants

🏢 Enterprise document analysis pipelines

📜 Example Code Snippet
import streamlit as st
import pdf4llm
import pathlib

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
if uploaded_file and st.button("Convert"):
    temp_path = f"temp_{uploaded_file.name}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    text = pdf4llm.to_markdown(temp_path)
    pathlib.Path("output.txt").write_bytes(text.encode("utf-8"))
    st.download_button("Download Output", data=text, file_name="output.txt")

🧑‍💻 Author

Kshitij Singh
AI Developer & Python Engineer
🔗 LinkedIn
 · 💻 GitHub

Passionate about building AI-driven tools that make complex data simple and actionable.

🪪 License

MIT License — free for personal and commercial use.

