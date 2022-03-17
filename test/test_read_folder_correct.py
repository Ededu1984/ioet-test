from utils.payment import Payment


# Change the directory to the right one - ASTRID AND RENE CORRECT EXAMPLES
def test_read_folder():
    assert Payment.read_folder("D:/testes/teste_ioet/ioet-test/employees") == [[
        'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'],
        ['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00']]
