import pymysql
#连接mysql数据库
# REVOKE ALL PRIVILEGES ON *.* FROM 'wxuser'@'%' IDENTIFIED BY 'KeXncyAj';
# GRANT ALL PRIVILEGES ON wxuserdb.* TO 'wxuser'@'%' IDENTIFIED BY 'KeXncyAj';
def sql_sent(sqle):
    db = pymysql.connect("123.207.117.11","wxuser","KeXncyAj","wxuserdb")
    cursor = db.cursor()
    cursor.execute(sqle)
    data = cursor.fetchall()
    db.close()
    return data


