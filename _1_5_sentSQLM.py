import pymysql
import os
#连接mysql数据库
# REVOKE ALL PRIVILEGES ON *.* FROM 'wxuser'@'%' IDENTIFIED BY 'KeXncyAj';
# GRANT ALL PRIVILEGES ON wxuserdb.* TO 'wxuser'@'%' IDENTIFIED BY 'KeXncyAj';
def sql_sent(sqle):
    try:
        db = pymysql.connect("123.207.117.11", "wxuser", "KeXncyAj", "wxuserdb")
        # print(db)
        cursor = db.cursor()
        cursor.execute(sqle)
        if sqle[:6] == 'SELECT':
            data = cursor.fetchall()
            return data
        elif sqle[:6] == 'INSERT':
            db.commit()
        elif sqle[:6] == 'UPDATE':
            db.commit()
        else:
            pass
        db.close()
    except:
        # print ('Program wrong 2')
        log = open(r'./wronglog.ini', 'a')
        log.write('Program wrong 2\n')
        log.close()
# sql_sent('123')
# sql = '''UPDATE `user_list`
# SET `times` = '0',`request` = '1'
# WHERE `wxid` = \'''' + wxid + '''\';
# '''
# print (sql)
# print ('safd')
# sql_sent(sql)