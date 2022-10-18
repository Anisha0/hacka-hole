from collections import deque


# Function to generate a power set of given set `S`
def findPowerSet(S, s, n):

	# if we have considered all elements
	if n == 0:
		print(s)
		return

	# consider the n'th element
	s.append(S[n - 1])
	findPowerSet(S, s, n - 1)

	s.pop()					# backtrack

	# or don't consider the n'th element
	findPowerSet(S, s, n - 1)


if __name__ == '__main__':

	S = [1, 2, 3]

	s = []
	findPowerSet(S, s, len(S))
