# import _1_5_sentSQLM
# import _2_5_wxSentM
# import time
# while True:
#     atk = '20_a17yWRROOK1wZkfIN-cqKT1libEpIY7hm8VW72yf5bQmPgMM_PFNkQiXdndQefkQfdQtBlWqGzkwzb2OdDDLMOzT7TEyRJ-m9VWkHC7yJgr2J3sxDZM3hAl-YVhiy8Ct0RvK-M1WRxXpTx0KVERcABAOXK'
#     wxid = 'o__Cr1Y4gVbFpJv18yUdHN7cr4RI'
#     sql = "SELECT * FROM `user_list` WHERE `wxid`=\'" + wxid + "\'"
#     data = _1_5_sentSQLM.sql_sent(sql)
#     times = data[0][3]
#     request = data[0][4]
#     print (data)
#     print (str(times))
    
#     print (request)
#     if request == 1:
#         _2_5_wxSentM.setm2user(wxid, atk, 'tpfs')
#         times += 1
#         sql = '''UPDATE `user_list`
#             SET `times` = \'''' + str(times) + '''\',`request` = '0'
#             WHERE `wxid` = \'''' + wxid + '''\';
#             '''
#         _1_5_sentSQLM.sql_sent(sql)
#         print ('ok')
#     time.sleep(2)
a = []
a.append(1)
a.append(2)
print (len(a))
