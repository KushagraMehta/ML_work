from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

class cancer_cal:
	def __init__(self):
		self.file=pd.read('blog/static/breast-cancer-wisconsin-data.csv')
		label = self.file['breast_cancer']
		features = self.file[self.file.columns[:-1]]

		split_data=train_test_split(label,features,test_size=0.1)
		train_label,self.test_label,train_features,self.test_features=split_data

		self.dtree_algo = tree.DecisionTreeClassifier()
		self.knn_algo = KNeighborsClassifier(n_neighbors=5)
		self.trained_knn = self.knn_algo.fit(train_features, train_label)
		self.trained_dtree = self.dtree_algo.fit(train_features, train_label)
	def result(self, info):

		out_dtree = self.trained_dtree.predict([info])

		out_knn = self.trained_knn.predict([info])

		return out_knn,out_dtree
	def accuracy(self):

		test_out_dtree=self.trained_dtree.predict(self.test_features)
		dtree_acc=accuracy_score(self.test_label,test_out_dtree)

		test_out_knn=self.trained_knn.predict(self.test_features)
		knn_acc=accuracy_score(self.test_label,test_out_dtree)

		return dtree_acc,knn_acc