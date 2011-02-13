Exchequer
=========

Exchequer is a Python library and command-line utility for printing tables in
plain-text. Here's how it looks from Python::

    >>> import exchequer
    >>> exchequer.print_table([
    ...     ('Name', 'EmpId', 'DeptName'),
    ...     ('Harry', 3415, 'Finance'),
    ...     ('Sally', 2241, 'Sales'),
    ...     ('George', 3401, 'Finance'),
    ...     ('Harriet', 2202, 'Sales')], header=True)
    Name    | EmpId | DeptName
    --------+-------+---------
    Harry   | 3415  | Finance
    Sally   | 2241  | Sales
    George  | 3401  | Finance
    Harriet | 2202  | Sales

And from the command-line::

    % cat file.txt
    Name,EmpId,DeptName
    Harry,3415,Finance
    Sally,2241,Sales
    George,3401,Finance
    Harriet,2202,Sales
    % exchequer -i csv -o text --header < file.txt
    Name    | EmpId | DeptName
    --------+-------+---------
    Harry   | 3415  | Finance
    Sally   | 2241  | Sales
    George  | 3401  | Finance
    Harriet | 2202  | Sales

Installation
------------

You can get the module from PyPI::

    pip install exchequer

(Un)license
===========

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this
software, either in source code form or as a compiled binary, for any purpose,
commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this
software dedicate any and all copyright interest in the software to the public
domain. We make this dedication for the benefit of the public at large and to
the detriment of our heirs and successors. We intend this dedication to be an
overt act of relinquishment in perpetuity of all present and future rights to
this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
