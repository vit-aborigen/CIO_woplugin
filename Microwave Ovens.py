def convert_to_seconds(time):
    if time[-1] == 's':
        return int(time[:-1])
    elif time[-1] == 'm':
        return int(time[:-1]) * 60
    min, sec = time.split(':')
    return int(min) * 60 + int(sec)

def convert_from_seconds(seconds):
    min, sec = divmod(seconds, 60)
    return '{:02d}:{:02d}'.format(min, sec)


class MicrowaveBase:
    def show_time(self, seconds):
        pass

class Microwave1(MicrowaveBase):
    def show_time(self, seconds):
        time = convert_from_seconds(seconds)
        return '_' + time[1:]

class Microwave2(MicrowaveBase):
    def show_time(self, seconds):
        time = convert_from_seconds(seconds)
        return time[:-1] + '_'

class Microwave3(MicrowaveBase):
    def show_time(self, seconds):
        return convert_from_seconds(seconds)


class RemoteControl(object):
    def __init__(self, microwave):
        self.seconds = 0
        self.microwave = microwave

    def set_time(self, time):
        seconds = convert_to_seconds(time)
        if 0 <= seconds <= 5400:
            self.seconds = seconds

    def add_time(self, time):
        self.seconds = min(self.seconds + convert_to_seconds(time), 5400)

    def del_time(self, time):
        self.seconds = max(self.seconds - convert_to_seconds(time), 0)

    def show_time(self):
        return self.microwave.show_time(self.seconds)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    microwave_1 = Microwave1()
    microwave_2 = Microwave2()
    microwave_3 = Microwave3()

    remote_control_1 = RemoteControl(microwave_1)
    remote_control_1.set_time("01:00")

    remote_control_2 = RemoteControl(microwave_2)
    remote_control_2.add_time("90s")

    remote_control_3 = RemoteControl(microwave_3)
    remote_control_3.del_time("300s")
    remote_control_3.add_time("100s")

    assert remote_control_1.show_time() == "_1:00"
    assert remote_control_2.show_time() == "01:3_"
    assert remote_control_3.show_time() == "01:40"
    print("Coding complete? Let's try tests!")