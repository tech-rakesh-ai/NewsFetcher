# celery_worker.py
from celery import Celery
import httpx
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models import NewsArticle, Base

celery = Celery(
    'celery_worker',
    broker='pyamqp://guest:guest@localhost//',
    backend='rpc://'
)


@celery.task
def fetch_and_store_news():
    NEWS_API_KEY = "4f77e31eb1174a109a7d5dbc753ecd9b"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

    with httpx.Client() as client:
        response = client.get(url)
        news_data = response.json()

        # Assuming you have a MySQL database configured, replace the following with your database setup logic
        engine = create_engine("mysql+mysqlconnector://rakesh:password@localhost/news_db")
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        for article in news_data.get('articles', []):
            # source = Source(name=source_data.get('name'))
            source_data = article.get('source', {})
            news_article = NewsArticle(
                source_id=source_data.get('id'),
                source_name=source_data.get('name'),
                author=article.get('author'),
                title=article.get('title'),
                description=article.get('description'),
                url=article.get('url'),
                url_to_image=article.get('urlToImage'),
                published_at=datetime.strptime(article.get('publishedAt'), "%Y-%m-%dT%H:%M:%SZ"),
                content=article.get('content')
            )
            session.add(news_article)

        session.commit()
        session.close()
