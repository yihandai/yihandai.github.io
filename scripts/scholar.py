import json
import os
import re
import requests
from bs4 import BeautifulSoup

SCHOLAR_ID = "evwzw60AAAAJ"
SCHOLAR_URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"
OUTPUT_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "scholar_stats.json",
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "en-US,en;q=0.9",
}


def main():
    resp = requests.get(SCHOLAR_URL, headers=HEADERS, timeout=15)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    stats = {"citedby": 0, "hindex": 0, "i10index": 0}

    # Google Scholar stats are in a table with class "gsc_rsb_std"
    # The rows are: Citations, h-index, i10-index
    for row in soup.select("table#gsc_rsb_st tbody tr"):
        cells = row.find_all("td")
        if len(cells) < 2:
            continue
        label = cells[0].get_text(strip=True).lower()
        value = cells[1].get_text(strip=True)
        if "citations" in label or "citation" in label:
            stats["citedby"] = int(value)
        elif label.startswith("h-index"):
            stats["hindex"] = int(value)
        elif label.startswith("i10-index"):
            stats["i10index"] = int(value)

    with open(OUTPUT_FILE, "w") as f:
        json.dump(stats, f, indent=2)

    print(f"Updated scholar stats: {stats}")


if __name__ == "__main__":
    main()
