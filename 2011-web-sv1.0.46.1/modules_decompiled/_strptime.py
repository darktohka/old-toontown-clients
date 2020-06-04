# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\cygwin\home\toonpub\player\wintools\sdk\python\Python-2.4.1\Lib\_strptime.py
import time, locale, calendar
from re import compile as re_compile
from re import IGNORECASE
from re import escape as re_escape
from datetime import date as datetime_date
try:
    from thread import allocate_lock as _thread_allocate_lock
except:
    from dummy_thread import allocate_lock as _thread_allocate_lock

__author__ = 'Brett Cannon'
__email__ = 'brett@python.org'
__all__ = [
 'strptime']

def _getlang():
    return locale.getlocale(locale.LC_TIME)


class LocaleTime(object):
    __module__ = __name__

    def __init__(self):
        self.lang = _getlang()
        self.__calc_weekday()
        self.__calc_month()
        self.__calc_am_pm()
        self.__calc_timezone()
        self.__calc_date_time()
        if _getlang() != self.lang:
            raise ValueError('locale changed during initialization')

    def __pad(self, seq, front):
        seq = list(seq)
        if front:
            seq.insert(0, '')
        else:
            seq.append('')
        return seq

    def __calc_weekday(self):
        a_weekday = [ calendar.day_abbr[i].lower() for i in range(7) ]
        f_weekday = [ calendar.day_name[i].lower() for i in range(7) ]
        self.a_weekday = a_weekday
        self.f_weekday = f_weekday

    def __calc_month(self):
        a_month = [ calendar.month_abbr[i].lower() for i in range(13) ]
        f_month = [ calendar.month_name[i].lower() for i in range(13) ]
        self.a_month = a_month
        self.f_month = f_month

    def __calc_am_pm(self):
        am_pm = []
        for hour in (1, 22):
            time_tuple = time.struct_time((1999, 3, 17, hour, 44, 55, 2, 76, 0))
            am_pm.append(time.strftime('%p', time_tuple).lower())

        self.am_pm = am_pm

    def __calc_date_time(self):
        time_tuple = time.struct_time((1999, 3, 17, 22, 44, 55, 2, 76, 0))
        date_time = [None, None, None]
        date_time[0] = time.strftime('%c', time_tuple).lower()
        date_time[1] = time.strftime('%x', time_tuple).lower()
        date_time[2] = time.strftime('%X', time_tuple).lower()
        replacement_pairs = [('%', '%%'), (self.f_weekday[2], '%A'), (self.f_month[3], '%B'), (self.a_weekday[2], '%a'), (self.a_month[3], '%b'), (self.am_pm[1], '%p'), ('1999', '%Y'), ('99', '%y'), ('22', '%H'), ('44', '%M'), ('55', '%S'), ('76', '%j'), ('17', '%d'), ('03', '%m'), ('3', '%m'), ('2', '%w'), ('10', '%I')]
        replacement_pairs.extend([ (tz, '%Z') for tz_values in self.timezone for tz in tz_values ])
        for (offset, directive) in ((0, '%c'), (1, '%x'), (2, '%X')):
            current_format = date_time[offset]
            for (old, new) in replacement_pairs:
                if old:
                    current_format = current_format.replace(old, new)

            time_tuple = time.struct_time((1999, 1, 3, 1, 1, 1, 6, 3, 0))
            if time.strftime(directive, time_tuple).find('00'):
                U_W = '%U'
            else:
                U_W = '%W'
            date_time[offset] = current_format.replace('11', U_W)

        self.LC_date_time = date_time[0]
        self.LC_date = date_time[1]
        self.LC_time = date_time[2]
        return

    def __calc_timezone(self):
        try:
            time.tzset()
        except AttributeError:
            pass

        no_saving = frozenset(['utc', 'gmt', time.tzname[0].lower()])
        if time.daylight:
            has_saving = frozenset([time.tzname[1].lower()])
        else:
            has_saving = frozenset()
        self.timezone = (
         no_saving, has_saving)


class TimeRE(dict):
    __module__ = __name__

    def __init__(self, locale_time=None):
        if locale_time:
            self.locale_time = locale_time
        else:
            self.locale_time = LocaleTime()
        base = super(TimeRE, self)
        base.__init__({'d': '(?P<d>3[0-1]|[1-2]\\d|0[1-9]|[1-9]| [1-9])', 'H': '(?P<H>2[0-3]|[0-1]\\d|\\d)', 'I': '(?P<I>1[0-2]|0[1-9]|[1-9])', 'j': '(?P<j>36[0-6]|3[0-5]\\d|[1-2]\\d\\d|0[1-9]\\d|00[1-9]|[1-9]\\d|0[1-9]|[1-9])', 'm': '(?P<m>1[0-2]|0[1-9]|[1-9])', 'M': '(?P<M>[0-5]\\d|\\d)', 'S': '(?P<S>6[0-1]|[0-5]\\d|\\d)', 'U': '(?P<U>5[0-3]|[0-4]\\d|\\d)', 'w': '(?P<w>[0-6])', 'y': '(?P<y>\\d\\d)', 'Y': '(?P<Y>\\d\\d\\d\\d)', 'A': self.__seqToRE(self.locale_time.f_weekday, 'A'), 'a': self.__seqToRE(self.locale_time.a_weekday, 'a'), 'B': self.__seqToRE(self.locale_time.f_month[1:], 'B'), 'b': self.__seqToRE(self.locale_time.a_month[1:], 'b'), 'p': self.__seqToRE(self.locale_time.am_pm, 'p'), 'Z': self.__seqToRE((tz for tz_names in self.locale_time.timezone for tz in tz_names), 'Z'), 
           '%': '%'})
        base.__setitem__('W', base.__getitem__('U').replace('U', 'W'))
        base.__setitem__('c', self.pattern(self.locale_time.LC_date_time))
        base.__setitem__('x', self.pattern(self.locale_time.LC_date))
        base.__setitem__('X', self.pattern(self.locale_time.LC_time))

    def __seqToRE(self, to_convert, directive):
        to_convert = sorted(to_convert, key=len, reverse=True)
        for value in to_convert:
            if value != '':
                break
        else:
            return ''

        regex = ('|').join((re_escape(stuff) for stuff in to_convert))
        regex = '(?P<%s>%s' % (directive, regex)
        return '%s)' % regex

    def pattern(self, format):
        processed_format = ''
        regex_chars = re_compile('([\\\\.^$*+?\\(\\){}\\[\\]|])')
        format = regex_chars.sub('\\\\\\1', format)
        whitespace_replacement = re_compile('\\s+')
        format = whitespace_replacement.sub('\\s*', format)
        while '%' in format:
            directive_index = format.index('%') + 1
            processed_format = '%s%s%s' % (processed_format, format[:directive_index - 1], self[format[directive_index]])
            format = format[directive_index + 1:]

        return '%s%s' % (processed_format, format)

    def compile(self, format):
        return re_compile(self.pattern(format), IGNORECASE)


