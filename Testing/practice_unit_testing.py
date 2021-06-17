#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:34:13 2021

testing practice

@author: veemcclure
"""

import unittest

class TestSum(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
    
    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
    
if __name__ == '__main__':
    unittest.main()
