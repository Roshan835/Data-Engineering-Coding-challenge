from datetime import datetime # Import datetime module for date and time handling
from fastapi import APIRouter, Query, HTTPException, Depends # Import necessary FastAPI components
from fastapi.security.api_key import APIKey
from src.logic import analyze_sentiment # Import sentiment analysis logic
from src.logic import generate_api_url # Import function for generating API URLs
from src.logic import generate_subfeddit_url # Import function for generating subfeddit URLs
from src.logic import get_id_by_username # Import function for getting subfeddit ID by username
from typing import List # Import List type from typing module
import requests # Import requests library for making HTTP requests
from src import auth


# Initialize FastAPI router instance
router = APIRouter()

# Endpoint to perform all the mentioned tasks
@router.get("/sentiment-analysis/", response_model=List[dict])
async def analyze_comments_sentiment(
    subfeddit_name: str = Query(..., title="Subfeddit_name", description="name of subfeddit"),
    limit: int = Query(25, title="Limit", description="Number of comments to retrieve"),
    skip: int = Query(0, title="Skip", description="Number of comments to skip"),
    start_date: datetime = Query(None, title="Start Date", description="Start date for time range filter"),
    end_date: datetime = Query(None, title="End Date", description="End date for time range filter"),
    sort_by_polarity: bool = Query(False, title="Sort by Polarity", description="Sort results by comments polarity score"),
    api_key: str = Depends(auth.get_api_key)
    ):
  
    #Fetches subfeddits from feddit_api to this webapi
    subfeddit_url = generate_subfeddit_url()
    response1 = requests.get(subfeddit_url)
    subfeddit_data = response1.json()
    subfeddit_id = get_id_by_username(subfeddit_data, subfeddit_name)

    #Fetches comments from Feddit_api to this web api
    Feddit_url = generate_api_url(subfeddit_id, skip, limit)
    response = requests.get(Feddit_url) 
    feddit_data = response.json()

    #Filters comments based on timestamp
    filtered_comments = [
        comment for comment in feddit_data.get("comments", [])
        if (start_date is None or comment.get("timestamp") >= start_date) and
           (end_date is None or comment.get("timestamp") <= end_date)
    ]

    sentiment_analysis_list = []  # Collect sentiment analysis results for all comments

    for comment in filtered_comments:
        id = comment.get("id", "")
        text = comment.get("text", "")
        sentiment_analysis = analyze_sentiment(text, id)
        sentiment_analysis_list.append(sentiment_analysis)  # Collect each sentiment analysis result

    # Sorts comments based on their polarity score
    if sort_by_polarity:
        sentiment_analysis_list = sorted(sentiment_analysis_list, key=lambda x: x['polarity_score'], reverse=True)

    return sentiment_analysis_list
