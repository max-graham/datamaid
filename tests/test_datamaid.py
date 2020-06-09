#!/usr/bin/env python

"""Tests for `datamaid` package."""


import unittest
import pandas as pd
from datamaid import TypeReport


class TestTypeReport(unittest.TestCase):
    """Tests for `TypeReport` class."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_get_shape(self):
        df = pd.DataFrame({
            'col_1': [1, 2, 3],
            'col_2': [4, 5, 6],
        })
        obj = TypeReport(df=df)
        expected = (3, 2)
        result = obj.get_shape()
        self.assertTupleEqual(result, expected)
