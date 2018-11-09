import math, re
R = 6371

def convert_to_radians(string):
    def calc_rad(splitted_string):
        deg, min, sec, direction = re.split('[°′″]', splitted_string)
        result = float(deg) + float(min)/60 + float(sec)/3600
        if direction in 'SW':
            result *= -1
        return result

    latitude, longitude = string.replace(',',' ').split()
    return (calc_rad(latitude), calc_rad(longitude))


def distance(first, second):
    lat1, lon1 = convert_to_radians(first)
    lat2, lon2 = convert_to_radians(second)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return round(d, 1)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    print(distance(u"48°27′0″N,34°59′0″E", u"15°47′56″S 47°52′0″W"))
