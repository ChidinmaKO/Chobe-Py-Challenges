# source: https://www.virgin.com/richard-branson/my-top-10-quotes-living-life-better

import re

HTML = """<!DOCTYPE html>
<head>
  <meta charset="utf-8" />
  <title>My top 10 quotes on living life better | Virgin</title>
</head>
<body>
  <div class="content">
    <p>I’m striving this year to maintain my fitness and to always be learning new things. The new theme on Virgin.com is Live Life Better – a series shining a spotlight on how we can all lead happier, healthier and more fulfilled lives. Virgin has always wanted to make things better for our team and customers and to improve their experiences.</p>
    <p>Here are my top 10 quotes on living life better for some New Year inspiration:</p>
    <p>10. "The beautiful thing about learning is nobody can take it away from you." - B.B King</p>
    <p>9. "Inexperience is an asset. Embrace it." - Wendy Kopp</p>
    <p>8. "Change will not come if we wait for some other person, or if we wait for some other time. We are the ones we’ve been waiting for. We are the change that we seek." - Barack Obama</p>
    <p>7. "The sky is not my limit… I am." - T.F. Hodge</p>
    <p>6. "Life is either a daring adventure or nothing at all." - Helen Keller</p>
    <p>5. "It does not matter how slowly you go as long as you do not stop." - Confucius</p>
    <p>4. "Too many of us are not living our dreams because we are living our fears." - Les Brown</p>
    <p>3. "Continuous efforts – not strength or intelligence – is the key to unlocking our potential." - Winston Churchill</p>
    <p>2. "Believe you can and you’re halfway there." - Theodore Roosevelt</p>
    <p>1. "Success means doing the best we can with what we have. Success is the doing, not the getting; in the trying, not the triumph. Success is a personal standard, reaching for the highest that is in us, becoming all that we can be." - Zig Ziglar</p>
    <p>How do you try and live a healthier, happier life?</p>
  </div>
</body>
</html>"""


def extract_quotes(html: str = HTML) -> dict:
    """See instructions in the Bite description"""
    pattern = re.compile(r'<p>(\d+\.)\s\"(.*)\"\s\-\s([a-zA-Z\.\s]+)</p>')
    quotes = re.findall(pattern, html)
    result = {quote[2].strip(): quote[1].strip() for quote in quotes}
    return result

# tests
import pytest

from quotes import extract_quotes


expected_authors = [
    'B.B King', 'Wendy Kopp', 'Barack Obama', 'T.F. Hodge',
    'Helen Keller', 'Confucius', 'Les Brown', 'Winston Churchill',
    'Theodore Roosevelt', 'Zig Ziglar'
]

expected_quotes = [
    ('The beautiful thing about learning is nobody can take it away'
     ' from you.'),
    'Inexperience is an asset. Embrace it.',
    ('Change will not come if we wait for some other person, or if '
     'we wait for some other time. We are the ones we’ve been '
     'waiting for. We are the change that we seek.'),
    'The sky is not my limit… I am.',
    'Life is either a daring adventure or nothing at all.',
    'It does not matter how slowly you go as long as you do not stop.',
    ('Too many of us are not living our dreams because we are '
     'living our fears.'),
    ('Continuous efforts – not strength or intelligence – is the '
     'key to unlocking our potential.'),
    'Believe you can and you’re halfway there.',
    ('Success means doing the best we can with what we have. '
     'Success is the doing, not the getting; in the trying, '
     'not the triumph. Success is a personal standard, reaching '
     'for the highest that is in us, becoming all that we can be.')
]


@pytest.fixture(scope="module")
def output_your_code():
    return extract_quotes()


def test_quotes_type(output_your_code):
    assert type(output_your_code) == dict


def test_quotes_len(output_your_code):
    assert len(output_your_code) == 10


@pytest.mark.parametrize("author, quote",
                         zip(expected_authors, expected_quotes))
def test_quotes_dict_content(author, quote, output_your_code):
    assert output_your_code.get(author) == quote