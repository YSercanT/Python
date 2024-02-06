import requests
from twilio.rest import Client
VIRTUAL_TWILIO_NUMBER = "your virtual twilio number"
VERIFIED_NUMBER = "your own phone number verified with Twilio"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "YOUR OWN API KEY FROM ALPHAVANTAGE"
NEWS_API_KEY = "YOUR OWN API KEY FROM NEWSAPI"
TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
stock_params = {"function": "TIME_SERIES_DAILY",
                "symbol": STOCK_NAME,
                "apikey": STOCK_API_KEY}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
data=stock_response.json()["Time Series (Daily)"]
data_list=[value for (key,value) in data.items() ]
#print(data_list)
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
#print(yesterday_closing_price)



day_before_yesterday_data=data_list[1]
day_before_closing_price=day_before_yesterday_data["4. close"]
#print(day_before_closing_price)


diff=abs(float(yesterday_closing_price)-float(day_before_closing_price))
#print(diff)
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent=round((diff/float(yesterday_closing_price))*100)
#print(diff_percent)
if diff_percent>=3:
    new_params={"apikey":NEWS_API_KEY,
                "qInTitle":COMPANY_NAME,
                }
    new_response=requests.get(NEWS_ENDPOINT,params=new_params)
    articles=new_response.json()["articles"]
    three_articles=articles[:3]

    #print(three_articles)

    
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


    for article in formatted_articles:
            message = client.messages.create(
    from_=VIRTUAL_TWILIO_NUMBER,
    body=article,
    to=VERIFIED_NUMBER
    )
