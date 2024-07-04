from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


NEWS_API_KEY = "4f77e31eb1174a109a7d5dbc753ecd9b"


@app.get("/fetch-news")
async def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        news_data = response.json()
        print(news_data)
    return news_data
