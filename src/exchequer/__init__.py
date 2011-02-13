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


def print_table(rows, header=True, outfile=None, justify=unicode.ljust):
    """
    Print a list of rows as a text table.

    A basic example::

        >>> data = [
        ...     ('Name', 'EmpId', 'DeptName'),
        ...     ('Harry', 3415, 'Finance'),
        ...     ('Sally', 2241, 'Sales'),
        ...     ('George', 3401, 'Finance'),
        ...     ('Harriet', 2202, 'Sales')]
        >>> print_table(data)
        Name    | EmpId | DeptName
        --------+-------+---------
        Harry   | 3415  | Finance
        Sally   | 2241  | Sales
        George  | 3401  | Finance
        Harriet | 2202  | Sales

    :param header: Whether or not this table has a header row.
    :param outfile: The file-like object to write to (default: ``sys.stdout``).
    :param justify: A function to justify text in a cell (default:
                    ``unicode.ljust``).
    """
    first_pass, second_pass = itertools.tee(iter(rows))
    columns = column_lengths(first_pass)

    format_row = lambda row: ' | '.join(justify(unicode(cell), length) for cell, length in zip(row, columns))
    print >>outfile, format_row(second_pass.next()).rstrip()
    if header:
        print >>outfile, '-+-'.join('-' * length for length in columns)
    for row in second_pass:
        print >>outfile, format_row(row).rstrip()
