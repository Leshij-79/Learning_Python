from src.decorators import log


def test_log_file() -> None:
    @log("mylog.txt")
    def func_test(a, b):
        return a + b

    func_test("1", "2")
    with open("mylog.txt", "r", encoding="utf-8") as file_:
        read_text = file_.readlines()
        assert "Время начала" in read_text[0]
        assert "Время окончания" in read_text[1]
        assert read_text[2] == "func_test ok\n"
        assert "Результат выполнения" in read_text[3]


def test_log_file_error() -> None:
    @log("mylog.txt")
    def func_test(a, b):
        return a + b

    func_test("1", 2)
    with open("mylog.txt", "r", encoding="utf-8") as file_:
        read_text = file_.readlines()
        assert "Время начала" in read_text[0]
        assert "Время окончания" in read_text[1]
        assert "error:" in read_text[2]


def test_log_consol(capsys) -> None:
    @log("")
    def func_test(a, b):
        return a + b

    func_test("1", "2")
    captured = capsys.readouterr()
    captured_list = captured.out.strip().split("\n")

    assert "Время начала" in captured_list[0]
    assert "Время окончания" in captured_list[1]
    assert captured_list[2] == "func_test ok"
    assert "Результат выполнения" in captured_list[3]


def test_log_consol_error(capsys) -> None:
    @log("")
    def func_test(a, b):
        return a + b

    func_test("1", 2)
    captured = capsys.readouterr()
    captured_list = captured.out.strip().split("\n")

    assert "Время начала" in captured_list[0]
    assert "Время окончания" in captured_list[1]
    assert "error:" in captured_list[2]
