import mysql
def user_check(userc, passc):
    userflag = [0,"null"]
    #连接mysql得到用户表["user", "pass", "wxid"]
    sqle = "SELECT * FROM `user_list`"
    data = mysql.sql_sent(sqle)
    for row in data:
        username = row[0]
        password = row[1]
        userwxid = row[2]
        if username == userc:
            if password == passc:
                userflag = [1,userwxid]
                break
            else:
                continue
        else:
            continue
    return userflag