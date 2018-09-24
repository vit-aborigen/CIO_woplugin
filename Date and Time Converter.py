from datetime import datetime

def date_time(time: str) -> str:
    dt_obj = datetime.strptime(time, '%d.%m.%Y %H:%M')

    #it doesn't count :(
    # return dt_obj.strftime("%#d %B %Y year %#H hours %#M minute")

    result = dt_obj.strftime("%#d %B %Y year %#H hour") + ('s' if dt_obj.hour not in [1,] else '')
    result += dt_obj.strftime(" %#M minute") + ('s' if dt_obj.hour not in [1,] else '')
    return result


if __name__ == '__main__':
    print(date_time("11.04.1812 01:01"))
    print(date_time("11.04.1812 01:01") == "11 April 1812 year 1 hour 1 minute")