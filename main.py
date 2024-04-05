from FileComparator import FileComparator

if __name__ == '__main__':
    comparator = FileComparator('file1.txt', 'file2.txt')
    comparator.compare_files()