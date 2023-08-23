import pytest
from joke_bot import Bot

@pytest.fixture
def bot():
    return Bot()

def mock_input(prompt=""):
    if "feeling" in prompt:
        return "happy"
    elif "mood for" in prompt:
        return "dad joke"
    return ""

def test_tell_joke(bot):
    # Mock the input function to provide consistent responses.
    bot.input = mock_input

    joke = bot.tell_joke()
    assert isinstance(joke, str)
    assert len(joke) > 20

def test_rate_joke(bot):
    joke = "Why did the chicken cross the road? To get to the other side!"
    rating = bot.rate_joke(joke)
    assert isinstance(rating, int)
    assert 1 <= rating <= 10