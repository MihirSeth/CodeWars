def make_readable(seconds):

    time = '{:02}:{:02}:{:02}'.format(seconds//3600,seconds//60%60, seconds%60)

    return time


print(make_readable(60))


# https://www.codewars.com/kata/52685f7382004e774f0001f7/