from utils.dicts import get_val

data = {"vcs": "mercurial", "test": "pytest"}


def test_empty_dict():
    assert get_val({}, "anything", "git") == "git"


def test_key_present():
    assert get_val(data, "vcs", "git") == "mercurial"


def test_key_not_present():
    assert get_val(data, "anything", "default") == "default"

