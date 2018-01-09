import math, operator

def euclidean_similarity(data1, data2, num_attr):
	distance = 0
	for x in range(num_attr):
		distance += pow((data1[x] - data2[x]), 2)
	return math.sqrt(distance)
  
def kNN(trainingSet, test_data, k):
	similarity = []
	num_attr = len(test_data)
	for x in range(len(trainingSet)):
		dist = euclidean_similarity(test_data, trainingSet[x], num_attr)
		similarity.append((trainingSet[x], dist))
	similarity.sort(key=operator.itemgetter(1))
	kn_neighbors = []
	print 'The ',k,' nearest neighbours are:'
	for x in range(k):
		kn_neighbors.append(similarity[x][0])
		print similarity[x][0]
	return kn_neighbors

def max_class(kn_neighbors):
	num_vote = {}
	for x in range(len(kn_neighbors)):
		targ_class = kn_neighbors[x][-1]
		if targ_class in num_vote:
			num_vote[targ_class] += 1
		else:
			num_vote[targ_class] = 1
	sortedVotes = sorted(num_vote.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

def main():
	trainingSet=[]
	testSet=[]
	num_inst=input("Enter the number of data instances: ")
	num_attr=input("Enter the number of attributes: ")
	
	for i in range(num_inst):
		temp_train=[]
		print 'Enter the attributes of instance' , i+1
		for j in range(num_attr):
			attr_val=input()
			temp_train.append(attr_val)
		class_val=raw_input("Enter the class: ")
		temp_train.append(class_val)
		trainingSet.append(temp_train)
	
	print("........Enter the test data.......")
	temp_test=[]
	print("Enter the attributes of test data")
	for j in range(num_attr):
		attr_val=input()
		temp_test.append(attr_val)
	testSet.append(temp_test)

	test_class=[]
	k = input("Enter the number of nearest neighbours to be considered: ")
	for x in range(len(testSet)):
		kn_neighbors = kNN(trainingSet, testSet[x], k)
		result = max_class(kn_neighbors)
		test_class.append(result)
		print('Predicted class for test data is' + repr(result))
	
main()
