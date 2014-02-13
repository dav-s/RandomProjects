# Wow This solution is really slow... WAY faster than brute force, but with 1mil numbers, it is slow
# Will probably come back to this one and optimize it

lStart = 0
lChain = 0
foundSols = {}

def longColSeqUnd(num):

	def genSeq(n, lenOChain, st):
		global lStart, lChain, foundSols
		if n==1:
			if lenOChain>lChain:
				lStart = st
				lChain = lenOChain
			return lenOChain
		if n in foundSols:
			print n
			genSeq(1,lenOChain+foundSols[str(n)],st)
		if n%2==0:
			foundSols[str(n)]=genSeq(n/2, lenOChain+1, st)
		else:
			foundSols[str(n)]=genSeq(n*3+1, lenOChain+1, st)

	for i in xrange(2,num):
		if not (i in foundSols):
			genSeq(i,0,i)

	return (lStart,lChain)

print longColSeqUnd(1000000)
