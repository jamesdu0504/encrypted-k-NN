from sklearn.neighbors import KNeighborsClassifier
from numpy import genfromtxt

from optparse import OptionParser


training_data = 'simple5x3.data.training'
testing_data = 'simple5x3.data.testing'


#training_data = 'datasets/wine/wine.data.ope.training'
#testing_data = 'datasets/wine/wine.data.ope.testing'

#training_data = 'datasets/wine/wine.data.training'
#testing_data = 'datasets/wine/wine.data.testing'

#training_data = 'datasets/abalone/abalone.data.ope.training'
#testing_data = 'datasets/abalone/abalone.data.ope.testing'

#training_data = 'datasets/abalone/abalone.data.training'
#testing_data = 'datasets/abalone/abalone.data.testing'

#training_data = 'datasets/iris/iris.data.training'
#testing_data = 'datasets/iris/iris.data.testing'

#training_data = 'datasets/iris/iris.data.ope.training'
#testing_data = 'datasets/iris/iris.data.ope.testing'

#training_data = 'datasets/climate/climate.data.training'
#testing_data = 'datasets/climate/climate.data.testing'

#training_data = 'datasets/climate/climate.data.ope.training'
#testing_data = 'datasets/climate/climate.data.ope.testing'

#training_data = 'datasets/credit/credit.data.training'
#testing_data = 'datasets/credit/credit.data.testing'

#training_data = 'datasets/credit/credit.data.ope.training'
#testing_data = 'datasets/credit/credit.data.ope.testing'


parser = OptionParser()
parser.add_option("-f", dest="base_filename", default=True,
                          help="base name of the training set and testing set files")
parser.add_option("-k", type="int", dest="k", default=True, help="number of nearest neighbors")

(options, args) = parser.parse_args()

knn = KNeighborsClassifier(n_neighbors=int(options.k), weights='distance', algorithm='brute')

# reading the training data
training_data = options.base_filename + ".training"
data_and_classes = genfromtxt(training_data, dtype='int')
data = data_and_classes[:, 0:(len(data_and_classes[0]) - 1)]
classes = data_and_classes[:, (len(data_and_classes[0]) - 1)]
knn.fit(data, classes)
print("training data:")
print(data)
print("training classes")
print(classes)


# reading the testing data
testing_data = options.base_filename + ".testing"
data_and_classes = genfromtxt(testing_data, dtype='int')
data = data_and_classes[:, 0:(len(data_and_classes[0]) - 1)]
classes = data_and_classes[:, (len(data_and_classes[0]) - 1)]

print("testing data:")
print(data)
print("testing classes")
print(classes)

for i in range(len(data)):
    print("knn.predict(data[%d])" % i);
    print(knn.predict(data[i]));

print(knn.score(data, classes))

