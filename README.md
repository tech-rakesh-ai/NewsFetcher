# NewsFetcher

## Project Description

NewsFetcher is a FastAPI application that fetches top headlines from the NewsAPI and stores them in a MySQL database
using Celery for asynchronous task scheduling.

## Basic Flow

1. **FastAPI Server**:
    - Provides an endpoint to fetch top news headlines.
    - Uses an async HTTP client to query the NewsAPI.
    - Stores fetched news articles in a MySQL database.

2. **Celery Worker**:
    - Asynchronously fetches and stores news articles at regular intervals.
    - Uses SQLAlchemy for ORM operations to interact with the MySQL database.

## Getting Started

### Prerequisites

- Install Python (version 3.8 or higher).
- Install MySQL and set up a database.

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/tech-rakesh-ai/NewsFetcher.git
   cd NewsFetcher
   ```

2. Create a virtual environment:

   ```shell
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Set up MySQL database:
    - Create a MySQL database (`news_db` for example).
    - Update `celery_worker.py` with your database configuration.

5. Run the FastAPI server:

   ```shell
   uvicorn main:app --reload
   ```

6. Run the Celery worker:

   ```shell
   celery -A celery_worker worker --loglevel=info
   ```

7. Start the scheduler (to fetch news periodically):

   ```shell
   python scheduler.py
   ```

### Usage

- Access the FastAPI server at `http://localhost:8000/` to fetch news headlines.
- The Celery worker will automatically fetch news articles and store them in the MySQL database.

### API Endpoints

- **Fetch News**: `/fetch-news` - Returns top headlines from the NewsAPI.

### Example Usage

```bash
curl http://localhost:8000/fetch-news
```

## Contributors

- Rakesh Kumar (@tech-rakesh-kr)