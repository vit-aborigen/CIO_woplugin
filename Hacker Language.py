import re

NON_CODED_CHARS = '!?$%@.:'


date_format = '([0-3][0-9].[0-1][0-9].[1,2][0-9]{3})'
time_format = '([0-2][0-9]:[0-5][0-9])'
pattern = date_format + '|' + time_format

class HackerLanguage(object):
    def __init__(self):
        self.message = ''

    def write(self, text):
        self.message += text

    def delete(self, N):
        if len(self.message) >= N:
            self.message = self.message[:-N]

    def send(self):
        result = ''
        for char in self.message:
            if char in NON_CODED_CHARS:
                result += char
            elif char == ' ':
                result += '1000000'
            else:
                result += bin(ord(char))[2:]
        return result


    def read(self, text):
        result = ''
        splitted = re.findall('.{7}', text)
        for code in splitted:
            if code == '1000000':
                result += ' '
            elif code[6] in NON_CODED_CHARS:
                result += code[6]
            else:
                result += chr(int(code, 2))

        return result



inst = HackerLanguage()
inst.write('email')
print(inst.send())
print(inst.read('11001011101101110000111010011101100'))


