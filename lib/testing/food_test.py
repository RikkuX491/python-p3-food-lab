#!/usr/bin/env python3
import pytest

from os import path
import runpy
import io
import sys
from food import *

class TestFoodPy:
    '''food.py'''

    def test_something(self):
        '''some message for test.'''
        print(Food)