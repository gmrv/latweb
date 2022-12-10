import datetime
import inspect
from dataclasses import dataclass
from datetime import timedelta

from app import settings

@dataclass
class IntervalViewItem:
    minutes: int = 0
    max_minutes: int = 0
    percent: int = 0
    hint: str = ""
    start_time: datetime = None

    def inc(self):
        self.minutes +=1
        self.percent = (self.minutes / self.max_minutes * 100)

    def percent_str(self):
        return str(self.percent)

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

def get_all_intervals(start, min_per_interval = settings.MINUTES_PER_INTERVAL_DEFAULT, report_days_count = 1):
    intervals = []
    for interval in range(0, int(1440 / min_per_interval) * report_days_count):
        interval_start_time = start + timedelta(minutes=(min_per_interval*interval))
        intervals.append(IntervalViewItem(start_time=interval_start_time.astimezone(), max_minutes=min_per_interval))
    return intervals