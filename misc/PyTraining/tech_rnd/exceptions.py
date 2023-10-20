import traceback
"""
if exception is not handled in inner block (try except), it will be analysed again the exceptions in outer tyr-except 
block.

try - <any block> is valid
for "else" you need at-least one except block is required

try-else (not possible)
try-except
try-finally
try-except-else-finally
try-else-finally (not possible)
etc.
"""


try:
    1/0
    try:
        raise ValueError("There is value error")
    except TypeError as e:
        print ("There is type error", e.__class__.__name__)
        traceback.format_exc()
except (ZeroDivisionError, AttributeError) as e:
    print("ZERO-D occureed", e.__class__.__name__, e)
    print(traceback.format_exc())
except Exception as e:
    print("Error occureed", e.__class__.__name__, e)
    print(traceback.format_exc())

else:
    print("ELSE block, executed only if no exceptions occured")

finally:
    print("Finally block is always executed")


class InvalidNumber(Exception):
    pass


def chec_return():
    try:
        1/0 # return 2
        # 1/1 return 2, return 1 is overshadoed wby return in finally block
        # if exception occured in try block, none of the statements in remaining try block executed
        return 1
    except Exception:
        print("Haha")
    finally:
       return 2

print(chec_return())