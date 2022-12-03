import inspect

from app import settings

def get_username_from_call_stack():
    stack_arr = inspect.stack()
    for item in stack_arr:
        if 'request' in item.frame.f_locals:
            r = item.frame.f_locals['request']
            if type(r).__name__ == 'WSGIRequest':
                if r.user.is_anonymous:
                    return 'anonymous'
                return item.frame.f_locals['request'].user.username
    return 'unknown'

def get_all_intervals(min_per_interval = settings.MINUTES_PER_INTERVAL_DEFAULT):
    days = []
    for day in range(1,32):
        minutes = []
        for minute in range(0, int(1440 / min_per_interval)):
            minutes.append(0)
        days.append(minutes)
    return days