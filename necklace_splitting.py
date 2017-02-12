'''
Created on Feb 11, 2017 by Jonathan Simon
'''

from collections import Counter
from warnings import warn

def split_necklace(necklace):
	'''
	DESCRIPTION:

	See README.md for details

	INPUTS:

	list(str) - list of strings, with each unique string corresponding to a unique bead type

	OUTPUTS:

	list(tuple(int)) - list of tuples of start/end indexes (inclusive) denoting the segments of the necklace belonging to the first group
	list(tuple(int)) - list of tuples of start/end indexes (inclusive) denoting the segments of the necklace belonging to the second group
	'''

	####################################################
	### Verify the conditions of the problem are met ###
	####################################################

	bead_counter = Counter(necklace)

	# Check that the necklace contains exactly two types of beads
	if len(bead_counter) != 2:
		raise Exception("Necklace must contain exactly two types of beads")

	# Check that the necklace contains a multiple of two of each bead type
	for bead in bead_counter:
		if bead_counter[bead] % 2 != 0:
			raise Exception("There exists non-even number of '{0}' beads in the necklace, therefore necklace cannot be split".format(bead))


	#######################################
	### Solve the degenerate 1-cut case ###
	#######################################

	# Check that the necklace is not degenerate
	# If it is degenerate, return the single-cut solution
	bead_to_idx = dict(zip(bead_counter.keys(), [0,1]))
	left_bead_pair_count = [0,0]
	for i in range(len(necklace)):
		left_bead_pair_count[bead_to_idx[left_bead_pair_count[i]]] += 1
		if [2*left_bead_pair_count[0],2*left_bead_pair_count[1]] == bead_counter.values():
			warn("The solution is degenerate, requiring only 1 cut")
			return [(0,i)], [(i+1,len(necklace)-1)]


	######################################
	### Solve the general two-cut case ###
	######################################
	
	# First constuct a dict which maps pairs of counts to indices
	# Because can't create a dict with dict keys without rolling our own FrozenDict class, just use pairs of counts
	left_cum_sum_dict = dict()
	left_bead_pair_count = [0,0]
	for i in range(len(necklace)):
		left_bead_pair_count[bead_to_idx[necklace[i]]] += 1
		left_cum_sum_dict[tuple(left_bead_pair_count)] = i

	# Next iterate from right to left, looking for complimentary pairs
	right_bead_pair_compliment_count = bead_counter.values()
	for i in range(len(necklace)-1,-1,-1):
		right_bead_pair_compliment_count[bead_to_idx[necklace[i]]] -= 1
		if tuple(right_bead_pair_compliment_count) in left_cum_sum_dict:
			idx = left_cum_sum_dict[tuple(right_bead_pair_compliment_count)]
			return [(0,idx),(i,len(necklace)-1)], [(idx+1,i-1)]