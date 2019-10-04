import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import random

data = pd.read_csv('train.csv')
# data = pd.read_csv('train_feature.csv')
print('read')
# data2 = pd.read_csv('public/label-001.csv')
data2 = pd.read_csv('D:\kaggle\label1-45.csv')
print('read2')
# data3 = pd.read_csv('test_feature2.csv')
data3 = pd.read_csv('feature.csv')
print('read3')
usersList = data3['user_id'].values
print(usersList)
print(len(usersList))
# print(data.loc[1][0])
# print(df[1:2]) #data.at[1, '0']
# print(len(data))    #1251

lr = LogisticRegression()
x_train = data.drop(['user_id'], axis=1)
x_train = x_train
x_test = data3.drop(['user_id'], axis=1)

time_slot = np.zeros((len(usersList), 28))
for i in range(28):
    index = 'time_slot_' + str(i)
    y_train = data2[index]
    lr.fit(x_train, y_train)
    pred = lr.predict_proba(x_test)[:,1]
    # print(pred)
    for y in range(len(pred)):
        time_slot[y][i] = pred[y]
    print(i)

fieldnames = ['time_slot_0', 'time_slot_1', 'time_slot_2', 'time_slot_3', 'time_slot_4', 'time_slot_5', 'time_slot_6',
              'time_slot_7', 'time_slot_8', 'time_slot_9', 'time_slot_10', 'time_slot_11', 'time_slot_12',
              'time_slot_13', 'time_slot_14', 'time_slot_15', 'time_slot_16', 'time_slot_17', 'time_slot_18',
              'time_slot_19', 'time_slot_20', 'time_slot_21', 'time_slot_22', 'time_slot_23', 'time_slot_24',
              'time_slot_25', 'time_slot_26', 'time_slot_27']
table = pd.DataFrame(time_slot, index=usersList, columns=fieldnames)
table['user_id'] = usersList
table.set_index('user_id', inplace=True)
table.to_csv('test_result.csv')


# for index in range(len(data)-1):
#     # for i in range(896):
#     #     x_train.append(data[str(index)][i])
#     # print(x_train[0])
#     for j in range(28):
#         y_train.append(data2.loc[index][j])
#     # x_train = np.reshape(x_train, (len(x_train), 1))
#     # y_train = np.reshape(y_train, (len(y_train), 1))
#     # x_train = np.array(x_train).reshape((-1, 1))
#     lr.fit(x_train, y_train)
#     # sc = StandardScaler()
#     # sc.fit(x_train)
#     # x_train_nor = sc.transform(x_train)
#     # x_test_nor = sc.transform()
#     # x_train = np.reshape(x_train, (len(x_train), 1))
#     # y_train = np.reshape(y_train, (len(y_train), 1))
#     for x in range(0, 32):
#         start = x * 28
#         train[x] = x_train[start:start+28]
#     train1 = np.reshape(train, (28, 32))
#     lr.fit(train1, y_train)
#     x_train.clear()
#     y_train.clear()
# for y in range(32):
#     start = y * 28
#     test[y] = x_test[start:start+28]
# test = np.reshape(test, (28, 32))



