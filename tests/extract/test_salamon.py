"""Tests for motif/extract/salamon.py
"""
import unittest
import os
import numpy as np

from motif.extract import salamon
from motif.core import Contours


def array_equal(array1, array2):
    return np.all(np.isclose(array1, array2))


def relpath(f):
    return os.path.join(os.path.dirname(__file__), f)


AUDIO_FILE = relpath("../data/short.wav")
CONTOURS = relpath("../data/short_contours_salamon.csv")


class TestSalamon(unittest.TestCase):

    def setUp(self):
        self.etr = salamon.Salamon()

    def test_get_id(self):
        expected = 'salamon'
        actual = self.etr.get_id()
        self.assertEqual(expected, actual)

    @unittest.skip("Binary doesn't exist on remote machine.")
    def test_compute_contours(self):
        ctr = self.etr.compute_contours(AUDIO_FILE)
        self.assertTrue(isinstance(ctr, Contours))

    def test_failed_compute_contours(self):
        with self.assertRaises(IOError):
            self.etr.compute_contours('does/not/exist.wav')


class TestLoadContours(unittest.TestCase):

    def test_load(self):
        (actual_idx, actual_times,
         actual_freqs, actual_sal) = salamon._load_contours(CONTOURS)
        idx_length = len(actual_idx)
        self.assertEqual(idx_length, len(actual_times))
        self.assertEqual(idx_length, len(actual_freqs))
        self.assertEqual(idx_length, len(actual_sal))
