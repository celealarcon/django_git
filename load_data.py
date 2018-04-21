import csv
def load_data():
	X = []
	y = []
	test = []
	traincount = 0
	testcount = 0
	with open('Spike Challenge/dataset.csv') as _dataset:
		buff = csv.reader(_dataset)
		for song in buff:
			X.append([])
			for i in range(6):
				try:
					X[traincount].append(float(song[i]))
				except:
					print("fail", traincount)
			try:
				y.append(int(song[6]))
			except:
				print("fail_label", traincount)
			traincount += 1
	with open('Spike Challenge/_data_test.csv') as _dataset:
		buff = csv.reader(_dataset)
		for song in buff:
			test.append([])
			for i in range(6):
				try:
					test[testcount].append(float(song[i]))
				except:
					print("fail", testcount)
			testcount += 1
	return X, y, traincount, test