from stock_fetcher import get_stock_price
from notion_updater import get_stocks, update_stock_price


def main():
    print("Fetching stocks from Notion...")
    stocks = get_stocks()

    for stock in stocks:
        ticker = stock["ticker"]
        page_id = stock["page_id"]

        print(f"Fetching price for {ticker}...")
        price = get_stock_price(ticker)

        print(f"Updating {ticker} → €{price}")
        update_stock_price(page_id, price)

    print("Done! All prices updated.")


if __name__ == "__main__":
    main()