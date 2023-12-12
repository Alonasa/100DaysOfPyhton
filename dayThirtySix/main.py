import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY = "7YMLK7K2SSOFF20T"
NEWS_API_KEY = "f5d2e398a5c64dfba2db6a92db9a3f88"
STOCK_ACTIVE = "IBM"

investment_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_ACTIVE,
    "apikey": API_KEY,
    "datatype": "json"
}

news_parameters = {
    "q": STOCK_ACTIVE,
    "apiKey": NEWS_API_KEY
}

get_investment = requests.get(url=STOCK_ENDPOINT, params=investment_parameters)
investment_data = get_investment.json()['Time Series (Daily)']
data_list = [value for key, value in investment_data.items()]
yesterday_price = float(data_list[0]['4. close'])
day_before_price = float(data_list[1]['4. close'])

price_difference = yesterday_price - day_before_price
get_five_percent = yesterday_price / 100 * 5

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator

if abs(price_difference) > get_five_percent:
    get_news = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_data = get_news.json()['articles']
    for i in range(10):
        news_article = news_data[i]
        print(news_article['title'])
        print(news_article['description'])
        print(news_article['publishedAt'])
        print(f"Learn {news_article['url']}")

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
