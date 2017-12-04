from pytest import raises
import os
from diary import DiaryCoder, Diary


class TestCoder:
    def test_code(self):
        coder = DiaryCoder('Super Secret Key')
        text = 'My text'
        result = coder.code_text(text)
        dtext = coder.decode_text(result)
        assert dtext == text
        # пустой текст
        coder = DiaryCoder('Super Secret Key')
        text = b''
        dtext = coder.decode_text(text)
        assert dtext == ''


class TestDiary:
    def test_rw(self):
        text = 'The Rain in spain'
        d = Diary('test.dat', 'Super Secret Key')
        d.write(text)
        result = d.read()
        assert result == text
        # надо удалить test.dat
        os.remove('test.dat')
