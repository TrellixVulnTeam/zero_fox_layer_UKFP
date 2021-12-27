import sys

print(sys.path)
print()
from libs.my_libs import testMethod
thing = testMethod('asus')

print(thing)