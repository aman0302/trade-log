from datetime import datetime, tzinfo, timedelta


class Zone(tzinfo):
    def __init__(self, offset_in_minutes, isdst, name):
        self.offset = offset_in_minutes
        self.isdst = isdst
        self.name = name

    def utcoffset(self, dt):
        return timedelta(minutes=self.offset) + self.dst(dt)

    def dst(self, dt):
        return timedelta(hours=1) if self.isdst else timedelta(0)

    def tzname(self, dt):
        return self.name


def get_current_timestamp():
    IST = Zone(330, False, 'IST')
    return datetime.now(IST).strftime('%d/%m/%Y %H:%M:%S')


def military_time_to_string(mil_time):
    if mil_time < 10:
        return '00:0' + str(mil_time)

    elif mil_time < 60:
        return '00:' + str(mil_time)[:2]

    elif mil_time < 960:
        return '0' + str(mil_time)[:1] + ':' + str(mil_time)[1:]

    else:
        return str(mil_time)[:2] + ':' + str(mil_time)[2:]


def mililary_time_adjust_rolling_window(mil_time):
    last_two_digits = (mil_time % 100)
    if (last_two_digits >= 60):
        mil_time = mil_time - last_two_digits + ((mil_time % 100) % 60)
        mil_time += 100

    return mil_time
