# scheduler.py
import schedule
import time
from celery_worker import fetch_and_store_news


def job():
    fetch_and_store_news.apply_async()


print("Scheduler started.")

# Run the job every minute
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

print("Scheduler stopped.")
