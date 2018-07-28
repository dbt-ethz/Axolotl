#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
returns the Boolean difference of A minus B
"""
__author__     = ['Mathias Bernhard']
__copyright__  = 'Copyright 2018 / Digital Building Technologies DBT / ETH Zurich'
__license__    = 'MIT License'
__email__      = '<bernhard@arch.ethz.ch>'

a = [max(t[0],-t[1]) for t in zip(A,B)]
