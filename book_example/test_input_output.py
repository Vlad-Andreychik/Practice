from book_example import input_output


def test_using_file():
    assert (type(input_output.using_file()[0])) == str
    assert (len(input_output.using_file()[1])) == 0
