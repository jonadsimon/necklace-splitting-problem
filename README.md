# Necklace Splitting Problem

The [necklace splitting problem](https://en.wikipedia.org/wiki/Necklace_splitting_problem) considers a necklace on which t different types of beads are strung, and asks for the minimum number of pieces that the necklace must be cut into such that, if the pieces are grouped into k disjoint sets, that each set contains the same number of each type of bead. It turns out that, regardless of necklace length, the number of cuts required is always ≤(k-1)t.

# Algorithm

In the case where k=t=2, there exists a linear time algorithm for finding the two (or fewer) cuts which are needed to solve the problem. That algorithm is contained in the file `necklace_splitting.py"

# Extras

I was inspired to write this code after watching a beautiful video walkthrough of the proof by 3Blue1Brown. [The video can be found here.](https://www.youtube.com/watch?v=FhSFkLhDANA)

