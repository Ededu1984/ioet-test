from utils.payment import Payment


def test_read_folder():
    assert Payment.read_folder("./employees") == [['ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']]

