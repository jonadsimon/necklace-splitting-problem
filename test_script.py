from necklace_splitting import *

if __name__ == "__main__":
	necklace1 = ['b','a','b','a','a','b','a','b','b','b','a','a'] # this case is degenerate, requiring only 1 cut
	necklace2 = ['a','b','a','a','b','a','b','b','b','a','a','b']
	necklace3 = ['a','a','a','b','b','a','b','b']

	necklace1_split = split_necklace(necklace1)
	necklace2_split = split_necklace(necklace2)
	necklace3_split = split_necklace(necklace3)

	print necklace1, 'can be split as', necklace1_split[0], '&', necklace1_split[1]
	print necklace2, 'can be split as', necklace2_split[0], '&', necklace2_split[1]
	print necklace3, 'can be split as', necklace3_split[0], '&', necklace3_split[1]