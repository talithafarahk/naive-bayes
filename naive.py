import csv
import math
import pandas as pd 
import numpy as np 


trainset = pd.read_csv('TrainsetTugas1ML.csv', header=None)
label = []
for i in range(1,9):
    label.append(list(set(trainset[i].tolist())))


lebihdari = trainset[trainset[8]=='>50K']
kurangdari = trainset[trainset[8]=='<=50K']

prob_lebih = len(lebihdari) / len(trainset)
prob_kurang = len(kurangdari) / len(trainset)
# print(prob_lebih)
# print(prob_kurang)

def tabel(data):
	hasil = []
	for i in range(1,8):
		state = data.groupby(i)
		num = state.size()
		prob = np.asarray(num.apply(lambda jumlahdata : jumlahdata/len(data)))
		hasil.append(prob)
	return hasil

a = pd.DataFrame(np.asarray(tabel(lebihdari)))
b = pd.DataFrame(np.asarray(tabel(kurangdari)))
# print(a)
# print(b)
df = pd.read_csv('TestsetTugas1ML.csv', header=None)
testSet = pd.DataFrame(df)

dict_prob = { 
'>50K':{ 'adult':a[0][0], 'old':a[1][0], 'young':a[2][0],
'Local-gov':a[0][1],'Private':a[1][1], 'Self-emp-not-inc':a[2][1],
'Bachelors':a[0][2],'HS-grad':a[1][2], 'Some-college':a[2][2],
'Divorced':a[0][3],'Married-civ-spouse':a[1][3], 'Never-married':a[2][3],
'Craft-repair':a[0][4], 'Exec-managerial':a[1][4], 'Prof-specialty':a[2][4],
'Husband':a[0][5],'Not-in-family':a[1][5],'Own-child':a[2][5],
'low':a[0][6],'many':a[1][6],'normal':a[2][6]
}, 
'<=50K':{ 'adult':b[0][0], 'old':b[1][0], 'young':b[2][0], 
'Local-gov':b[0][1], 'Private':b[1][1],'Self-emp-not-inc':b[2][1],
'Bachelors':b[0][2],'HS-grad':b[1][2], 'Some-college':b[2][2],
'Divorced':b[0][3],'Married-civ-spouse':b[1][3], 'Never-married':b[2][3],
'Craft-repair':b[0][4], 'Exec-managerial':b[1][4], 'Prof-specialty':b[2][4],
'Husband':b[0][5],'Not-in-family':b[1][5],'Own-child':b[2][5],
'low':b[0][6],'many':b[1][6],'normal':b[2][6]
}}

result = []
for i in range(1,len(testSet)):
	if (testSet[1][0] == 'age'):
		if (testSet[1][i] == 'young'):
			age_a = dict_prob['>50K']['young']
			age_b = dict_prob['<=50K']['young']
		elif(testSet[1][i] == 'adult'):
			age_a = dict_prob['>50K']['adult']
			age_b = dict_prob['<=50K']['adult']
		else:
			age_a = dict_prob['>50K']['old']
			age_b = dict_prob['<=50K']['old']
	if (testSet[2][0] == 'workclass'):
		if (testSet[2][i] == 'Local-gov'):
			work_a = dict_prob['>50K']['Local-gov']
			work_b = dict_prob['<=50K']['Local-gov']
		elif(testSet[2][i] == 'Private'):
			work_a = dict_prob['>50K']['Private']
			work_b = dict_prob['<=50K']['Private']
		else:
			work_a = dict_prob['>50K']['Self-emp-not-inc']
			work_b = dict_prob['<=50K']['Self-emp-not-inc']
	if (testSet[3][0] == 'education'):
		if (testSet[3][i] == 'Bachelors'):
			edu_a = dict_prob['>50K']['Bachelors']
			edu_b = dict_prob['<=50K']['Bachelors']
		elif(testSet[3][i] == 'HS-grad'):
			edu_a = dict_prob['>50K']['HS-grad']
			edu_b = dict_prob['<=50K']['HS-grad']
		else:
			edu_a = dict_prob['>50K']['Some-college']
			edu_b = dict_prob['<=50K']['Some-college']
	if (testSet[4][0] == 'marital-status'):
		if (testSet[4][i] == 'Divorced'):
			marital_a = dict_prob['>50K']['Divorced']
			marital_b = dict_prob['<=50K']['Divorced']
		elif(testSet[4][i] == 'Married-civ-spouse'):
			marital_a = dict_prob['>50K']['Married-civ-spouse']
			marital_b = dict_prob['<=50K']['Married-civ-spouse']
		else:
			marital_a = dict_prob['>50K']['Never-married']
			marital_b = dict_prob['<=50K']['Never-married']
	if (testSet[5][0] == 'occupation'):
		if (testSet[5][i] == 'Craft-repair'):
			ocu_a = dict_prob['>50K']['Craft-repair']
			ocu_b = dict_prob['<=50K']['Craft-repair']
		elif(testSet[5][i] == 'Exec-managerial'):
			ocu_a = dict_prob['>50K']['Exec-managerial']
			ocu_b = dict_prob['<=50K']['Exec-managerial']
		else:
			ocu_a = dict_prob['>50K']['Prof-specialty']
			ocu_b = dict_prob['<=50K']['Prof-specialty']
	if (testSet[6][0] == 'relationship'):
		if (testSet[6][i] == 'Husband'):
			rela_a = dict_prob['>50K']['Husband']
			rela_b = dict_prob['<=50K']['Husband']
		elif(testSet[6][i] == 'Not-in-family'):
			rela_a = dict_prob['>50K']['Not-in-family']
			rela_b = dict_prob['<=50K']['Not-in-family']
		else:
			rela_a = dict_prob['>50K']['Own-child']
			rela_b = dict_prob['<=50K']['Own-child']
	if (testSet[7][0] == 'hours-per-week'):
		if (testSet[7][i] == 'low'):
			hours_a = dict_prob['>50K']['low']
			hours_b = dict_prob['<=50K']['low']
		elif(testSet[7][i] == 'many'):
			hours_a = dict_prob['>50K']['many']
			hours_b = dict_prob['<=50K']['many']
		else:
			hours_a = dict_prob['>50K']['normal']
			hours_b = dict_prob['<=50K']['normal']
	hasil_lebihdari = age_a * work_a * edu_a * marital_a * ocu_a * rela_a * hours_a * prob_lebih
	hasil_kurangdari = age_b * work_b * edu_b * marital_b * ocu_b * rela_b * hours_b * prob_kurang
	# print(i, hasil_lebihdari)
	# print(i, hasil_kurangdari)
	
	if (hasil_lebihdari > hasil_kurangdari):
		result.append(">50K")
	else:
		result.append("<=50K")

array_result = np.asarray(result)
with open('TebakanTugas1ML.csv', 'w') as fp:
   a = csv.writer(fp,quoting=csv.QUOTE_ALL)
   for word in array_result:
     a.writerow([word])