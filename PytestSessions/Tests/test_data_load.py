import pytest

from PytestSessions.conftest import dataLoad


@pytest.mark.usefixtures("dataLoad")
class Test_DataRetrive():
    def test_userdata(self, dataLoad):
        for word in dataLoad:
            print(word)