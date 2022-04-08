"""
import math

def sqrt(n):
    return math.sqrt(n)

try:
    print sqrt(-1)
except ValueError as e:
    print "Failed to calculate sqrt of -1. Error was: %s" % e.message
except Exception as e:
    print "Something went wrong. Sorry", e
finally:
    print "Thanks for using Python Sqrt Calculator"
_______________________________________________________________________


class InvalidVATError(Exception):
    def __init__(self, msg):
        super(InvalidVATError, self).__init__(msg)

class Invoice:
    def __init__(self, vat):
        if vat < 0:
            raise InvalidVATError("VAT must be >= 0. Got: %d"  % vat)
        self.vat = (1.0 + vat / 100.0)

    def price_with_vat(self, price):
        return price * self.vat

try:
    i = Invoice(18)
    print i.price_with_vat(100)

    j = Invoice(-2)
    print j.price_with_vat(100)

except InvalidVATError as e:
    print "Invalid VAT: ", e.message

"""
