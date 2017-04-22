from time import localtime, strftime


def get_current_timestamp():
    return strftime("%Y-%m-%d %H:%M:%S", localtime())


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
