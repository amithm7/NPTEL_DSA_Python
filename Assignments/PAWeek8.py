'''
(http://www.iarcs.org.in/inoi/contests/oct2004/Advanced-1.php)

Dividing Sequences
(IARCS OPC Archive, K Narayan Kumar, CMI)

This problem is about sequences of positive integers a1,a2,…,aN. A subsequence
of a sequence is anything obtained by dropping some of the elements. For
example, 3,7,11,3 is a subsequence of 6,3,11,5,7,4,3,11,5,3 , but 3,3,7 is not a
subsequence of 6,3,11,5,7,4,3,11,5,3 .
A fully dividing sequence is a sequence a1,a2,…,aN where ai divides aj whenever
i < j. For example, 3,15,60,720 is a fully dividing sequence.
Given a sequence of integers your aim is to find the length of the longest fully
dividing subsequence of this sequence.
Consider the sequence 2,3,7,8,14,39,145,76,320
It has a fully dividing sequence of length 3, namely 2,8,320, but none of length
4 or greater.
Consider the sequence 2,11,16,12,36,60,71,17,29,144,288,129,432,993 .
It has two fully dividing subsequences of length 5, (Marked by a -num- at the
end of numbers)
  -2-,11,16,-12-,-36-,60,71,17,29,-144-,-288-,129,432,993 and
  -2-,11,16,-12-,-36-,60,71,17,29,-144-,288,129,-432-,993
and none of length 6 or greater.

Solution hint
Let the input be a1, a2, …, aN. Let us define Best(i) to be the length of
longest dividing sequence in a1,a2,…ai that includes ai.
Write an expression for Best(i) in terms of Best(j) with j<i, with base case
Best(1) = 1. Solve this recurrence using dynamic programming.

Full solution
(http://www.iarcs.org.in/inoi/contests/oct2004/Advanced-1-solution.php)

Input format
The first line of input contains a single positive integer N indicating the
length of the input sequence. Lines 2,…,N+1 contain one integer each.
The integer on line i+1 is ai.

Output format
Your output should consist of a single integer indicating the length of the
longest fully dividing subsequence of the input sequence.

Test Data
You may assume that N ≤ 2500.

Example:
Here are the inputs and outputs corresponding to the two examples discussed
above.

Sample input 1:
9
2
3
7
8
14
39
145
76
320

Sample output 1:
3

Sample input 2:
14
2
11
16
12
36
60
71
17
29
144
288
129
432
993

Sample output 2:
5
'''
# dsubs --> Dividing Sub Sequence

seq = []        # original sequence
dsubslist = []  # lengths of longest dividing subsequences

n = int(input())
for i in range(n):
  seq.append(int(input()))

# Each iteration gives longest dsubs's (seq[i] included) length
for i in range(n):
  dsubs = 1             # Counting 1st element of dsubs, i.e. for seq[i]
  for j in range(i):    # Comparing seq[i] with elements before it
    if seq[i] % seq[j] == 0:
      dsubs = max(dsubs,(dsubslist[j])+1)
      # max ensures counting of longest dsubs associated with seq[i]
      # if currently counting dsubs is longer, dsubs remains same. Else, longest
      # dsubs associated with seq[j] is counted, dsubslist[j]+1, adds 1 more.
  dsubslist.append(dsubs)

print(max(dsubslist))


'''
1st Algo: Fails as sequence() doesn't return longest dsubs
'''
# seq = []    # Stores the original sequence
# dsubs = []  # A dividing subsequence of a list, which includes it's last element
# dsubslist = []  # All subsequences of original sequence

# n = int(input())
# for i in range(n):
#     seq += [int(input())]

# # Computes dsubs for current sequence
# def sequence (cseq):
#     global dsubs
#     dsubs.append(cseq[(len(cseq)-1)])
#     for e in range(len(cseq)-2, -1, -1):
#         if cseq[len(cseq)-1] % cseq[e] == 0:
#             sequence(cseq[:(e+1)])
#             break

# # Calling sequence() with list which creates dsubs for it, passed list gets
# # shorter and shorter from the end every call
# for i in range(n):
#     sequence(seq[:n-i])
#     dsubslist.append(dsubs)
#     dsubs = []

# ldsubslist = list(map(len, dsubslist))

# # print (dsubslist)
# # print (ldsubslist)
# print (max (ldsubslist))
