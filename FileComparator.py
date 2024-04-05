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