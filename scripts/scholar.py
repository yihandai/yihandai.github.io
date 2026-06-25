import json
import os
from scholarly import scholarly, ProxyGenerator

SCHOLAR_ID = "evwzw60AAAAJ"
OUTPUT_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "scholar_stats.json",
)


def main():
    # Set up proxy to avoid being blocked by Google Scholar
    pg = ProxyGenerator()
    success = pg.FreeProxies()
    if success:
        scholarly.use_proxy(pg)
        print("Proxy enabled")
    else:
        # Fallback: try without proxy
        print("Warning: could not set up proxy, trying direct connection")

    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author, sections=["indices"])

    stats = {
        "citedby": author.get("citedby", 0),
        "hindex": author.get("hindex", 0),
        "i10index": author.get("i10index", 0),
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(stats, f, indent=2)

    print(f"Updated scholar stats: {stats}")


if __name__ == "__main__":
    main()
