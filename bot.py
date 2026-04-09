")
CHAT_ID = os.getenv("CHAT_ID")

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

# رسالة بداية
send_message("✅ Bot restarted successfully")

while True:
    try:
        send_message("📡 Bot is running...")
        time.sleep(60)

    except Exception as e:
        send_message(f"Error: {e}")
        time.sleep(60)