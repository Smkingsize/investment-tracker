# 📈 Investment Tracker

Automatically fetches stock prices and updates a Notion investment table using Python and GitHub Actions.

## How It Works

```
yfinance (fetches prices)
        ↓
   Python Script
        ↓
  Notion API (updates table)
        ↑
GitHub Actions (runs every weekday at 8AM UTC)
```

## Project Structure

```
investment-tracker/
│
├── .github/
│   └── workflows/
│       └── update_tracker.yml   # GitHub Actions schedule
│
├── src/
│   ├── main.py                  # Entry point
│   ├── notion_updater.py        # Notion API logic
│   └── stock_fetcher.py         # yfinance logic
│
├── .env                         # Local secrets (never committed)
├── .gitignore
├── requirements.txt
└── README.md
```



## Automation
The script runs automatically every weekday at 8AM UTC via GitHub Actions.
You can also trigger it manually from the Actions tab on GitHub.

## Built With
- [yfinance](https://github.com/ranaroussi/yfinance) — stock price fetching
- [Notion API](https://developers.notion.com/) — database updates
- [GitHub Actions](https://docs.github.com/en/actions) — automation