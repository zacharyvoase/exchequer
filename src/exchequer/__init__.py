import itertools


def column_lengths(rows):
    """
    Get the maximum column lengths of a given iterable of rows.

    Returns an empty tuple if no rows are given. All rows must be of the same
    length, otherwise a :exc:`ValueError` will be raised. This function is
    unicode-ready; :func:`unicode` will be called on every item to get its
    string representation (for determining length).

        >>> column_lengths([('a', 'bcdef', 'gh'), ('fed', 'up', 'boring')])
        (3, 5, 6)
        >>> column_lengths([])
        ()
        >>> column_lengths([('a', 'b'), ('1', '2', '3')])
        Traceback (most recent call last):
        ...
        ValueError: Row 1: expected 2 columns, got 3
    """
    columns = []
    for i, row in enumerate(rows):
        if columns and len(columns) != len(row):
            raise ValueError("Row %d: expected %d columns, got %d" % (
                i, len(columns), len(row)))
        elif not columns:
            columns = [len(unicode(cell)) for cell in row]
        else:
            for j, cell in enumerate(row):
                columns[j] = max(len(unicode(cell)), columns[j])
    return tuple(columns)


def print_table(rows, header=True, justify=unicode.ljust):
    """
    Print a list of rows as a text table.

        >>> data = [
        ...     ('Name', 'EmpId', 'DeptName'),
        ...     ('Harry', 3415, 'Finance'),
        ...     ('Sally', 2241, 'Sales'),
        ...     ('George', 3401, 'Finance'),
        ...     ('Harriet', 2202, 'Sales')]
        >>> print_table(data, header=True)
        Name    | EmpId | DeptName
        --------+-------+---------
        Harry   | 3415  | Finance
        Sally   | 2241  | Sales
        George  | 3401  | Finance
        Harriet | 2202  | Sales

    You can modify justification rules using `justify`. It will be called with
    a unicode object (the cell) and a column length, so you can use the methods
    ``unicode.ljust``, ``unicode.rjust`` and ``unicode.center``.

        >>> print_table(data, header=True, justify=unicode.rjust)
           Name | EmpId | DeptName
        --------+-------+---------
          Harry |  3415 |  Finance
          Sally |  2241 |    Sales
         George |  3401 |  Finance
        Harriet |  2202 |    Sales
    """
    first_pass, second_pass = itertools.tee(iter(rows))
    columns = column_lengths(first_pass)

    format_row = lambda row: ' | '.join(justify(unicode(cell), length) for cell, length in zip(row, columns))
    print format_row(second_pass.next()).rstrip()
    if header:
        print '-+-'.join('-' * length for length in columns)
    for row in second_pass:
        print format_row(row).rstrip()
