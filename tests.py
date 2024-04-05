import pytest
from FileComparator import FileComparator


@pytest.fixture
def file_comparator(tmpdir):
    file1 = tmpdir.join("file1.txt")
    file1.write("Hello, world!\nPython is great. Yes, it is.")

    file2 = tmpdir.join("file2.txt")
    file2.write("Python is great. Yes, it is.\nIt's a beautiful day.")

    return FileComparator(str(file1), str(file2))

def test_read_file(file_comparator):
    assert file_comparator.read_file(file_comparator.file1) == {"Hello, world!", "Python is great. Yes, it is."}

def test_write_file(file_comparator, tmpdir):
    data = {"Hello, world!", "Python is great. Yes, it is."}
    file_path = str(tmpdir.join("test.txt"))
    file_comparator.write_file(file_path, data)
    with open(file_path, 'r') as file:
        lines = set(line.strip() for line in file)
    assert lines == data