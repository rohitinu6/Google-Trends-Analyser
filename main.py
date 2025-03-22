import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import time
import requests
from requests.exceptions import RequestException

# Initialize Pytrends connection (without requests_args for stability)
Trending_topics = TrendReq(hl='en-US', tz=360)

# Function to handle rate limits and retries
def safe_request(func, retries=5, delay=10):
    for attempt in range(retries):
        try:
            return func()
        except RequestException as e:
            print(f"Request failed: {e}. Retrying... ({attempt + 1}/{retries})")
            time.sleep(delay)
    raise Exception("Max retries reached. Exiting...")

# Build Payload for "Cloud Computing"
kw_list = ["Cloud Computing"]
Trending_topics.build_payload(kw_list, cat=0, timeframe='today 12-m')
time.sleep(5)

# Interest Over Time
data = safe_request(Trending_topics.interest_over_time)
print("\nInterest Over Time (Top 10):")
print(data.sort_values(by="Cloud Computing", ascending=False).head(10))

# Historical Hourly Interest
Trending_topics.build_payload(kw_list, timeframe='2018-01-01 2018-02-01')
data = safe_request(Trending_topics.interest_over_time)
print("\nHistorical Hourly Interest (Top 10):")
print(data.sort_values(by="Cloud Computing", ascending=False).head(10))

# Interest By Region
data = safe_request(Trending_topics.interest_by_region)
print("\nInterest By Region (Top 10):")
print(data.sort_values(by="Cloud Computing", ascending=False).head(10))

# Visualization
data.reset_index().plot(x='geoName', y='Cloud Computing', figsize=(10, 5), kind="bar")
plt.style.use('fivethirtyeight')
plt.title("Interest in 'Cloud Computing' by Region")
plt.show()

# Top Charts (With Error Handling)
try:
    top_charts = safe_request(lambda: Trending_topics.top_charts(2020, hl='en-US', tz=300, geo='GLOBAL'))
    print("\nTop Charts of 2020:")
    print(top_charts.head(10))
except Exception as e:
    print(f"Error fetching top charts: {e}")

# Related Queries
try:
    related_queries = safe_request(lambda: Trending_topics.related_queries())
    print("\nRelated Queries for 'Cloud Computing':")
    print(related_queries['Cloud Computing']['top'].head(10))
except Exception as e:
    print(f"No related queries found: {e}")

# Keyword Suggestions
try:
    suggestions = Trending_topics.suggestions(keyword='Cloud Computing')
    suggestions_df = pd.DataFrame(suggestions).drop(columns='mid')
    print("\nKeyword Suggestions:")
    print(suggestions_df.head(10))
except Exception as e:
    print(f"Error fetching keyword suggestions: {e}")


