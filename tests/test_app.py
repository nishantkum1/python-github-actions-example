from app import read_json, resultdata_with_bmi

def test_read_json():
    assert read_json() == "Hello, Nishant!"

def test_resultdata_with_bmi():
    assert resultdata_with_bmi() == "Hello, Nishant!"