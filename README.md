
# datafun-03-analytics

Project Overview

This project fetches JSON data from the web, processes it using Python collections, and saves the results into multiple file formats. It demonstrates key skills in data analytics, including HTTP requests, file handling, and logging.

Features

Fetches task data from https://jsonplaceholder.typicode.com/todos

Processes data to count completed tasks

Saves processed data in four formats:

CSV (data/tasks.csv)

Excel (data/tasks.xlsx)

JSON (data/tasks.json)

Text (data/tasks.txt)

Uses logging to track execution (project.log)

Requirements

Python 3.8+
External dependencies (installed from requirements.txt):

loguru

pyttsx3

statistics (built-in, no install needed)

requests

openpyxl

Install requirements into your virtual environment:

py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install -r requirements.txt

Files in this Project

batyrov_project3.py – Main script

utils_logger.py – Reusable logging setup

requirements.txt – Dependencies

.gitignore – Git ignore rules

project.log – Log file showing project run history

data/ – Output data folder

tasks.csv

tasks.xlsx

tasks.json

tasks.txt

Output Example

When you run the project, you’ll see logs like this:

2025-09-12 02:14:54 | INFO | utils_logger | Processing data...
2025-09-12 02:14:54 | INFO | utils_logger | Processed data: 90 completed tasks.
2025-09-12 02:14:54 | INFO | utils_logger | Saving CSV file to data/tasks.csv...
2025-09-12 02:14:54 | INFO | utils_logger | Saving Excel file to data/tasks.xlsx...
2025-09-12 02:14:54 | INFO | utils_logger | Saving JSON file to data/tasks.json...
2025-09-12 02:14:54 | INFO | utils_logger | Saving Text file to data/tasks.txt...
