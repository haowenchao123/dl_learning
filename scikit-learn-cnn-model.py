import numpy as np
import pandas as pd
from sklearn import datasets


if __name__ == '__main__':

	#加载IRIS数据集合
	scikit_iris = datasets.load_iris()

	#转换为pandas的DataFrame格式， 以便于观察数据
	pd_iris = pd.DataFrame(data = np.c_[scikit_iris['data'], scikit_iris['target']], columns = np.append(scikit_iris.feature_names, ['y']))
	#print(pd_iris.head(3))

	#选择全部特征参与训练模型
	X = pd_iris[scikit_iris.feature_names]
	y = pd_iris['y']

	from sklearn.model_selection import train_test_split
	from sklearn import metrics

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 0)
    
    # (1) 选择模型
	from sklearn.neighbors import KNeighborsClassifier
	knn = KNeighborsClassifier(n_neighbors = 10)

    # (2) 拟合模型
	knn.fit(X_train, y_train)

	# (3) 预测
	y_predict_on_train = knn.predict(X_train)
	y_predict_on_test = knn.predict(X_test)

	print('准确率为: {}'.format(metrics.accuracy_score(y_train, y_predict_on_train)))
	print('准确率为: {}'.format(metrics.accuracy_score(y_test, y_predict_on_test)))

