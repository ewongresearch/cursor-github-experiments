"""Minimal experiment: verify repo sync and CI on GitHub."""
HELLO_CODE = "30624700"
def greet(name: str = "GitHub") -> str:
    return f"Hello from Cursor Cloud Agent — {name}! (code: {HELLO_CODE})"
if __name__ == "__main__":
    print(greet())
