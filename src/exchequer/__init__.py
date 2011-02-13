import itertools


def print_table(rows, header=True, outfile=None, justify=unicode.ljust, encoding='utf-8'):
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
    :param encoding: An encoding to assume when dealing with bytestrings
                     (default: utf-8).
    """
    first_pass, second_pass = itertools.tee(ensure_text(iter(rows), encoding=encoding))
    columns = column_lengths(first_pass)

    if not columns:
        raise ValueError("Can't print an empty table")

    format_row = lambda row: ' | '.join(justify(cell, length) for cell, length in zip(row, columns))
    print >>outfile, format_row(second_pass.next()).rstrip()
    if header:
        print >>outfile, '-+-'.join('-' * length for length in columns)
    for row in second_pass:
        print >>outfile, format_row(row).rstrip()


def ensure_text(row_iterator, encoding='utf-8'):
    """
    Ensure that all the cells in the given row iterator are unicode objects.

    This method will return a new iterator over the rows in which all cells
    have been coerced to unicode, using the specified encoding where necessary.
    """

    def cell_to_unicode(cell):
        if isinstance(cell, str):
            return unicode(cell, encoding)
        elif hasattr(cell, 'decode'):
            return cell.decode(encoding)
        return unicode(cell)

    for row in row_iterator:
        yield map(cell_to_unicode, row)


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
    len_columns = 0
    for i, row in enumerate(rows):
        if columns and len_columns != len(row):
            raise ValueError("Row %d: expected %d columns, got %d" % (
                i, len_columns, len(row)))
        elif not columns:
            columns = [len(cell) for cell in row]
            len_columns = len(columns)
        else:
            for j, cell in enumerate(row):
                columns[j] = max(len(cell), columns[j])
    return tuple(columns)


def _get_tests():
    import doctest
    return doctest.DocTestSuite()
