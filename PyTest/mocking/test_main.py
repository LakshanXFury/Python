from main import get_weather
import pytest

def test_get_weather(mocker):
    # Mock request.get
    mock_get = mocker.patch("main.requests.get")

    # Set return values
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temprature": 25, "condition" : "Sunny"}

    # Call Function
    result = get_weather("Dubai")

    # Assertions
    assert result == {"temprature": 25, "condition" : "Sunny"}
    mock_get.assert_called_once_with("http://api.weather.com/v1/Dubai")
