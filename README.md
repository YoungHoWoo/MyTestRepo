# MyTestRepo

This repository contains a simple script to generate a single HTML page comparing project data from Google Sheets.

## Setup

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Edit `generate_page.py` if you need to change the `SPREADSHEET_ID` or the
column names listed in `PROJECT_COLUMNS`.

Run the script:

```bash
python generate_page.py
```

It will create an `output.html` file showing a line graph of the selected projects in a modern, simple page.
