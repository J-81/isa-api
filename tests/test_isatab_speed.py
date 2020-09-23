"""Tests on isatab.py package speed performance"""
from __future__ import absolute_import
import unittest
import shutil
import tempfile

from isatools.tests import utils
import timeit


class TestIsaTabSpeed(unittest.TestCase):

    def setUp(self):
        self._tab_data_dir = utils.TAB_DATA_DIR
        self._tmp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self._tmp_dir)

    def test_isatab_dump_speed(self):
        setup = '''
from isatools import isatab
import os
from isatools.tests import utils
ISA = isatab.load(os.path.join(utils.TAB_DATA_DIR, "BII-I-1"))
'''
        print(timeit.timeit('isatab.dumps(ISA)', setup=setup, number=1))

    """
    When using isatab._all_end_to_end_paths_with_multiprocessing() it actually 
    seems to slow down compared to _all_end_to_end_paths(). Maybe more sleep 
    time waiting to aggregate results from the split up processes?
    """