from django.shortcuts \
    import HttpResponse, render, redirect
import json
import requests
import mysql.connector
from mysql.connector import errorcode
import re

from django_tables2 import RequestConfig
from .forms import ReceiptForm, SearchForm, RegisterForm
from .handlers import handleRecieptImage, handleSearchBar, insertToDatabase, removeFromDatabase, getInventory
from .tables import ItemTable

DB_NAME = 'test'
table_description = "CREATE TABLE Refridgerator (Item_Name VARCHAR(100), ",
"Purchase_Date DATE, Expiration_Date DATE, Calories INT, Quantity INT)"

apikey = 'KuxAxBfl8w4FvTaNwqwHD3ajxzQBOoyVuaYqRXcgUPKQbtPezCMmxBloThkV3Ico'

cnx = mysql.connector.connect(user='websitedb', password='sql2019')
cursor = cnx.cursor()
total_calorie = 0  # total refridgerator calorie
scannedItems = {}


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


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})


def inventory(request):

    inventoryTable = getInventory()

    return render(request, 'webpage/refrigerator.html', {'inventory': inventoryTable})


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))


def removeItem(request):
    return render(request, 'webpage/removeItem.html')


def addItem(request):
    cnx = mysql.connector.connect(user='websitedb', password='sql2019')
    cursor = cnx.cursor()
    global scannedItems
    form = ReceiptForm(request.POST, request.FILES)
    # form = ReceiptForm(request.POST, request.FILES)
    # table = ItemTable(scannedItems)
    # RequestConfig(request).configure(table)
    if 'upload' in request.POST:
        print("Upload")
        print(len(scannedItems))
        form = ReceiptForm(request.POST, request.FILES)

        if form.is_valid():
            img = form.cleaned_data['img']
            # print(img.image)
            scannedItems = handleRecieptImage(img)
            # table = ItemTable(scannedItems)
            # print(scannedItems[0]['pur_date'])
            # return redirect('res/search', request, scannedItems)
    if "insert" in request.POST:

        # listOfInputs = request.POST.getlist('scales')
        scannedItems = insertToDatabase(scannedItems, request.POST.getlist('boxes'))

    if 'delete' in request.POST:
        scannedItems = removeFromDatabase(scannedItems, request.POST.getlist('boxes'))
    # if 'search' in request.POST:

    #     result_json = {}

    #     cnx = mysql.connector.connect(user='websitedb', password='sql2019')

    #     cursor = cnx.cursor()

    #     item = request.POST.get('myItem')
    #     print(item)

    #     try:
    #         cursor.execute("USE {}".format(DB_NAME))

    #         cursor.execute("SELECT EXISTS(SELECT * from Refridgerator WHERE ",
    #                        "Item_Name='{}') 'utf8'".format(item))
    #         row = cursor.fetchone()

    #         if row[0] == 1:
    #             print("Found")
    #             s = {'search_result': "Item was Found"}
    #             txt = json.dumps(s)
    #             search = json.loads(txt)
    #         else:
    #             print("Not Found")
    #             s = {'search_result': "Item was Not Found"}
    #             txt = json.dumps(s)
    #             search = json.loads(txt)
    #     except mysql.connector.Error as err:
    #         print("Error {}".format(err))
    #     cursor.close()
    #     cnx.close()
    # cnx = mysql.connector.connect(user='websitedb', password='sql2019')
    # cursor = cnx.cursor()

    # try:
    #     cursor.execute("USE {}".format(DB_NAME))
    #     cursor.execute("SELECT * FROM Refridgerator")
    #     table = cursor.fetchall()
    #     for items in table:
    #         print(items)
    # except mysql.connector.Error as err:
    #     print("Table {} does not exists.".format(DB_NAME))
    #     exit(1)

    # cnx.commit()
    # cursor.close()
    # cnx.close()
    # print(scannedItems)
    return render(request, 'webpage/addItem.html', {'form': form, 'scannedItems': scannedItems})


def showItems(request, dic):
    print("showItems")
    for row in dic:
        insertToDatabase(row[0], row[1], row[2], row[3])
    addItem.scannedItems.clear()
    return redirect('addItem')


def searchbar(request):
    # form = SearchForm(request.POST)
    # if form.is_valid():
    #     txt = form.cleaned_data['item']
    #     print(txt)
    #     handleSearchBar(txt)
    search_item = request.POST['searchroleName']

    search_details = handleSearchBar(search_item)

    return render(request, 'webpage/addItem.html', )
