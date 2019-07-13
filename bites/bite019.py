from datetime import datetime, timedelta

NOW = datetime.now()
    
class Promo:
  def __init__(self, name:str, expires:datetime=NOW):
    self.name = name
    self.expires = expires

  @property
  def expired(self):
    return self.expires <= NOW

# tests
# from datetime import timedelta

# from simple_property import Promo, NOW


def test_promo_expired():
    past_time = NOW - timedelta(seconds=3)
    twitter_promo = Promo('twitter', past_time)
    assert twitter_promo.expired


def test_promo_not_expired():
    future_date = NOW + timedelta(days=1)
    newsletter_promo = Promo('newsletter', future_date)
    assert not newsletter_promo.expired