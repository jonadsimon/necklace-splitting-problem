'''
Created on Feb 11, 2017 by Jonathan Simon
'''

from collections import Counter

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

	# Check that the necklace contains exactly two types of beads
	if len(set(necklace)) != 2:
		raise Exception("Necklace must contain exactly two types of beads")

	# Check that the necklace contains a multiple of two of each bead type
	bead_counter = Counter(necklace)
	for bead in bead_counter:
		if bead_counter[bead] % 2 != 0:
			raise Exception("There exists non-even number of '{0}' beads in the necklace, therefore necklace cannot be split".format(bead))

	# Check that the necklace is not degenerate, requiring only a single cut
	


	# Solve the general two-cut case