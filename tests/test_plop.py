import pathlib


def test_plop_title():
    html = pathlib.Path("plop/index.html").read_text(encoding="utf-8")
    assert "<title>Plop Bubble Game</title>" in html


def test_canvas_and_score():
    html = pathlib.Path("plop/index.html").read_text(encoding="utf-8")
    assert '<canvas id="game">' in html
    assert 'id="score"' in html
