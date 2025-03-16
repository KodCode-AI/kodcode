def test_print_numbers():
    import io
    import contextlib
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        print_numbers([1, 2, 3, 4, 5])
    output = captured_output.getvalue().strip().split('\n')
    assert output == ['1', '2', '3', '4', '5']

def test_print_numbers_with_empty_list():
    import io
    import contextlib
    captured_output = io.StringIO()
    with contextlib.redirect_stdout(captured_output):
        print_numbers([])
    output = captured_output.getvalue().strip()
    assert output == ''