from textblob import TextBlob # Import TextBlob for sentiment analysis

def get_id_by_username(data, input_title):
    """
    Get subfeddit ID based on the provided username.

    Args:
        data (dict): The data containing subfeddit information.
        input_title (str): The username to search for.

    Returns:
        int or None: The ID of the subfeddit if found, otherwise None.
    """
    for subfeddit in data["subfeddits"]:
        if subfeddit["title"] == input_title:
            return subfeddit["id"]
    return None

def generate_subfeddit_url():
    """
    Generate the URL for fetching subfeddits.

    Returns:
        str: The generated subfeddit URL.
    """
    return "http://localhost:8080/api/v1/subfeddits/?skip=0&limit=10"

def generate_api_url(subfeddit_id, skip, limit):
    """
    Generate the URL for fetching comments based on subfeddit ID, skip, and limit.

    Args:
        subfeddit_id (int): The ID of the subfeddit.
        skip (int): The number of comments to skip.
        limit (int): The number of comments to retrieve.

    Returns:
        str: The generated API URL for comments.
    """
    base_url = "http://localhost:8080/api/v1/comments/"
    api_params = f"?subfeddit_id={subfeddit_id}&skip={skip}&limit={limit}"
    api_url = base_url + api_params
    return api_url

def analyze_sentiment(text: str, id: int) -> dict:
    """
    Analyze sentiment of the given text and return results.

    Args:
        text (str): The text to analyze.
        id (int): The identifier associated with the text.

    Returns:
        dict: Sentiment analysis results including polarity, classification, ID, and text.
    """
    if not text:
        return {
            'polarity_score': 0,
            'classification': 'neutral'
        }
    
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    classification = "positive" if polarity > 0 else "negative" if polarity < 0 else "neutral"
    return {
        'id' : id,
        'text' : text,
        'polarity_score': polarity,
        'classification': classification
    }
