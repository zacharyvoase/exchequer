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

.. note:: The command-line utility is not yet implemented.

Installation
------------

You can get the module from PyPI::

    pip install exchequer

Quickstart
----------

Begin with the :func:`~exchequer.print_table` function; this is the simplest
way to format your tables from Python. You can also read the
:mod:`~exchequer.cli` documentation for command-line usage instructions.
