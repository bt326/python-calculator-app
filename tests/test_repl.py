import builtins
from app import repl


def test_exit(monkeypatch, capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    repl.start()

    captured = capsys.readouterr()
    assert "Goodbye" in captured.out


def test_add(monkeypatch, capsys):
    inputs = iter(["+", "2", "3", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    repl.start()

    captured = capsys.readouterr()
    assert "5" in captured.out


def test_subtraction(monkeypatch, capsys):
    inputs = iter(["-", "10", "3", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    repl.start()

    captured = capsys.readouterr()
    assert "Result:" in captured.out
    assert "7" in captured.out


def test_invalid_operator(monkeypatch, capsys):
    inputs = iter(["x", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    repl.start()

    captured = capsys.readouterr()
    assert "Invalid operation" in captured.out


def test_divide_by_zero(monkeypatch, capsys):
    inputs = iter(["/", "5", "0", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    repl.start()

    captured = capsys.readouterr()
    assert "Error:" in captured.out


def test_get_number_prints_error(monkeypatch, capsys):
    inputs = iter(["abc", "1"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    result = repl.get_number("Enter:")

    captured = capsys.readouterr()
    assert "Invalid number" in captured.out
    assert result == 1.0


def test_repl_startup_message(monkeypatch, capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    repl.start()

    captured = capsys.readouterr()

    assert "Welcome to Calculator" in captured.out
    assert "Operations" in captured.out
def test_multiply(monkeypatch, capsys):
    inputs = iter(["*", "4", "5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    from app.repl import start
    start()

    captured = capsys.readouterr()

    assert "20" in captured.out
