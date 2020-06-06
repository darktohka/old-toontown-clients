# File: c (Python 2.2)

from time import localtime, mktime, strftime
from types import SliceType
__all__ = [
    'error',
    'setfirstweekday',
    'firstweekday',
    'isleap',
    'leapdays',
    'weekday',
    'monthrange',
    'monthcalendar',
    'prmonth',
    'month',
    'prcal',
    'calendar',
    'timegm',
    'month_name',
    'month_abbr',
    'day_name',
    'day_abbr']
error = ValueError
January = 1
February = 2
mdays = [
    0,
    31,
    28,
    31,
    30,
    31,
    30,
    31,
    31,
    30,
    31,
    30,
    31]

class _indexer:
    
    def __getitem__(self, i):
        if isinstance(i, SliceType):
            return self.data[i.start:i.stop]
        else:
            return self.data[i]



class _localized_month(_indexer):
    
    def __init__(self, format):
        self.format = format

    
    def __getitem__(self, i):
        continue
        self.data = [ strftime(self.format, (2001, j, 1, 12, 0, 0, 1, 1, 0)) for j in range(1, 13) ]
        self.data.insert(0, '')
        return _indexer.__getitem__(self, i)

    
    def __len__(self):
        return 13



class _localized_day(_indexer):
    
    def __init__(self, format):
        self.format = format

    
    def __getitem__(self, i):
        continue
        self.data = [ strftime(self.format, (2001, 1, j + 1, 12, 0, 0, j, j + 1, 0)) for j in range(7) ]
        return _indexer.__getitem__(self, i)

    
    def __len__(self_):
        return 7


day_name = _localized_day('%A')
day_abbr = _localized_day('%a')
month_name = _localized_month('%B')
month_abbr = _localized_month('%b')
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(7)
_firstweekday = 0

def firstweekday():
    return _firstweekday


def setfirstweekday(weekday):
    global _firstweekday
    if MONDAY <= weekday:
        pass
    weekday <= SUNDAY
    if not 1:
        raise ValueError, 'bad weekday number; must be 0 (Monday) to 6 (Sunday)'
    
    _firstweekday = weekday


def isleap(year):
    if not year % 4 == 0 and year % 100 != 0:
        pass
    return year % 400 == 0


def leapdays(y1, y2):
    y1 -= 1
    y2 -= 1
    return (y2 / 4 - y1 / 4 - y2 / 100 - y1 / 100) + (y2 / 400 - y1 / 400)


def weekday(year, month, day):
    secs = mktime((year, month, day, 0, 0, 0, 0, 0, 0))
    tuple = localtime(secs)
    return tuple[6]


def monthrange(year, month):
    if 1 <= month:
        pass
    month <= 12
    if not 1:
        raise ValueError, 'bad month number'
    
    day1 = weekday(year, month, 1)
    if month == February:
        pass
    ndays = mdays[month] + isleap(year)
    return (day1, ndays)


def monthcalendar(year, month):
    (day1, ndays) = monthrange(year, month)
    rows = []
    r7 = range(7)
    day = ((_firstweekday - day1) + 6) % 7 - 5
    while day <= ndays:
        row = [
            0,
            0,
            0,
            0,
            0,
            0,
            0]
        for i in r7:
            if 1 <= day:
                pass
            day <= ndays
            if 1:
                row[i] = day
            
            day = day + 1
        
        rows.append(row)
    return rows


def _center(str, width):
    n = width - len(str)
    if n <= 0:
        return str
    
    return ' ' * ((n + 1) / 2) + str + ' ' * (n / 2)


def prweek(theweek, width):
    print week(theweek, width)
def week(theweek, width):
    days = []
    for day in theweek:
        if day == 0:
            s = ''
        else:
            s = '%2i' % day
        days.append(_center(s, width))
    
    return ' '.join(days)


def weekheader(width):
    if width >= 9:
        names = day_name
    else:
        names = day_abbr
    days = []
    for i in range(_firstweekday, _firstweekday + 7):
        days.append(_center(names[i % 7][:width], width))
    
    return ' '.join(days)


def prmonth(theyear, themonth, w = 0, l = 0):
    print month(theyear, themonth, w, l)
def month(theyear, themonth, w = 0, l = 0):
    w = max(2, w)
    l = max(1, l)
    s = _center(month_name[themonth] + ' ' + `theyear`, 7 * (w + 1) - 1).rstrip() + '\n' * l + weekheader(w).rstrip() + '\n' * l
    for aweek in monthcalendar(theyear, themonth):
        s = s + week(aweek, w).rstrip() + '\n' * l
    
    return s[:-l] + '\n'

_colwidth = 7 * 3 - 1
_spacing = 6

def format3c(a, b, c, colwidth = _colwidth, spacing = _spacing):
    print format3cstring(a, b, c, colwidth, spacing)


def format3cstring(a, b, c, colwidth = _colwidth, spacing = _spacing):
    return _center(a, colwidth) + ' ' * spacing + _center(b, colwidth) + ' ' * spacing + _center(c, colwidth)


def prcal(year, w = 0, l = 0, c = _spacing):
    print calendar(year, w, l, c)
def calendar(year, w = 0, l = 0, c = _spacing):
    w = max(2, w)
    l = max(1, l)
    c = max(2, c)
    colwidth = (w + 1) * 7 - 1
    s = _center(`year`, colwidth * 3 + c * 2).rstrip() + '\n' * l
    header = weekheader(w)
    header = format3cstring(header, header, header, colwidth, c).rstrip()
    for q in range(January, January + 12, 3):
        s = s + '\n' * l + format3cstring(month_name[q], month_name[q + 1], month_name[q + 2], colwidth, c).rstrip() + '\n' * l + header + '\n' * l
        data = []
        height = 0
        for amonth in range(q, q + 3):
            cal = monthcalendar(year, amonth)
            if len(cal) > height:
                height = len(cal)
            
            data.append(cal)
        
        for i in range(height):
            weeks = []
            for cal in data:
                if i >= len(cal):
                    weeks.append('')
                else:
                    weeks.append(week(cal[i], w))
            
            s = s + format3cstring(weeks[0], weeks[1], weeks[2], colwidth, c).rstrip() + '\n' * l
        
    
    return s[:-l] + '\n'

EPOCH = 1970

def timegm(tuple):
    (year, month, day, hour, minute, second) = tuple[:6]
    days = 365 * (year - EPOCH) + leapdays(EPOCH, year)
    for i in range(1, month):
        days = days + mdays[i]
    
    if month > 2 and isleap(year):
        days = days + 1
    
    days = days + day - 1
    hours = days * 24 + hour
    minutes = hours * 60 + minute
    seconds = minutes * 60 + second
    return seconds

