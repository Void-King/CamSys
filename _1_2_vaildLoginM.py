import time

import _1_5_sentSQLM
def vaildLoginUser(userc, passc):
    userFlag = [4,'null']
    # 1.2.1 空值检测
    if userc == '' or passc == '':
        userFlag[0] = 3
        return userFlag #输入为空返回3
    else:
        # 1.2.2 传输sql命令
        sqle = "SELECT * FROM `user_list`"
        data = _1_5_sentSQLM.sql_sent(sqle)
        if not data is None:
            # 1.2.3 用户信息检测
            for row in data:
                username = row[0]
                password = row[1]
                userwxid = row[2]
                if username == userc:
                    if password == passc:
                        userFlag = [0, userwxid]  # 验证成功返回0和wxid
                        strpn = '' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                        sqle = r"INSERT INTO activity_inf VALUES ('" + username + r"', '\
                            " + strpn + r"', '用户登录')"
                        _1_5_sentSQLM.sql_sent(sqle)
                        # print('suc')
                        break
                    else:
                        userFlag[0] = 1  # 密码错误返回1
                        break
                else:
                    userFlag[0] = 2  # 用户不存在返回3
                    continue
            return userFlag
        else:
            return userFlag