import mysql.connector
import sys
import inspect


specchar= ["'"]


def DB_Connect(host="localhost", user="AppAccess", password="Quebec123", database="testdatabase"):
    db = mysql.connector.connect(
        host=host,
        user=user,
        passwd=password,
        database=database
    )
    return db

def DB_Info(db):
    info = (db.user, db.database, db.server_host, db.server_port)

    return info

def DB_Disconnect(db):
    mycursor = db.cursor()

    return mycursor

def DB_CreateDatabase(db):
    mycursor = db.cursor()
    mycursor.execute("CREATE DATABASE testdatabase")
    DB_answer = mycursor.fetchall()

    return DB_answer

def DB_CreateTable(db, tablename, *headers):
    """
        Explanation: this function takes three arguments: `db`, `tablename` and 'headers'.
        - db is reference for MySQL database connection;
        - tablename is name of table that is going to be implemented;
        - headers are lines that will define headers in table, example 'LastName varchar(255) NOT NULL ' or 'PersonID INT PRIMARY KEY AUTO_INCREMENT';
        """
    #ToDo Add option when table is created to check If new setting need to be adjusted
    mycursor = db.cursor()
    query = "CREATE TABLE " + db.database + '.' + tablename + " ("
    for x in headers:
        query += str(x)
        query += ", "
    query = query[:-2]
    query += ")"
    print(query)
    try:
        mycursor.execute(query)
        DB_answer = mycursor.fetchall()
    except Exception as e:
        error_place = ("File=" + __name__ + " ::Function=" + inspect.currentframe().f_code.co_name +
                       "()::An exception occurred during query execution. Error desc: \n", sys.exc_info()[0])
        error_description = {str(e), e.errno, error_place, query}
        print(error_description)
        return error_description

    return DB_answer

def DB_Select_General(db, tablename, *header):
    mycursor = db.cursor()
    query = "SELECT "
    for x in header:
        query += str(x)
        query += ", "
    if len(header) > 0:
        query = query[:-2]

    query += " FROM " + db.database + '.' + tablename
    print(query)
    try:
        mycursor.execute(query)
        DB_answer = mycursor.fetchall()
    except Exception as e:
        error_place = ("File=" + __name__ + " ::Function=" + inspect.currentframe().f_code.co_name +
                       "()::An exception occurred during query execution. Error desc: \n", sys.exc_info()[0])
        error_description = {str(e), e.errno, error_place, query}
        print(error_description)
        return error_description

    return DB_answer

def DB_Select_Specific(db, tablename, header, *searchcondition):
    mycursor = db.cursor()
    query = "SELECT "
    for x in header:
        query += str(x)
        query += ", "
    if len(header) > 0:
        query = query[:-2]

    query += " FROM " + db.database + '.' + tablename
    print(query)
    try:
        mycursor.execute(query)
        DB_answer = mycursor.fetchall()
    except Exception as e:
        error_place = ("File=" + __name__ + " ::Function=" + inspect.currentframe().f_code.co_name +
                       "()::An exception occurred during query execution. Error desc: \n", sys.exc_info()[0])
        error_description = {str(e), e.errno, error_place, query}
        print(error_description)
        return error_description

    return DB_answer

def DB_Insert(db, tablename, *data):
    """Function Insert is to insert into DB record. data is values ordered in table order.\n
    Function will take tablename, list all columns read from DB and place them into INSERT instruction with data values\n
    #mycursor.execute("INSERT INTO %s (name, age) VALUES(%s,%s)", (tablename, data[0], data[1]))"""
    DB_tablename = db.database + '.' + tablename
    mycursor = db.cursor()
    mycursor.execute("Describe " + tablename, params=None, multi=True)
    DB_answer = mycursor.fetchall()
    #if len(data) != mycursor.arraysize:
        #ERROR
        #length of table and datas do not match
    #    return 0

    query = "INSERT INTO " + DB_tablename + " ("
    i = 0
    try:
        for x in DB_answer:
            if x[0].lower() != tablename.lower() + "id" and i <= len(data[0]):
                query += x[0] + ", "
            i += 1
    except Exception as e:
        error_place = ("File=" + __name__ + " ::Function=" + inspect.currentframe().f_code.co_name +
                       "()::An exception occurred during query creation. Error desc: \n", sys.exc_info()[0])
        error_description = {str(e), e.errno, error_place}
        print(error_description)
        return error_description
    if len(DB_answer) > 0:
        query = query[:-2]
    query += ") "

    query += "VALUES("
    for x in data[0]:
        if type(x) is str:
            for y in specchar:
                pos = x.find(y)
                if pos > -1:
                    x = x[:pos] + '"' + x[pos + 1:]
            query += "'" + str(x) + "'"
        elif type(x) is int:
            query += str(x)
        query += ", "
    if len(data) > 0:
        query = query[:-2]
    query += ") "

    #mycursor.execute("INSERT INTO %s (name, age) VALUES(%s,%s)", (tablename, data[0], data[1]))
    mycursor.execute("USE " + db.database)
    print(query)
    try:
        mycursor.execute(query)
        DB_answer = mycursor.fetchall()
    except Exception as e:
        error_place = ("File=" + __name__ + " ::Function=" + inspect.currentframe().f_code.co_name +
                       "()::An exception occurred during query execution. Error desc: \n", sys.exc_info()[0])
        error_description = {str(e), e.errno, error_place, query}
        print(error_description)
        return error_description
    db.commit()

    return DB_answer

