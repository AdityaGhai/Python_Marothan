import requests
from datetime import datetime
from twilio.rest import Client

TODAY_DATE = datetime.now().date()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# alphavantage api key and end point
API_KEY_STOCK = "your api"
END_POINT_STOCK = "https://www.alphavantage.co/query"

# news api key and end point
API_KEY_NEWS = "your api"
END_POINT_NEWS = "https://newsapi.org/v2/everything"

# twilio api key and end point
API_KEY_SMS = "your api"
END_POINT_SMS = "https://api.openweathermap.org/data/2.5/onecall"

# twilio sid and auth token
SMS_ACCOUNT_SID = "AC4737ee2d2a777daaa2d34270e14d1658"
SMS_AUTH_TOKEN = "your token"

PARAMETERS_STOCK = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_STOCK
}

PARAMETERS_NEWS = {
    "q": "Tesla",
    "from": TODAY_DATE,
    "sortBy": "popularity",
    "apikey": API_KEY_NEWS
}


# Using https://www.alphavantage.co for stock updates
# Checking if STOCK price increase/decreases by 5% between yesterday and the day before yesterday.

api_stock = requests.get(url=END_POINT_STOCK, params=PARAMETERS_STOCK)
api_stock.raise_for_status()

data = api_stock.json()["Time Series (Daily)"]
stock_data = [value for (key, value) in data.items()]
yesterday_close = float(stock_data[0]["4. close"])

day_before_yesterday_close = float(stock_data[1]["4. close"])

Get_News = False

stock_change = ((day_before_yesterday_close-yesterday_close)/day_before_yesterday_close) * 100

if abs(stock_change) >= 5:
    Get_News = True



# Using https://newsapi.org for news update
# getting first 3 news article of given stock.

if Get_News:
    api_news = requests.get(END_POINT_NEWS, params=PARAMETERS_NEWS)
    data_news = api_news.json()["articles"][:3]
    stock_articles = [f"Headline: {news['title']}. \nBrief: {news['description']}" for news in data_news]

    # Using https://www.twilio.com for sms notification
    # Sending a message with the percentage change and each article's title and description to your phone number.

    if stock_change < 0:
        stocks = f"🔻{int(stock_change)}%"
    else:
        stocks = f"🔺{int(stock_change)}%"
    print(stocks)

    client = Client(SMS_ACCOUNT_SID, SMS_AUTH_TOKEN)


    for article in stock_articles:

        message = client.messages.create(
            body=f"{STOCK}: {stocks}\n{article}",
            from_="+18455761219",
            to='your phone no.'
        )



