"""
Tennis score sim
Mitchell Vitez
5/9/2014

Simulates tennis sets between players where player one wins PERCENT_ADVANTAGE of points, on average
RESULTS: Small percent advantages lead to vastly different won set numbers.
	A 60% advantage gives about 95% of sets to the advantaged player
Win game if first to 4 by at least 2
Win set if first to 6 by 2 UNLESS tied at 6, then play game up to 7 by 2
"""
import random

NUM_SIMULATIONS = 100000
PERCENT_ADVANTAGE = 0.60

p1SetsWon = 0
p2SetsWon = 0
p2arr = [0] * 50

for counter in xrange(NUM_SIMULATIONS):
	p1setScore = 0
	p2setScore = 0
	while (p1setScore < 6 and p2setScore < 6) or abs(p1setScore - p2setScore) < 2:
		p1score = 0
		p2score = 0
		while p1score < 4 and p2score < 4:
			if (random.random() < PERCENT_ADVANTAGE):
				p1score += 1
			else:
				p2score += 1
		if p1score > p2score:
			p1setScore += 1
		else:
			p2setScore += 1
	p2arr[p2setScore] += 1
	if p1setScore > p2setScore:
		p1SetsWon += 1
	else:
		p2SetsWon += 1

print "Sets won by player one with percent advantage %d: %d" % (int(PERCENT_ADVANTAGE * 100), p1SetsWon)
print "Sets won by player two: %d" % (p2SetsWon)
print "%d simulations were run" % (NUM_SIMULATIONS)
print p2arr[0:10]
print ""
