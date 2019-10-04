import csv
import time
import numpy as np
import pandas as pd
user = {}
usersList = []


class User:
    def __init__(self):
        self.event_time = []
        # self.time_slot = np.zeros(28, dtype=int)


user_event_time = []
# with open('D:\kaggle\data046-75.csv', newline='') as f:     #public/data-001.csv
#         reader = csv.reader(f)
#         i = 0
#         for row in reader:
#             user_id = row[0]
#             if i != 0:
#                 if user_id not in usersList:
#                     usersList.append(user_id)
#                     # user_event_time.append([])
#                     user[user_id] = User()
#                 user[user_id].event_time.append(row[4])
#                 # user_event_time[int(user_id)].append(row[4])
#             print(i)
#             i += 1
# for file in range(0, 46):
#     filename = 'public/data-0' + str(file) + '.csv'
#     # print(filename)
#     with open(filename, newline='') as f:
#         reader = csv.reader(f)
#         i = 0
#         for row in reader:
#             user_id = row[0]
#             if i != 0:
#                 if user_id not in usersList:
#                     usersList.append(user_id)
#                     user[user_id] = User()
#                 user[user_id].event_time.append(row[4])
#             i += 1
#     print(file)

# print(data['user_id'][0])
# print(user_event_time[1])


# def take_off_ms(u=User()):      # 拿掉毫秒(.後面的)
#     for z in range(len(u.event_time)):
#         t = u.event_time[z]
#         strlist = t.split('.')
#         t = strlist[0]
#         u.event_time[z] = t


def in_which_slot(test):
    # test = time.strptime(str1, '%Y-%m-%d %H:%M:%S')
    # print(test.tm_wday)
    if test.tm_wday == 0:
        if 0 <= test.tm_hour < 1:
            return int(27)
        if 1 <= test.tm_hour < 9:
            return int(0)
        if 9 <= test.tm_hour < 17:
            return int(1)
        if 17 <= test.tm_hour < 21:
            return int(2)
        if 21 <= test.tm_hour < 24:
            return int(3)
    if test.tm_wday == 1:
        if 0 <= test.tm_hour < 1:
            return int(3)
        if 1 <= test.tm_hour < 9:
            return int(4)
        if 9 <= test.tm_hour < 17:
            return int(5)
        if 17 <= test.tm_hour < 21:
            return int(6)
        if 21 <= test.tm_hour < 24:
            return int(7)
    if test.tm_wday == 2:
        if 0 <= test.tm_hour < 1:
            return int(7)
        if 1 <= test.tm_hour < 9:
            return int(8)
        if 9 <= test.tm_hour < 17:
            return int(9)
        if 17 <= test.tm_hour < 21:
            return int(10)
        if 21 <= test.tm_hour < 24:
            return int(11)
    if test.tm_wday == 3:
        if 0 <= test.tm_hour < 1:
            return int(11)
        if 1 <= test.tm_hour < 9:
            return int(12)
        if 9 <= test.tm_hour < 17:
            return int(13)
        if 17 <= test.tm_hour < 21:
            return int(14)
        if 21 <= test.tm_hour < 24:
            return int(15)
    if test.tm_wday == 4:
        if 0 <= test.tm_hour < 1:
            return int(15)
        if 1 <= test.tm_hour < 9:
            return int(16)
        if 9 <= test.tm_hour < 17:
            return int(17)
        if 17 <= test.tm_hour < 21:
            return int(18)
        if 21 <= test.tm_hour < 24:
            return int(19)
    if test.tm_wday == 5:
        if 0 <= test.tm_hour < 1:
            return int(19)
        if 1 <= test.tm_hour < 9:
            return int(20)
        if 9 <= test.tm_hour < 17:
            return int(21)
        if 17 <= test.tm_hour < 21:
            return int(22)
        if 21 <= test.tm_hour < 24:
            return int(23)
    if test.tm_wday == 6:
        if 0 <= test.tm_hour < 1:
            return int(23)
        if 1 <= test.tm_hour < 9:
            return int(24)
        if 9 <= test.tm_hour < 17:
            return int(25)
        if 17 <= test.tm_hour < 21:
            return int(26)
        if 21 <= test.tm_hour < 24:
            return int(27)


field_name = []
user_slot = np.zeros((57159, 924))
for i in range(924):
    field_name.append(i)
for file in range(1, 46):
    if file < 10:
        filename = 'public/data-00' + str(file) + '.csv'
    else:
        filename = 'public/data-0' + str(file) + '.csv'
    print(filename)
    data = pd.read_csv(filename)
    print('read')
    print('-------------------------------------------')
# for user_id in usersList:
#     take_off_ms(user[user_id])
#     for index in range(len(user[user_id].event_time)):
#         str1 = user[user_id].event_time[index]
#         ttt = time.strptime(str1, '%Y-%m-%d %H:%M:%S')
#         if ttt.tm_mon == 8 and ttt.tm_mday == 22:
#             print('8/22')
#         else:
#         # print(ttt)
#             week = int((ttt.tm_yday - 2) / 7)
#             slot = week*28 + in_which_slot(ttt)
#             user_slot[int(user_id)][slot] = 1
#         # user_slot[int(user_id)][slot] = 1
#     print(user_id)
    # user_total = int(data['user_id'][len(data)-1]) - int(data['user_id'][0])
    for i in range(len(data)):
        user = data['user_id'][i]
        print(user)
        if user not in usersList:
            usersList.append(user)
        t = data['event_time'][i]
        e_time = t.split('.')[0]
        e_time = time.strptime(e_time, '%Y-%m-%d %H:%M:%S')
        if e_time.tm_mon == 8 and e_time.tm_mday == 22:
            print('8/22')
        else:
            week = int((e_time.tm_yday - 2) / 7)
            slot = week*28 + in_which_slot(e_time)
            user_slot[int(user)][slot] = 1
print('put')
print(len(usersList))
table = pd.DataFrame(user_slot, index=usersList, columns=field_name, dtype=int)
table['user_id'] = usersList
table.set_index('user_id', inplace=True)
# for user_id in usersList:
#     table.at[str(user_id)] = user_slot[int(user_id)]
table.to_csv('train_feature.csv')
