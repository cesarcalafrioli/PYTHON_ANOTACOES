from datetime import timedelta, date

class DateRangeIterable:
    """An iterable that contains its own iterator object."""
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._present_day >= self.end_date:
            raise StopIteration()
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today
    
for day in DateRangeIterable(date(2024, 5, 3), date(2024, 5, 8)):
    print(day)

class DateRangeContainerIterable:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)

r1 = DateRangeContainerIterable(date(2024, 5, 3), date(2024, 5, 8))
print(', '.join(map(str, r1)))

print(max(r1))

# Creating sequences
"""
If __iter__ is not defined on the object, the
iter() function will look for the presence of __getitem__ , and if this is
not found, it will raise TypeError .

A sequence is an object that implements __len__ and __getitem__ and
expects to be able to get the elements it contains, one at a time, in order,
starting at zero as the first index.
"""
class DateRangeSequence:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()
    
    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days
    
    def __getitem__(self, day_no):
        return self._range[day_no]
    
    def __len__(self):
        return len(self._range)

print("")
s1 = DateRangeSequence(date(2018, 1, 1), date(2018, 1, 5))
for day in s1:
    print(day)

print("")
print(s1[0])
print(s1[-1])