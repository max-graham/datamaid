#!/usr/bin/env python

"""Tests for `datamaid` package."""


import unittest
import pandas as pd
import pandas.testing as pdt
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

    def test_get_column_mins(self):
        df = pd.DataFrame({
            'col_1': [1, 2, 3],
            'col_2': [6, 4, 5]
        })
        obj = TypeReport(df=df)
        expected = pd.Series([1, 4], index=['col_1', 'col_2'], name='min')
        result = obj.get_column_mins()
        pdt.assert_series_equal(expected, result)

    def test_get_column_maxs(self):
        df = pd.DataFrame({
            'col_1': [1, 2, 3],
            'col_2': [6, 4, 5]
        })
        obj = TypeReport(df=df)
        expected = pd.Series([3, 6], index=['col_1', 'col_2'], name='max')
        result = obj.get_column_maxs()
        pdt.assert_series_equal(expected, result)

    def test_get_column_ranges(self):
        df = pd.DataFrame({
            'col_1': [1, 2, 3],
            'col_2': [4, 5, 6],
        })
        obj = TypeReport(df=df)
        expected = pd.DataFrame({
            'min': [1, 4],
            'max': [3, 6]
        }, index = ['col_1', 'col_2'])
        result = obj.get_column_ranges()
        pdt.assert_frame_equal(expected, result)
