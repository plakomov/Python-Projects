# datetime practice module
import datetime
import pytz # brings in the timezone database; easier to use with the timezones

# Naive and Aware (Aware has more info)

d = datetime.date(2022, 7, 24)

print(d)  # just outputs general format for a specific date

tdy = datetime.date.today()  # prints out today's date
print(tdy)
print(tdy.day)
print(tdy.weekday())  # Monday 0, Sunday 6
print(tdy.isoweekday())  # Monday 1, Sunday 7

# Time deltas ( difference in time between two dates)

tdelta = datetime.timedelta(days=7)

print(tdy + tdelta)  # prints out date 7 days in the future
print(tdy - tdelta)  # prints out date 7 days in the past

# date +/- date equals timedelta

bday = datetime.date(2022, 5, 10)
tillbday = bday - tdy  # timedelta object

print(tillbday)
print(tillbday.total_seconds())

t = datetime.time(9, 30, 45, 400)  # hours, minutes, seconds and microseconds still Naive
print(t)
print(t.hour)

dt = datetime.datetime(2022, 1, 28, 15, 22, 30, 5000)  # gives all the info from data and time
print(dt)

timedelta_1 = datetime.timedelta(hours=12)
print(datetime.datetime.today() + timedelta_1)

dt_today = datetime.datetime.today()  # current local time with localzone with none
dt_now = datetime.datetime.now()  # we can pass in the time zone if need be
dt_utcnow = datetime.datetime.utcnow()  # gives us utc time at this timezone

print(dt_today, dt_now, dt_utcnow)

dt_pytz = datetime.datetime(2022, 1, 28, 3, 30, 45, tzinfo=pytz.UTC)
print(dt_pytz)

dt_pytz_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_pytz_now)

dt_pytz_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

print(dt_pytz_utcnow)

dt_timezone_change = datetime.datetime.now(tz=pytz.UTC).astimezone(pytz.timezone('Canada/Pacific'))
print(dt_timezone_change)

print(dt_timezone_change.strftime("%B %d, %Y")) # Changing the format

d = datetime.datetime.strptime('January 28, 2022', '%B %d, %Y')
print(d)