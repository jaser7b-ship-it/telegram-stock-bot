import requests
import time
import os

# قراءة معلوماتك من Variables في Railway
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
POLYGON_API_KEY = os.getenv("POLYGON_API_KEY")
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY")

def send_telegram(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        data = {
            "chat_id": CHAT_ID,
            "text": message
        }
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram Error:", e)

def get_polygon_price(symbol):
    try:
        url = f"https://api.polygon.io/v2/aggs/ticker/{symbol}/prev?apiKey={POLYGON_API_KEY}"
        r = requests.get(url)
        data = r.json()

        if "results" in data and len(data["results"]) > 0:
            return data["results"][0]["c"]

    except Exception as e:
        print("Polygon Error:", e)

    return None

def get_finnhub_price(symbol):
    try:
        url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={FINNHUB_API_KEY}"
        r = requests.get(url)
        data = r.json()

        return data.get("c")

    except Exception as e:
        print("Finnhub Error:", e)

    return None

def check_stock(symbol):
    price = get_polygon_price(symbol)

    if price is None:
        price = get_finnhub_price(symbol)

    if price:
        message = f"📈 {symbol}\n💰 Price: {price}"
        send_telegram(message)

# الأسهم التي تريد متابعتها
stocks = [
    "AAPL",
    "TSLA",
    "NVDA"
]

print("Bot Started...")

while True:
    for stock in stocks:
        check_stock(stock)
        time.sleep(5)

    time.sleep(60)
