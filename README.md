# Automation Projects Collection

This repository contains a collection of Python automation scripts and projects designed for various tasks ranging from web scraping to natural language processing. These projects are curated to help with **Technical Interview Preparation** by covering key automation strategies.

## 1. HackerNews Emailer
*   **Directory:** `1.HackerNews_Emailer`
*   **Main Script:** `hackernews_emailer.py`
*   **Strategy:** Web Scraping (BeautifulSoup) + SMTP (Email).
*   **Description:** Scrapes the top stories from Hacker News and sends them as an email summary.

## 2. TED Talk Downloader
*   **Directory:** `2.TED_Talk_Downloader`
*   **Main Script:** `ted_downloader.py`
*   **Strategy:** HTTP Requests + JSON Parsing + Stream Downloading.
*   **Description:** Automates downloading videos from TED.com by reverse-engineering the page metadata (JSON).

## 3. UN HDI Table Extractor
*   **Directory:** `3.UN_HDI_Table_Extractor`
*   **Main Script:** `extractor.py` / `Extracting Table from PDF UN HDI Report.ipynb`
*   **Strategy:** PDF Parsing.
*   **Description:** Extracts tabular data from complex PDF reports into usable CSV/Excel formats.

## 4. Resume Parser
*   **Directory:** `4.Resume_Parser`
*   **Main Script:** `resume_parser.py`
*   **Strategy:** NLP (Spacy) + Pattern Matching (Regex).
*   **Description:** Parses resumes to extract structured entities like Names, Phone Numbers, and Skills.

## 5. Image Format Converter
*   **Directory:** `5.Image_Format_Converter`
*   **Main Script:** `png_to_jpg_converter.py`
*   **Strategy:** Batch Processing (Pillow Library).
*   **Description:** A utility to batch convert image formats (PNG to JPG) for an entire directory.

## 6. Article Summarizer
*   **Directory:** `6.Article_Summarizer`
*   **Main Script:** `summarizer.py`
*   **Strategy:** Text Summarization (LexRank/NLP).
*   **Description:** Uses Natural Language Processing to generate concise summaries of long news articles.

---
### **Part 2: Interview Strategy Focus (Concepts)**

## 7. Crypto Price Alert
*   **Directory:** `7.Crypto_Price_Alert`
*   **Main Script:** `crypto_alert.py`
*   **Strategy:** **API Polling & System Notifications**.
*   **Concept:** Demonstrates how to fetch data from a REST API (`requests`), run an infinite loop with delays (`time.sleep`), and interact with the OS (`plyer`). A common interview task is "Build a service that checks status X and simple alerts".

## 8. Automated Excel Report
*   **Directory:** `8.Automated_Excel_Report`
*   **Main Script:** `report_generator.py`
*   **Strategy:** **ETL (pandas)**.
*   **Concept:** Business automation: taking raw CSV dumps, processing them (Pivot Tables), and creating formatted Excel files.

## 9. Selenium Web Login
*   **Directory:** `9.Selenium_Web_Login`
*   **Main Script:** `login_bot.py`
*   **Strategy:** **Browser Automation (Selenium)**.
*   **Concept:** Automating interactions with websites that require login, JavaScript, or cannot be scraped with simple requests.

## 10. Desktop Cleaner
*   **Directory:** `10.Desktop_Cleaner`
*   **Main Script:** `file_organizer.py`
*   **Strategy:** **File System (OS/Shutil)**.
*   **Concept:** Organizing files based on extensions. Tests logical flow and file system manipulation.

## 11. PDF Manager
*   **Directory:** `11.PDF_Manager`
*   **Main Script:** `pdf_tools.py`
*   **Strategy:** **Binary File Manipulation (PyPDF2)**.
*   **Concept:** Merging, splitting, and password-protecting PDFs.

## 12. CSV to Database (ETL)
*   **Directory:** `12.CSV_to_Database`
*   **Main Script:** `csv_to_sql.py`
*   **Strategy:** **Database Interactions (SQL)**.
*   **Concept:** Reads raw CSV files and inserts them into a local SQLite database.

## 13. System Resource Monitor
*   **Directory:** `13.System_Monitor`
*   **Main Script:** `resource_logger.py`
*   **Strategy:** **SysAdmin/DevOps (psutil)**.
*   **Concept:** Logs CPU, RAM, and Disk usage to a file for server health monitoring.

## 14. CLI Tool Template
*   **Directory:** `14.CLI_Tool_Template`
*   **Main Script:** `cli_tool.py`
*   **Strategy:** **CLI Arguments (argparse)**.
*   **Concept:** Building tools that accept command-line flags (e.g., `--verbose`, `--input`).

---
### **Part 3: Real World Business Scenarios**

These projects simulate end-to-end tasks often assigned in corporate environments.

## 15. Bulk Invoice Generator
*   **Directory:** `15.Bulk_Invoice_Generator`
*   **Main Script:** `invoice_gen.py`
*   **Strategy:** **Finance Automation**.
*   **Concept:** Generates massive amounts of PDF invoices from CSV data using `fpdf`.

## 16. Broken Link Checker (Uptime Monitor)
*   **Directory:** `16.Broken_Link_Checker`
*   **Main Script:** `link_monitor.py`
*   **Strategy:** **QA / Site Reliability**.
*   **Concept:** Iterates through a list of URLs to detect 404/500 errors and trigger alerts.

## 17. Automated Backup Manager
*   **Directory:** `17.Automated_Backup_Script`
*   **Main Script:** `backup_manager.py`
*   **Strategy:** **IT Operations**.
*   **Concept:** Automates creating zip archives of folders and deletes backups that are older than X days.

---
### **Part 4: Advanced Interview Topics**

These projects demonstrate advanced knowledge and edge-case handling.

## 18. Log File Analyzer
*   **Directory:** `18.Log_File_Analyzer`
*   **Main Script:** `log_parser.py`
*   **Strategy:** **Regular Expressions (Regex)**.
*   **Concept:** Processing unstructured text files (Server Logs) to extract specific patterns like IP addresses and Status Codes. Regex is a critical interview skill.

## 19. Async Web Scraper
*   **Directory:** `19.Async_Web_Scraper`
*   **Main Script:** `async_scraper.py`
*   **Strategy:** **Concurrency (AsyncIO/AIOHTTP)**.
*   **Concept:** Speed logic. Using asynchronous programming to fetch 50+ pages concurrently, which is 10x faster than standard sequential loops.

## 20. GUI Bot (PyAutoGUI)
*   **Directory:** `20.GUI_Bot_PyAutoGUI`
*   **Main Script:** `gui_bot.py`
*   **Strategy:** **Desktop GUI Automation**.
*   **Concept:** Controlling the mouse and keyboard directly to automate applications that have no API (e.g., Notepad, Calculator, Legacy Software).

---

## How to Run
Navigate to the project folder and run the python script:
```bash
python <script_name>.py
```

## Setup Requirements
install all libraries:
```bash
pip install requests beautifulsoup4 spacy pdfminer.six pillow sumy rake-nltk pandas openpyxl selenium webdriver-manager plyer PyPDF2 reportlab psutil fpdf aiohttp pyautogui
```
