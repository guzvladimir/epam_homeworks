from task03.task_3_get_print_output import my_precious_logger


def test_my_precious_logger_stderr(capsys):
    my_precious_logger("error: file not found")
    out, err = capsys.readouterr()
    assert err == "error: file not found"


def test_my_precious_logger_stdout(capsys):
    my_precious_logger("OK")
    out, err = capsys.readouterr()
    assert out == "OK"
