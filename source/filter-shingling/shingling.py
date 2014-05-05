#!/usr/bin/python

# threadhold to determine if similar
Threshold = 0.0075  #88 #0053

#Length of each shingle
Shingle_Length = 3

#Check if 2 strings x and y are similar
#(in our use case, x and y should be the contents of the documents)
def is_similar(x, y, k = Shingle_Length):
	return score(x, y, k) >= Threshold

#Return the similarity of x and y
def score(x, y, k = Shingle_Length):
	x = x.split()
	y = y.split()
	return jaccard(shingling(x,k), shingling(y,k))

def jaccard(a, b):
	a = set([" ".join(x) for x in a])
	b = set([" ".join(x) for x in b])
	intersection = set.intersection(a, b)
	union = set.union(a, b)
	return len(intersection) / float(len(union))

def shingling(a, k):
	return [a[i:i+k] for i in xrange(0, len(a)-k)]

##################################################################
### Code from this point is for testing purpose only
##################################################################
def read_data():
	result = {}
	for i in xrange(1, 44):
		with open("410data/%s" % i) as f:
			result[i] = f.read()
	return result

def main():
	data = read_data()   
	l= len(data)
	print l
	#res = [[0 for x in xrange(l)] for x in xrange(l)] 
	f = open('workfile', 'w')
	counter = 0
	for i in range(1,l+1):
		for j in range(1,l+1):
			print  (i, j)
			s = score(data[i], data[j])
			temp = (str(i), str(j), str(s))  
			if (i < j and is_similar(data[i], data[j])):
				f.write(' '.join(temp)+'\n')
			counter+=1
	print counter
			
		
	
	

if __name__ == '__main__':
	main()
