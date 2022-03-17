from utils.payment import Payment
import os


# Delete the files in the folder to test the output
def test_read_folder():
    assert Payment.read_folder("D:/testes/teste_ioet/ioet-test/employees") == ["The folder is empty."]