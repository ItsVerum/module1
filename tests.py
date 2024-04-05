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


def test_compare_files(file_comparator, tmpdir):
    same_file = str(tmpdir.join("same.txt"))
    diff_file = str(tmpdir.join("diff.txt"))
    file_comparator.compare_files(same_file, diff_file)
    with open(same_file, 'r') as file:
        same = set(line.strip() for line in file)
    with open(diff_file, 'r') as file:
        diff = set(line.strip() for line in file)
    assert same == {"Python is great. Yes, it is."}
    assert diff == {"Hello, world!", "It's a beautiful day."}