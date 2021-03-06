# -*- coding: utf-8 -*-

## Function to add the elements of an array
def add_array(arr):
  L=len(arr)
  S=0
  for elt in arr:
    S=S+elt
  return S

## Function that finds pairs of numbers in a sequantial array whose product is equal to 
## the sum of all the remaining numbers in the array.
def find_pairs(arr): 
  ## Initialize an array to contain eligible pairs of numbers
  elig_pairs=[]
  ## Length of array
  L=len(arr)
  ## Go over all the pairs of numbers in the sequence
  ## I am assuming that the numbers in a pair are distinct     
  for n in range (L):  
    for m in range (n+1,L):  ## Note the starting point of this loop to avoid double counting of the pairs
      if ( (add_array(arr)-arr[n]-arr[m]) == (arr[n]*arr[m]) ):
        elig_pairs.append([arr[n],arr[m]])
        
  return elig_pairs
while True:
  
  N=int(input("Enter an integer: "))
  numbers=[n for n in range(1,N+1)]

  print(find_pairs(numbers))  
