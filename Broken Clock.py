from math import trunc

def broken_clock(starting_time, wrong_time, error_description):
    multipliers_to_seconds = (3600, 60, 1)
    starting_time_in_seconds = sum([multiplier * int(init_time) for multiplier, init_time in zip(multipliers_to_seconds, starting_time.split(':'))])
    wrong_time_in_seconds = sum([multiplier * int(init_time) for multiplier, init_time in zip(multipliers_to_seconds, wrong_time.split(':'))])
    diff = abs(wrong_time_in_seconds - starting_time_in_seconds)
    shift, period = error_description.split(' at ')
    shift_in_seconds = parse_error_correction(shift)
    period_in_seconds = parse_error_correction(period)
    result = starting_time_in_seconds + diff * period_in_seconds / (period_in_seconds + shift_in_seconds)
    return '{:02}:{:02}:{:02}'.format(trunc(result//3600), trunc(result//60%60), trunc(result%60))


def parse_error_correction(error):
    def return_multiplier(name: str):
        names = {'hour': 3600, 'minute': 60, 'sec': 1}
        for tm in names:
            if name.startswith(tm):
                return names[tm]
    value, multiplier = error.split(' ')
    return int(value) * return_multiplier(multiplier)



print(broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds'))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') == '00:00:22', 'Fifth example'
