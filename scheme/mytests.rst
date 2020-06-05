This file holds the tests that you create. Remember to import the python file(s)
you wish to test, along with any other modules you may need.
Run your tests with "python3 ok -t --suite SUITE_NAME --case CASE_NAME -v"
--------------------------------------------------------------------------------

Suite 1

    >>> from scheme_reader import *

    Case Example
        >>> scheme_read(Buffer(tokenize_lines(['nil'])))
        nil
        
    Case 1
        >>> scheme_read(Buffer(tokenize_lines(['(1 (2 3) . 4)'])))
        Pair(1, Pair(Pair(2, Pair(3, nil)), 4))

        >>> scheme_read(Buffer(tokenize_lines(['(1 2 3)'])))
        Pair(1, Pair(2, Pair(3, nil)))
