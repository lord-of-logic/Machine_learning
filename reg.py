from math import sqrt

def mean(data):
	return float(sum(data))/len(data)

def variance(data):
	data_mean=mean(data)
	return sum([(d-data_mean)**2 for d in data])

def co_var(data):
	covar=0
	x=[row[0] for row in data]
	y=[row[1] for row in data]
	x_mean=mean([row[0] for row in data])
	y_mean=mean([row[1] for row in data])
	for i in range(len(data)):
		covar+=(x[i]-x_mean)*(y[i]-y_mean)
	return covar

def calc_parameters(data):
	x_mean=mean([row[0] for row in data])
	y_mean=mean([row[1] for row in data])
	x=[row[0] for row in data]
	m = co_var(data) / variance(x)
	c = y_mean - (m * x_mean)
	return [m, c]

def predict(x,m,c):
	return m*x + c

def main():
	num_inst=input("Enter the number of data instances: ")
	training_data=[]
	test_data=[]
	for i in range(num_inst):
		temp_train=[]
		print 'Enter x and y for instance ', i+1
		x=input()
		y=input()
		temp_train.append(x)
		temp_train.append(y)
		training_data.append(temp_train)
	num_test=input("Enter the number of test data: ")
	for i in range(num_test):
		x=input()
		test_data.append(x)
	x_mean=mean([row[0] for row in training_data])
	y_mean=mean([row[1] for row in training_data])
	x_var =variance([row[0] for row in training_data])
	y_var =variance([row[1] for row in training_data])
	xy_covar=co_var(training_data)
	print 'Mean of x is ',x_mean,'and variance is ',x_var
	print 'Mean of y is ',y_mean,'and variance is ',y_var
	print 'Co-variance of x and y is ',xy_covar
	parameters=[]
	parameters=calc_parameters(training_data)
	print 'The regression line is y = ',parameters[0],'x + ',parameters[1]
	for i in range(len(test_data)):
		print 'The predicted value for x = ',test_data[i],' is ',predict(test_data[i],parameters[0],parameters[1])
main()