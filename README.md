
# Text Summarization APP

A small Streamlit web app that generates concise summaries from input text using Sumy summarizers (LSA, Luhn, LexRank, TextRank).

## Features

- Choose summarization algorithm: Lsa, Luhn, LexRank, TextRank
- Select number of sentences for the summary (1–10)
- View summary in the app and download as a text file

## Requirements
- Python 3.8+
- Windows (tested)
- Packages:
  - streamlit
  - sumy

## Install
Open PowerShell in the project folder:
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -U pip
pip install streamlit sumy
```

## Run
```powershell
streamlit run text_summarization.py
```
Open the local URL shown in the terminal (usually http://localhost:8501).

## Usage
1. Paste or type the source text into the text area.
2. Select a summarizer model.
3. Set the desired number of summary sentences.
4. Click "Summarize" to generate and view the summary.
5. Download the summary using the "Download summary" button if available.

## Troubleshooting
- Import errors: ensure packages are installed in the active virtual environment.
- Empty summary: try increasing input length or reducing requested sentences.
- App not starting: verify the virtual environment is activated and run the streamlit command from the project folder.

## Contribution
Contributions and improvements are welcome — submit issues or pull requests.

## License
Add a license of your choice (e.g., MIT) if you plan to publish this project.
```# filepath: c:\projects\NLP\README.md
...existing code...

# Text Summarization APP

A small Streamlit web app that generates concise summaries from input text using Sumy summarizers (LSA, Luhn, LexRank, TextRank).

## Features
- Choose summarization algorithm: Lsa, Luhn, LexRank, TextRank
- Select number of sentences for the summary (1–10)
- View summary in the app and download as a text file

## Requirements
- Python 3.8+
- Windows (tested)
- Packages:
  - streamlit
  - sumy

## Install
Open PowerShell in the project folder:
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -U pip
pip install streamlit sumy
```

## Run
```powershell
streamlit run text_summarization.py
```
Open the local
