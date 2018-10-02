import re

NON_CODED_CHARS = '!?$%@.:'

class Encoder(object):
    @staticmethod
    def find_date_time(text):
        date_format = '([0-3][0-9].[0-1][0-9].[1,2][0-9]{3})'
        time_format = '([0-2][0-9]:[0-5][0-9])'
        pattern = date_format + '|' + time_format

        datetime_with_position = []
        for item in re.finditer(pattern, text):
            datetime_with_position.append((item.group(), item.start()))
        return datetime_with_position


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
        idx, dict_enum = 0,0
        datetime_positions = Encoder.find_date_time(self.message)
        while idx <= (len(self.message) - 1):
            if len(datetime_positions) and idx == datetime_positions[dict_enum][1]:
                result += datetime_positions[dict_enum][0]
                idx += datetime_positions[dict_enum][1] - 1
                dict_enum += 1
            elif self.message[idx] in NON_CODED_CHARS:
                result += self.message[idx]
            elif self.message[idx] == ' ':
                result += '1000000'
            else:
                result += bin(ord(self.message[idx]))[2:]
            idx += 1
        return result

    def read(self, text):
        result = ''
        formatted = ''.join([char.zfill(7) if char in NON_CODED_CHARS else char for char in text])
        for code in re.findall('.{7}', formatted):
            if code == '1000000':
                result += ' '
            elif code[6] in NON_CODED_CHARS:
                result += code[6]
            else:
                result += chr(int(code, 2))
        return result
