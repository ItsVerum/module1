class FileComparator:
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2


    def read_file(self, filename):
        with open(filename, 'r') as file:
            return set(line.strip() for line in file)


    def write_file(self, filename, data):
        with open(filename, 'w') as file:
            for line in data:
                file.write(line + '\n')

    def compare_files(self):
        set1 = self.read_file(self.file1)
        set2 = self.read_file(self.file2)

        same = set1 & set2
        diff = (set1 - set2) | (set2 - set1)

        self.write_file('same.txt', same)
        self.write_file('diff.txt', diff)

