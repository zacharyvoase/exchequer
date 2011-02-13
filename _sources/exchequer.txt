:mod:`exchequer` --- Convenience functions
==========================================

This is the top-level module, which should be your starting point for
interaction with the library. The methods here are designed to get you off the
ground as soon as possible.

:func:`~exchequer.print_table`
------------------------------

.. autofunction:: exchequer.print_table(rows, header=True, outfile=None, justify=unicode.ljust)

    With the `outfile` parameter, you can write output to any file-like object
    (such as a :class:`StringIO`, ``sys.stderr`` or a location on the
    filesystem)::

        >>> from StringIO import StringIO
        >>> out = StringIO()
        >>> print_table(data, outfile=out)
        >>> print out.getvalue()
        Name    | EmpId | DeptName
        --------+-------+---------
        Harry   | 3415  | Finance
        Sally   | 2241  | Sales
        George  | 3401  | Finance
        Harriet | 2202  | Sales

    You can modify justification rules using `justify`. It must be a callable
    which will receive a unicode object (the cell) and a column length; you can
    use the methods ``unicode.ljust``, ``unicode.rjust`` and
    ``unicode.center``.

        >>> print_table(data, justify=unicode.rjust)
           Name | EmpId | DeptName
        --------+-------+---------
          Harry |  3415 |  Finance
          Sally |  2241 |    Sales
         George |  3401 |  Finance
        Harriet |  2202 |    Sales
