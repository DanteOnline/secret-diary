from .code_aes import AesCoder


class DiaryCoder(AesCoder):
    def __init__(self, key):
        super().__init__(key.encode())

    def code_text(self, text):
        result = self._encrypt(text.encode())
        return result

    def decode_text(self, btext):
        if btext:
            result = self._decrypt(btext).decode().rstrip()
            return result
        else:
            return ''


class Diary:
    def __init__(self, fpath, key):
        self.fpath = fpath
        self.coder = DiaryCoder(key)

    def read(self):
        with open(self.fpath, 'rb') as f:
            btext = f.read()
        text = self.coder.decode_text(btext)
        return text

    def write(self, text):
        btext = self.coder.code_text(text)
        with open(self.fpath, 'wb') as f:
            f.write(btext)
