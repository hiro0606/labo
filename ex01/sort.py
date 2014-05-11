#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random as rand
import time

###バブルソート###
def BubbleSort(inlist):
  """バブルソート"""
  length = len(inlist)
  for i in range(length):
    for j in range(i,length):
      if inlist[i] > inlist[j]:
        inlist[i],inlist[j] = inlist[j],inlist[i]
  return inlist

"""
###クイックソート###
def pivot(inlist,left,right):
  length = right - left + 1
  i,j = rand.sample(range(length),2)#
  print i,j
  if inlist[i] > inlist[j]:
    return inlist[i]
  else:return inlist[j]

def partition(inlist,left,right,threshold):
  l = left
  r = right
  while l <= r:#軸が交差するまで
    while l <= right and inlist[l] < threshold:l += 1
    while r >= left and inlist[r] >= threshold:r -= 1
    if l > r:break
    temp = inlist[l]
    inlist[l] = inlist[r]
    inlist[r] = temp
    l += 1
    r -= 1
  return l


def QuickSort(inlist,left,right):
  if left == right:return
  th = pivot(inlist,left,right)
  print th
  k = partition(inlist,left,right,th)
  print inlist
  print k
  QuickSort(inlist,left,k-1)
  QuickSort(inlist,k,right)
"""



"""
def QuickSort(inlist):
  pv = 0
  if len(inlist)>= 3:
    l1,l2,l3 = rand.sample(inlist,3)
    if l1 >= l2 and l1 <= l3 or l1 <= l2 and l1 >= l3:
      pv = l1
    if l2 >= l1 and l2 <= l3 or l2 <= l1 and l2 >= l3:
      pv = l2
    if l3 >= l1 and l3 <= l2 or l3 <= l1 and l3 >= l2:
      pv = l3
  elif len(inlist)==2:
    if inlist[0] > inlist[1]:
      pv = inlist[0]
    elif inlist[0] < inlist[1]:
      pv = inlist[1]
    else:return inlist
  else:return inlist
  left = []
  right = []
  for i in inlist:
    if i >= pv:
      right.append(i)
    else:
      left.append(i)
  left = QuickSort(left)
  right = QuickSort(right)
  return left + right
"""

def QuickSort(inlist):
  """クイックソート"""
  """リストの先頭をpivotにする"""
  if len(inlist) > 1:
    pivot = inlist[0]
  else:
    return inlist
  left = []
  right = []
  for i in inlist[1:]:
    if i >= pivot:
      right.append(i)
    else:left.append(i)
  left = QuickSort(left)
  right = QuickSort(right)
  return left + [pivot] + right

"""モンティホール問題"""
def MontyHall(trial_number):
  change_percent = 0
  no_change_percent = 0
  for i in range(0,trial_number):
    ###当たりドアの作成###
    door = [0] * 3
    hit_number = rand.randint(0,2)
    door[hit_number] = 1
  
    ###最初に選択する扉番号の決定###
    first_select_number = rand.randint(0,2)

    ###司会者が自分の選択した扉と当たり扉以外の扉を選択###
    monty_number = rand.randint(0,2)
    while monty_number == hit_number or monty_number == first_select_number:
      monty_number = rand.randint(0,2)

    ###ドアを交換しなかった場合###
    if door[first_select_number] == 1:
      no_change_percent += 1
    ###交換した場合###
    else: change_percent += 1

  print float(change_percent) / trial_number
  print float(no_change_percent) / trial_number

if __name__ == "__main__":
  #demolist = [6,1,1,4,3,9,10,2,5]
  demolist2 = [rand.randint(0,100) for i in range(0,100)]
  time1 = time.clock()
  print BubbleSort(demolist2)
  time2 = time.clock()
  print time2 - time1
  time1 = time.clock()
  print QuickSort(demolist2)
  time2 = time.clock()
  print time2 - time1
  time1 = time.clock()
  print sorted(demolist2)
  time2 = time.clock()
  print time2 - time1
  MontyHall(1000)