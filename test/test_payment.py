from utils.payment import Payment


def test_payment():
    assert Payment.calculate_payment(['ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']) == ("ASTRID", 85)
