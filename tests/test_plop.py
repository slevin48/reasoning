import pathlib


def test_plop_title():
    html = pathlib.Path("plop/index.html").read_text(encoding="utf-8")
    assert "<title>Plop</title>" in html


def test_plop_button_and_message():
    html = pathlib.Path("plop/index.html").read_text(encoding="utf-8")
    assert "plop-btn" in html
    assert "Plop!" in html
