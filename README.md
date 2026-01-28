# Automation Projects Collection

This repository contains a collection of Python automation scripts and projects designed for various tasks ranging from web scraping to natural language processing. Below is a summary of each project included in this collection.

## 1. HackerNews Emailer
*   **Directory:** `HackerNews_Emailer`
*   **Main Script:** `hackernews_emailer.py`
*   **Description:** Scrapes the top stories from Hacker News and sends them as an email summary. It uses `requests` and `BeautifulSoup` for scraping and `smtplib` for sending emails via Gmail.

## 2. TED Talk Downloader
*   **Directory:** `TED_Talk_Downloader`
*   **Main Script:** `ted_downloader.py`
*   **Description:** automating the process of downloading TED Talk videos. It fetches the video URL from a given TED Talk page and downloads the video file (MP4).

## 3. UN HDI Table Extractor
*   **Directory:** `UN_HDI_Table_Extractor`
*   **Main Script:** `Extracting Table from PDF UN HDI Report.ipynb`
*   **Description:** Extracts tabular data from UN Human Development Index (HDI) PDF reports. It likely uses libraries like `camelot` or `pdfplumber` (based on typical usage) to convert PDF tables into structured data (CSV/Excel).

## 4. Resume Parser
*   **Directory:** `Resume_Parser`
*   **Main Script:** `resume_parser.py`
*   **Description:** A tool to parse information from resumes (PDFs). It uses `spacy` for Named Entity Recognition (NER) to extract details like Names, Emails, Phone Numbers, and Skills, and uses `pdfminer` (via `pdf2txt`) to convert PDFs to text. Results are exported to CSV.

## 5. Image Format Converter
*   **Directory:** `Image_Format_Converter`
*   **Main Script:** `png_to_jpg_converter.py`
*   **Description:** A utility script using the `Pillow` (PIL) library to batch convert all `.png` images in a directory to `.jpg` format.

## 6. Article Summarizer
*   **Directory:** `Article_Summarizer`
*   **Main Script:** `article_summarizer.ipynb` / `summarizer.py`
*   **Description:** Summarizes news articles using Natural Language Processing (NLP). It utilizes the `sumy` library (LexRank algorithm) for summarization and `rake-nltk` for keyword extraction.

---

## How to Run
To run any of the python scripts, navigate to the specific directory and run:
```bash
python <script_name>.py
```
For Jupyter Notebooks (`.ipynb`), start Jupyter Notebook or Jupyter Lab:
```bash
jupyter notebook
```

## Requirements
Each project may have its own dependencies. Common libraries used across these projects include:
*   `requests`
*   `beautifulsoup4`
*   `spacy` (and `en_core_web_sm` model)
*   `pdfminer.six`
*   `Pillow`
*   `sumy`
*   `rake-nltk`
*   `pandas`

Ensure these are installed via `pip install <package_name>`.
