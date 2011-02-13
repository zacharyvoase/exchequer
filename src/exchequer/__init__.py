import itertools


def print_table(rows, header=True):
    """
    Print a list of rows as a text table.

        >>> print_table([
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
    """
    first_pass, second_pass = itertools.tee(iter(rows))
    try:
        columns = [len(cell) for cell in first_pass.next()]
        len_columns = len(columns)
    except StopIteration:
        raise ValueError("Can't print an empty table")

    for i, row in enumerate(first_pass):
        if len(row) != len_columns:
            raise ValueError("Row %d: expected %d columns, got %d" % (
                i + 1, len_columns, len(row)))
        for j, cell in enumerate(row):
            columns[j] = max(columns[j], len(str(cell)))

    format_row = lambda row: ' | '.join(str(cell).ljust(length) for cell, length in zip(row, columns))
    print format_row(second_pass.next()).rstrip()
    if header:
        print '-+-'.join('-' * length for length in columns)
    for row in second_pass:
        print format_row(row).rstrip()
