from fastapi.testclient import TestClient
from datetime import datetime
from main import app  # Import the FastAPI app instance

client = TestClient(app)  # Create a test client using the FastAPI app instance


def test_analyze_comments_sentiment():
    # Define test data
    test_subfeddit_name = "sample_subfeddit"
    test_limit = 10
    test_skip = 0
    test_start_date = datetime(2022, 1, 1)
    test_end_date = datetime(2022, 12, 31)
    test_sort_by_polarity = True
    test_api_key = "your_test_api_key"

    # Make a request to the endpoint
    response = client.get(
        f"/sentiment-analysis/?subfeddit_name={test_subfeddit_name}&limit={test_limit}"
        f"&skip={test_skip}&start_date={test_start_date}&end_date={test_end_date}"
        f"&sort_by_polarity={test_sort_by_polarity}",
        headers={"X-API-Key": test_api_key},
    )

    # Check if the request was successful (status code 200)
    assert response.status_code == 200

    # Check if the response data is a list of dictionaries
    assert isinstance(response.json(), list)