from pymysql.cursors import DictCursor
def user_return(isim="None",data=None,mysql=""):
    db = mysql.connect()
    cursor = db.cursor(cursor=DictCursor)
    query_string = "SELECT * FROM eticaret LIMIT 2"
    cursor.execute(query_string)
    data = cursor.fetchall()
    return data


