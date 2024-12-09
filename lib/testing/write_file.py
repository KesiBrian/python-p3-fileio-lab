def test_write_file(tmpdir):
    file_path = tmpdir.join('test_file.txt')
    write_file(file_path, "This is a test content.")
    content = read_file(file_path)
    assert content == "This is a test content."
