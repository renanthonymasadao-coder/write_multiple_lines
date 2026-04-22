class FileWriter:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_lines(self):
        with open(self.file_name, 'w') as file:
            while True:
                line = input("Enter line: ")
                file.write(line + "\n")

                choice = input("Are there more lines? y/n: ").lower()
                if choice == 'n':
                    break