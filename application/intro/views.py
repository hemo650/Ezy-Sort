from django.shortcuts \
    import HttpResponse, render
import json
import requests
import mysql.connector
from mysql.connector import errorcode
import re

from .forms import ReceiptForm, SearchForm
from .handlers import handleRecieptImage, handleSearchBar

DB_NAME = 'test'
table_description = "CREATE TABLE Refridgerator (Item_Name VARCHAR(100), ",
"Purchase_Date DATE, Expiration_Date DATE, Calories INT)"

apikey = 'KuxAxBfl8w4FvTaNwqwHD3ajxzQBOoyVuaYqRXcgUPKQbtPezCMmxBloThkV3Ico'

cnx = mysql.connector.connect(user='websitedb', password='sql2019')
cursor = cnx.cursor()

total_calorie = 0  # total refridgerator calorie


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
    return render(request, 'webpage/Welcome.html')


def profile_page(request):
    return render(request, 'webpage/profile.html')


def home_page(request):
    return render(request, 'webpage/home.html')


def refrigerator(request):
    return render(request, 'webpage/refrigerator.html')


def shoppingList(request):
    return render(request, 'webpage/ShoppingList.html')


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))


def addItem(request):

    cnx = mysql.connector.connect(user='websitedb', password='sql2019')
    cursor = cnx.cursor()

    if 'upload' in request.POST:
        form = ReceiptForm(request.POST, request.FILES)
        if form.is_valid():
            print("valid")
            img = form.cleaned_data['img']
            print(img.image)
            handleRecieptImage(img)
    elif 'search' in request.POST:
        form = SearchForm(request.POST)
        if form.is_valid():
            print("valid")
            word = form.cleaned_data['item']
            print(word)
    else:
        form = {}


    #if 'upload' in request.POST and request.FILES['myfile']:

        # try:
        #     cursor.execute("USE {}".format(DB_NAME))
        #     cursor.execute("SELECT * FROM Refridgerator")
        #     table = cursor.fetchall()
        #     for items in table:
        #         print(items)
        # except mysql.connector.Error as err:
        #     print("Table {} does not exists.".format(DB_NAME))
        #     exit(1)
        # s = {}
        # # Tabscanner API post endpoint
        # URL_post = 'https://api.tabscanner.com/' + apikey + '/process'

        # myImage = request.FILES['myfile']  # uploaded image
        # headers = {'content-type': 'application/x-www-form-urlencoded'}
        # files = {'receiptImage': myImage}
        # # json api processing result
        # r = requests.post(url=URL_post, files=files)
        # json_data = json.loads(r.text)
        # token = json_data['token']
        # # receipt json data
        # URL_get = 'https://api.tabscanner.com/' + apikey + '/result/' + token
        # j = requests.get(url=URL_get)
        # result_json = json.loads(j.text)
        # while(result_json['status'] == "pending"):
        #     j = requests.get(url=URL_get)
        #     result_json = json.loads(j.text)
        # # Select the Database which we need
        # try:
        #     cursor.execute("USE {}".format(DB_NAME))
        # except mysql.connector.Error as err:
        #     print("Database {} does not exists.".format(DB_NAME))
        #     if err.errno == errorcode.ER_BAD_DB_ERROR:
        #         create_database(cursor)
        #         print("Database {} created successfully.".format(DB_NAME))
        #         cnx.database = DB_NAME
        #     else:
        #         print(err)
        #         exit(1)
        # try:
        #     cursor.execute(table_description)
        # except mysql.connector.Error as err:
        #     if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        #         print("already exists.")

        # for items in result_json['result']['lineItems']:
        #     nutr_url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
        #     headers = {
        #         'x-app-id': '5e5a70f8',
        #         'x-app-key': '247d06b35f3d414d67179247f2b5287c',
        #         'x-remote-user-id': '0',
        #         'accept': 'application/json'
        #             }
        #     body = {
        #         "query": "string",
        #         "num_servings": 1,
        #         "aggregate": "string",
        #         "line_delimited": False,
        #         "use_raw_foods": False,
        #         "include_subrecipe": False,
        #         "timezone": "string",
        #         "consumed_at": "string",
        #         "lat": 0,
        #         "lng": 0,
        #         "meal_type": 0,
        #         "use_branded_foods": True,
        #         "locale": "string"
        #             }

        #     data = {'query': items["descClean"]}
        #     r1 = requests.post(nutr_url, headers=headers, data=data, json=body)
        #     nutr_data = json.loads(r1.text)
        #     output = re.sub('[^A-Za-z]+', ' ', items["descClean"])
        #     print(output)
        #     try:
        #         cursor.execute("INSERT INTO Refridgerator",
        #                        "(Item_Name, Purchase_Date, ",
        #                        "Expiration_Date, Calories) ",
        #                        "VALUES ('{}','9999-12-30', '9999-12-31', {})"
        #                        .format(output, nutr_data["foods"][0][
        #                         "nf_calories"]))
        #     except KeyError as err:
        #         print(err)
        # cnx.commit()
        # cursor.close()
        # cnx.close()
    if 'search' in request.POST:

        result_json = {}

        cnx = mysql.connector.connect(user='websitedb', password='sql2019')

        cursor = cnx.cursor()

        item = request.POST.get('myItem')
        print(item)

        try:
            cursor.execute("USE {}".format(DB_NAME))

            cursor.execute("SELECT EXISTS(SELECT * from Refridgerator WHERE ",
                           "Item_Name='{}') 'utf8'".format(item))
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
    cnx = mysql.connector.connect(user='websitedb', password='sql2019')
    cursor = cnx.cursor()

    try:
        cursor.execute("USE {}".format(DB_NAME))
        cursor.execute("SELECT * FROM Refridgerator")
        table = cursor.fetchall()
        for items in table:
            print(items)
    except mysql.connector.Error as err:
        print("Table {} does not exists.".format(DB_NAME))
        exit(1)

    cnx.commit()
    cursor.close()
    cnx.close()
    return render(request, 'webpage/addItem.html', {'form': form})


def searchbar(request):

    form = SearchForm(request.POST)
    if form.is_valid():
        txt = form.cleaned_data['item']
        print(txt)
        handleSearchBar(txt)
        
    return render(request, 'webpage/addItem.html', {'searchform': form})
