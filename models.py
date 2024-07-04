from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# class Source(Base):
#     __tablename__ = 'sources'
#     id = Column(String(255), primary_key=True, nullable=False)
#     name = Column(String(length=255), nullable=False)


class NewsArticle(Base):
    __tablename__ = 'news_articles'

    id = Column(Integer, primary_key=True)
    source_id = Column(String(length=255), nullable=True)
    source_name = Column(String(length=255), nullable=True)
    # source_id = Column(Integer, ForeignKey('sources.id'))
    author = Column(String(length=255))
    title = Column(String(length=255))
    description = Column(Text)
    url = Column(String(length=255))
    url_to_image = Column(String(length=255))
    published_at = Column(DateTime)
    content = Column(Text)
