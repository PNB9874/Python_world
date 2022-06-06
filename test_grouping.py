import pytest

def test_SBI_bank():
    print("SBI")

@pytest.mark.smoke
def test_ICICI_bank():
    print("ICICI")


def test_KOTAK_bank():
    print("Kotak")

@pytest.mark.smoke
def test_HDFC_bank():
    print("HDFC")


def test_financial_sectore():
    print("financial sectore")
