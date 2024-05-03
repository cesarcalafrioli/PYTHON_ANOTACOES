fd = open(filename)
try:
    proccess_file(fd)
finally:
    fd.close()

# An alternative to a code above, in accordance with PEP-343
with open(filename) as fd:
    process_file(fd)


""""
Context managers consists of two magic methods: __enter__ and __exit__

Create a class that implements the __enter__ and __exit__ magic methods
and then that object will be able to support the context manager
protocol.

Book "Clean code in Python" -> Pg. 66 - 73
"""
# Example 2
def stop_database():
    run("systemctl stop postgresql.service")

def start_database():
    run("systemctl start postgresql.service")

class DBHandler:
    def __enter__(self):
        stop_database()
        return self
    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()

def db_backup():
    run("pg_dump database")

def main():
    with DBHandler():
        db_backup()

# Example 3 - Previous example rewritten with the context manager decorator
import contextlib

@contextlib.contextmanager
def db_handler():
    try:
        stop_database()
        yield
    finally:
        start_database()

with db_handler():
    db_backup()

# Example 4 - Providing a class as the logic for applying
# a decorator to a function that will make it run inside
# the context manager
class dbhandler_decorator(contextlib.ContextDecorator):
    def __enter__(self):
        stop_database()
        return self
    def __exit__(self, ext_type, ex_value, ex_traceback):
        start_database()

@dbhandler_decorator()
def offline_backup():
    run("pg_dump database")

# Example 5 - Using contextlib.suppress to avoid certain
# exceptions in situations where we know it is safe to ignore
# them. It's similar to use try/except block and passing method
# makes it more explicit that those exceptions are controlled as
# part of our logic
import contextlib

with contextlib.suppress(DataConversionException):
    parse_data(input_json_or_dict)