from datetime import datetime


class Timer:
    def __init__(self, hour: str = '00:00'):
        time = datetime.now()
        self.__start_hour = hour
        self.__start_time = time

    def get_time(self) -> str:
        time = datetime.now() - self.__start_time
        [hours, minutes] = self.__start_hour.split(sep=':', maxsplit=2)

        raw_minutes = int(minutes) + time.seconds

        if (time.seconds >= 60):
            new_minutes = time.seconds % 60
            fixed_hours = raw_minutes / 60 if raw_minutes >= 60 else 0

            return '%02d:%02d' % (self.__fix_hour(int(fixed_hours) + int(hours)), self.__fix_minute(new_minutes + int(minutes)))

        if (raw_minutes >= 60):
            fixed_minutes = raw_minutes % 60
            fixed_hours = (raw_minutes / 60) + int(hours)

            return '%02d:%02d' % (self.__fix_hour(int(fixed_hours)), fixed_minutes)

        return '%02d:%02d' % (int(hours), raw_minutes)

    def __fix_hour(self, hour: int) -> int:
        if(hour >= 24):
            return hour - 24
        return hour

    def __fix_minute(self, minute: int) -> int:
        if(minute >= 60):
            return minute - 60
        return minute
