from django.shortcuts \
    import HttpResponse, render
import json
import requests
import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'test'

table_description = "CREATE TABLE Refridgerator (Item_Name VARCHAR(100), Purchase_Date DATE, Expiration_Date DATE, Calories INT)"


def index(request):
    return render(request, 'intro/welcome.html')

def anne(request):
    return render(request, 'intro/anne.html')

def abdi(request):
    return render(request, 'intro/abdi.html')

def carolyn(request):
    return render(request, 'intro/carolyn.html')

def ibrahim(request):
    return render(request, 'intro/ibrahim.html')

def john(request):
    return render(request, 'intro/john.html')

def surabhi(request):
    return render(request, 'intro/surabhi.html')

def tianrong(request):
    return render(request, 'intro/tianrong.html')

def Note1(request):
    return render(request, 'intro/Note1.html')

def Note2(request):
    return render(request, 'intro/Note2.html')

def Note3(request):
    return render(request, 'intro/Note3.html')

def main_page(request):
    return render(request, 'webpage/main.html')

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)


def addItem(request):

    cnx = mysql.connector.connect(user='websitedb', password='sql2019')
    cursor = cnx.cursor()



    if 'upload' in request.POST:
        s = {}
        URL_post = 'https://api.tabscanner.com/KuxAxBfl8w4FvTaNwqwHD3ajxzQBOoyVuaYqRXcgUPKQbtPezCMmxBloThkV3Ico/process'
        myImage = request.FILES['myfile']
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        files = {'receiptImage': myImage}
        r = requests.post(url=URL_post, files=files)
        json_data = json.loads(r.text)
        token = json_data['token']
        URL_get = 'https://api.tabscanner.com/KuxAxBfl8w4FvTaNwqwHD3ajxzQBOoyVuaYqRXcgUPKQbtPezCMmxBloThkV3Ico/result/' + token
        j = requests.get(url=URL_get)
        result_json = json.loads(j.text)
        while(result_json['status'] == "pending"):
            print("pending")
            j = requests.get(url=URL_get)
            result_json = json.loads(j.text)

        try:
            cursor.execute("USE {}".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                create_database(cursor)
                print("Database {} created successfully.".format(DB_NAME))
                cnx.database = DB_NAME
            else:
                print(err)
                exit(1)
        try:
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")

        for items in result_json['result']['lineItems']:
            cursor.execute("INSERT INTO Refridgerator (Item_Name, Purchase_Date, Expiration_Date, Calories) VALUES ('{}','9999-12-30', '9999-12-31', 0)".format(items["descClean"]))
            print(items["descClean"])
        #print(j.text)

        cnx.commit()
        cursor.close()
        cnx.close()

        

    if 'search' in request.POST:

        result_json = {}
        cnx = mysql.connector.connect(user='websitedb', password='sql2019')

        cursor = cnx.cursor()

        item = request.POST.get('myItem')
        print(item)

        try:
            cursor.execute("USE {}".format(DB_NAME))

            cursor.execute("SELECT EXISTS(SELECT * from Refridgerator WHERE Item_Name='{}') 'utf8'".format(item))
            row = cursor.fetchone()

            if row[0] == 1:
                print("Found")
                s = {'search_result': "Item was Found"}
                txt = json.dumps(s)
                search = json.loads(txt)
            else:
                print("Not Found")
                s = {'search_result': "Item was Not Found"}
                txt = json.dumps(s)
                search = json.loads(txt)
        except mysql.connector.Error as err:
            print("Error {}".format(err))


        cursor.close()
        cnx.close()


    if request.method == 'GET':
        result_json = {}
        s = {}
        txt = ""

    return render(request, 'intro/addPage.html',{'list2': s} , {'list': result_json} )