def DB_Update(db, tablename, name, *data):
    """Function Update is to insert into DB record. data is values ordered in table order.\n
    Function will take tablename, list all columns read from DB and place them into INSERT instruction with data values\n
    #mycursor.execute(UPDATE testdatabase.tablename SET data[x] = data[x+1],... WHERE Name=name"""
    DB_tablename = db.database + '.' + tablename
    mycursor = db.cursor()
    mycursor.execute("Describe " + tablename, params=None, multi=True)
    DB_answer = mycursor.fetchall()

    query = "UPDATE " + DB_tablename + " SET "
    i = 1
    try:
        for x in DB_answer:
            if x[0].lower() != tablename.lower() + "id" and x[0].lower() != "name":
                query += x[0] + "="
                if i < len(data[0]):
                    if x[1] == b'int':
                        query += str(data[0][i]) + ", "
                    else:
                        query += "'" + str(data[0][i]) + "', "
                else:
                    query += """Null, """
                i += 1
    except Exception as e:
        error_place = ("File=" + __name__ + " ::Function=" + inspect.currentframe().f_code.co_name +
                       "()::An exception occurred during query creation. Error desc: \n", sys.exc_info()[0])
        error_description = {str(e), e.errno, error_place}
        print(error_description)
        return error_description
    if len(DB_answer) > 0:
        query = query[:-2]


    query += " WHERE Name='" + str(name) + "'"

    #mycursor.execute("INSERT INTO %s (name, age) VALUES(%s,%s)", (tablename, data[0], data[1]))
    mycursor.execute("USE " + db.database)
    print(query)
    try:
        mycursor.execute(query)
        DB_answer = mycursor.fetchall()
    except Exception as e:
        error_place = ("File=" + __name__ + " ::Function=" + inspect.currentframe().f_code.co_name +
                       "()::An exception occurred during query execution. Error desc: \n", sys.exc_info()[0])
        error_description = {str(e), e.errno, error_place, query}
        print(error_description)
        return error_description
    db.commit()

    return DB_answer

def DB_Delete(db, tablename, name):
    """Function Update is to insert into DB record. data is values ordered in table order.\n
    Function will take tablename, list all columns read from DB and place them into INSERT instruction with data values\n
    #mycursor.execute(UPDATE testdatabase.tablename SET data[x] = data[x+1],... WHERE Name=name"""
    DB_tablename = db.database + '.' + tablename
    mycursor = db.cursor()
    mycursor.execute("Describe " + tablename, params=None, multi=True)
    DB_answer = mycursor.fetchall()

    query = "DELETE FROM " + DB_tablename
    i = 1
    query += " WHERE Name='" + str(name) + "'"

    #mycursor.execute("DELETE FROM somelog WHERE user = 'jcole')
    mycursor.execute("USE " + db.database)
    print(query)
    try:
        mycursor.execute(query)
        DB_answer = mycursor.fetchall()
    except Exception as e:
        error_place = ("File=" + __name__ + " ::Function=" + inspect.currentframe().f_code.co_name +
                       "()::An exception occurred during query execution. Error desc: \n", sys.exc_info()[0])
        error_description = {str(e), e.errno, error_place, query}
        print(error_description)
        return error_description
    db.commit()

    return DB_answer

def DB_ExistsRow(db, tablename, name):
    """Function DB_ExistsRow is to check into DB record. data is values ordered in table order.\n
    Function will take tablename, list all columns read from DB and place them into INSERT instruction with data values\n
    #mycursor.execute(SELECT EXISTS(SELECT * FROM testdatabase.tablename WHERE Name="name")"""
    DB_tablename = db.database + '.' + tablename
    mycursor = db.cursor()

    query = "SELECT EXISTS(SELECT * FROM " + DB_tablename
    i = 0
    #check if name has special characters that need to be marked

    for x in specchar:
        pos = name.find(x)
        if pos > -1:
            name = name[:pos] + '"' + name[pos+1:]

    query += " WHERE Name='" + str(name) + "')"

    #mycursor.execute("SELECT EXISTS(SELECT * FROM testdatabase.plan WHERE Name="Sprinkler_v10")))
    mycursor.execute("USE " + db.database)
    print(query)
    try:
        mycursor.execute(query)
        DB_answer = mycursor.fetchall()
    except Exception as e:
        error_place = ("File=" + __name__ + " ::Function=" + inspect.currentframe().f_code.co_name +
                       "()::An exception occurred during query execution. Error desc: \n", sys.exc_info()[0])
        error_description = {str(e), e.errno, error_place, query}
        print(error_description)
        return error_description
    db.commit()

    return DB_answer

def DB_CursorPrint(mycursor):
    print("Mycursor Start")
    if not isinstance(mycursor, set):
        for x in mycursor:
            print(x)
        print("Mycursor End\n")

#DB_Insert(db, "Person", 'jerry', 82)
#DB_Insert(db, "Person", 'Jo mama is so fat', 999)
#mycursor = DB_Select_General(db, "Person", "name", "age", "personID")
#DB_CursorPrint(mycursor)

#DB_Insert(db, "Person", "Janusz", 300)

#mycursor = DB_Select_General(db, "Person", "name", "age", "personID")
#DB_CursorPrint(mycursor)

#DB_CreateTable(db, "Pizza", "pizzaID INT Primary Key AUTO_INCREMENT", "name varchar(100)", "description text", "calories int")
#DB_Insert(db,"Pizza", "Margarita", "Simples Pizza to made, only cace and souce", 200)

#mycursor = DB_Select_General(db, "Pizza", "*")
#DB_CursorPrint(mycursor)