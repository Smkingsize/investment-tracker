import os
import requests
from dotenv import load_dotenv

load_dotenv()

NOTION_API_KEY = os.getenv("NOTION_API_KEY")
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

HEADERS = {
    "Authorization": f"Bearer {NOTION_API_KEY}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


def get_stocks():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"
    response = requests.post(url, headers=HEADERS)
    data = response.json()

    stocks = []
    for page in data["results"]:
        ticker = page["properties"]["Ticker"]["rich_text"][0]["text"]["content"]
        page_id = page["id"]
        stocks.append({"ticker": ticker, "page_id": page_id})

    return stocks


def update_stock_price(page_id: str, price: float):
    url = f"https://api.notion.com/v1/pages/{page_id}"
    payload = {
        "properties": {
            "Current Price": {
                "number": price
            }
        }
    }
    response = requests.patch(url, headers=HEADERS, json=payload)
    return response.status_code