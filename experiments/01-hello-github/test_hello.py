from hello import HELLO_CODE, greet
def test_greet_default():
    assert "GitHub" in greet()
    assert HELLO_CODE in greet()
def test_greet_custom_name():
    assert greet("Erik") == f"Hello from Cursor Cloud Agent — Erik! (code: {HELLO_CODE})"