_cache_lock = _thread_allocate_lock()
_TimeRE_cache = TimeRE()
_CACHE_MAX_SIZE = 5
_regex_cache = {}

def strptime(data_string, format='%a %b %d %H:%M:%S %Y'):
    global _TimeRE_cache
    _cache_lock.acquire()
    try:
        time_re = _TimeRE_cache
        locale_time = time_re.locale_time
        if _getlang() != locale_time.lang:
            _TimeRE_cache = TimeRE()
        if len(_regex_cache) > _CACHE_MAX_SIZE:
            _regex_cache.clear()
        format_regex = _regex_cache.get(format)
        if not format_regex:
            format_regex = time_re.compile(format)
            _regex_cache[format] = format_regex
    finally:
        _cache_lock.release()
    found = format_regex.match(data_string)
    if not found:
        raise ValueError('time data did not match format:  data=%s  fmt=%s' % (data_string, format))
    if len(data_string) != found.end():
        raise ValueError('unconverted data remains: %s' % data_string[found.end():])
    year = 1900
    month = day = 1
    hour = minute = second = 0
    tz = -1
    week_of_year = -1
    week_of_year_start = -1
    weekday = julian = -1
    found_dict = found.groupdict()
    for group_key in found_dict.iterkeys():
        if group_key == 'y':
            year = int(found_dict['y'])
            if year <= 68:
                year += 2000
            else:
                year += 1900
        elif group_key == 'Y':
            year = int(found_dict['Y'])
        elif group_key == 'm':
            month = int(found_dict['m'])
        elif group_key == 'B':
            month = locale_time.f_month.index(found_dict['B'].lower())
        elif group_key == 'b':
            month = locale_time.a_month.index(found_dict['b'].lower())
        elif group_key == 'd':
            day = int(found_dict['d'])
        elif group_key == 'H':
            hour = int(found_dict['H'])
        elif group_key == 'I':
            hour = int(found_dict['I'])
            ampm = found_dict.get('p', '').lower()
            if ampm in ('', locale_time.am_pm[0]):
                if hour == 12:
                    hour = 0
            elif ampm == locale_time.am_pm[1]:
                if hour != 12:
                    hour += 12
        elif group_key == 'M':
            minute = int(found_dict['M'])
        elif group_key == 'S':
            second = int(found_dict['S'])
        elif group_key == 'A':
            weekday = locale_time.f_weekday.index(found_dict['A'].lower())
        elif group_key == 'a':
            weekday = locale_time.a_weekday.index(found_dict['a'].lower())
        elif group_key == 'w':
            weekday = int(found_dict['w'])
            if weekday == 0:
                weekday = 6
            else:
                weekday -= 1
        elif group_key == 'j':
            julian = int(found_dict['j'])
        elif group_key in ('U', 'W'):
            week_of_year = int(found_dict[group_key])
            if group_key == 'U':
                week_of_year_start = 6
            else:
                week_of_year_start = 0
        elif group_key == 'Z':
            found_zone = found_dict['Z'].lower()
            for (value, tz_values) in enumerate(locale_time.timezone):
                if found_zone in tz_values:
                    if time.tzname[0] == time.tzname[1] and time.daylight and found_zone not in ('utc',
                                                                                                 'gmt'):
                        break
                    else:
                        tz = value
                        break

    if julian == -1 and week_of_year != -1 and weekday != -1:
        first_weekday = datetime_date(year, 1, 1).weekday()
        preceeding_days = 7 - first_weekday
        if preceeding_days == 7:
            preceeding_days = 0
        if weekday == 6 and week_of_year_start == 6:
            week_of_year -= 1
        if weekday == 0 and first_weekday == 0 and week_of_year_start == 6:
            week_of_year += 1
        if week_of_year == 0:
            julian = 1 + weekday - first_weekday
        else:
            days_to_week = preceeding_days + 7 * (week_of_year - 1)
            julian = 1 + days_to_week + weekday
    if julian == -1:
        julian = datetime_date(year, month, day).toordinal() - datetime_date(year, 1, 1).toordinal() + 1
    else:
        datetime_result = datetime_date.fromordinal(julian - 1 + datetime_date(year, 1, 1).toordinal())
        year = datetime_result.year
        month = datetime_result.month
        day = datetime_result.day
    if weekday == -1:
        weekday = datetime_date(year, month, day).weekday()
    return time.struct_time((year, month, day, hour, minute, second, weekday, julian, tz))