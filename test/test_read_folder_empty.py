from utils.payment import Payment


# Delete the files in the folder to test the output
def test_read_folder():
    assert Payment.read_folder("/home/edson/ioet-test/employees") == ["The folder is empty."]