from .diary import Diary


class ConsoleClient:

    def run(self):
        fpath = input('Input file path>')
        key = input('Input key>')
        d = Diary(fpath, key)
        text = d.read()
        print(text)
        while True:
            new_row = input('>')
            if new_row.startswith('end'):
                d.write(text)
                break
            text += '\n' + new_row