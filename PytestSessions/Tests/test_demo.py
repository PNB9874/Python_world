import pytest

@pytest.mark.usefixtures("setup")
class Test_Demo:
    def test_testcase(self):
        print("It is test case")