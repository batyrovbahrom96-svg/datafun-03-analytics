from utils_logger import logger

def main():
    logger.info("Starting Project 3...")

    # TODO: fetch data, save CSV, Excel, JSON, and Text
    # You will add more functions here.

    logger.info("Finished Project 3.")

if __name__ == "__main__":
    main()

"""
Project 3 - Python Data Project
Author: Bakhrom Botirov
"""

# =========================================================
# Imports
# =========================================================
import os
import requests
import csv
import json
from openpyxl import Workbook
from utils_logger import logger  # reuse logger

# =========================================================
# Functions
# =========================================================

def fetch_data(url: str) -> list[dict]:
    """Fetch JSON data from a URL and return as Python list of dicts."""
    logger.info(f"Fetching data from {url}...")
    response = requests.get(url)
    data = response.json()
    logger.info(f"Fetched {len(data)} records.")
    return data


def process_data(data: list[dict]) -> dict:
    """Process the data: count completed tasks, extract titles."""
    logger.info("Processing data...")
    completed_tasks = [task for task in data if task["completed"]]
    titles = [task["title"] for task in data]

    results = {
        "total_tasks": len(data),
        "completed_tasks": len(completed_tasks),
        "incomplete_tasks": len(data) - len(completed_tasks),
        "titles": titles[:10]  # only first 10 titles for preview
    }
    logger.info(f"Processed data: {results['completed_tasks']} completed tasks.")
    return results


def save_csv(data: list[dict], filepath: str) -> None:
    """Save list of dicts to CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    logger.info(f"Saving CSV file to {filepath}...")
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["userId", "id", "title", "completed"])
        writer.writeheader()
        writer.writerows(data)


def save_excel(data: list[dict], filepath: str) -> None:
    """Save list of dicts to Excel file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    logger.info(f"Saving Excel file to {filepath}...")
    wb = Workbook()
    ws = wb.active
    ws.append(["userId", "id", "title", "completed"])  # header row
    for task in data:
        ws.append([task["userId"], task["id"], task["title"], task["completed"]])
    wb.save(filepath)


def save_json(data: list[dict], filepath: str) -> None:
    """Save data to JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    logger.info(f"Saving JSON file to {filepath}...")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def save_text(titles: list[str], filepath: str) -> None:
    """Save list of task titles to a plain text file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    logger.info(f"Saving Text file to {filepath}...")
    with open(filepath, "w", encoding="utf-8") as f:
        for title in titles:
            f.write(title + "\n")

# =========================================================
# Main
# =========================================================

def main() -> None:
    """Main function to run the project."""
    logger.info("Starting Project 3...")

    # Step 1: Fetch data
    url = "https://jsonplaceholder.typicode.com/todos"
    data = fetch_data(url)

    # Step 2: Process data
    results = process_data(data)

    # Step 3: Save to files
    save_csv(data, "data/tasks.csv")
    save_excel(data, "data/tasks.xlsx")
    save_json(data, "data/tasks.json")
    save_text(results["titles"], "data/tasks.txt")

    logger.info("Finished Project 3.")

# =========================================================
# Run
# =========================================================

if __name__ == "__main__":
    main()