import _1_5_sentSQLM
def vaildRegisterUser(userc, passc, wxidc):
    userFlag = 3
    # 1.4.1 空值检测
    if userc == '' or passc == '':
        return userFlag #输入为空返回3
    # 1.4.2 微信id限制检测
    if not len(wxidc) == 28:
        userFlag = 2
        return userFlag #wxid错误返回2
    else:
        # 1.4.3 传输sql命令
        sqle = "SELECT user FROM `user_list`"
        data = _1_5_sentSQLM.sql_sent(sqle)
        # 1.4.4 用户信息检测
        for row in data:
            username = row[0]
            if username == userc:
                userFlag = 1 #用户名已存在返回3
                return userFlag
        sqle1 = "INSERT INTO `user_list`(`user`, `pass`, `wxid`) VALUES('"
        sqle1 = sqle1 + userc + "','" + passc + "','" + wxidc + "')"
        print (sqle1)
        _1_5_sentSQLM.sql_sent(sqle1)
        userFlag = 0#成功
        return userFlag
