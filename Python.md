# Python - Today I Learned 

2018

December

November

23

experimenting with the ``text.endswith`` operator.

```
Python 2.7.12 (default, Dec  4 2017, 14:50:18)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> text = iterate through this sentence and stop here. Don't count anything past that period result = text.endswith('.') print result
  File "<stdin>", line 1
    text = iterate through this sentence and stop here. Don't count anything past that period result = text.endswith('.') print result
                         ^
SyntaxError: invalid syntax
>>> text = iterate through this sentence and stop here. Don't count anything past that period
  File "<stdin>", line 1
    text = iterate through this sentence and stop here. Don't count anything past that period
                         ^
SyntaxError: invalid syntax
>>> text = iterate through this sentence and stop here. Don't count anything past that period
  File "<stdin>", line 1
    text = iterate through this sentence and stop here. Don't count anything past that period
                         ^
SyntaxError: invalid syntax
>>> text = "iterate through this sentence and stop here. Don't count anything past that period"
>>> result = text.endswith('.') print result
  File "<stdin>", line 1
    result = text.endswith('.') print result
                                    ^
SyntaxError: invalid syntax
>>> result = text.endswith('.')
>>> print result
False
>>> text = "iterate through this sentence and stop at the full stop."
>>> print result
False
>>> text = "this is a sentence."
>>> result = text.endswith('.')
>>> print result
True
>>> exit()
```
