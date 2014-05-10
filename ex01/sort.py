#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random as rand

def pivot(input_list):
  """ピボット作成関数"""
  if len(input_list) >= 3:
    i,j,m = rand.sample(input_list,3)
    if i <= j and i >= m or i >= j and i <= m:
      return i
    if j <= m and j >= i or j >= m and j <= i:
      return j
    if m <= i and m >= j or m >= i and m <= j:
      return m

def partition(input_list,left,right):
  l = left
  r = right
  while l < r:
    while 



