import requests
import mysql.connector
import json
from mysql.connector import errorcode

apikey = 'KuxAxBfl8w4FvTaNwqwHD3ajxzQBOoyVuaYqRXcgUPKQbtPezCMmxBloThkV3Ico'

cnx = mysql.connector.connect(user='websitedb', password='sql2019')

cursor = cnx.cursor()

DB_NAME = 'test'


try:
    cursor.execute("USE {}".format(DB_NAME))  
except mysql.connector.Error as err:
    exit(1)


def handleRecieptImage(image):

    URL_post = 'https://api.tabscanner.com/' + apikey + '/process'
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    files = {'receiptImage': image}
    # json api processing result
    r = requests.post(url=URL_post, files=files)
    json_data = json.loads(r.text)
    token = json_data['token']
    # receipt json data
    URL_get = 'https://api.tabscanner.com/' + apikey + '/result/' + token
    j = requests.get(url=URL_get)
    result_json = json.loads(j.text)
    while(result_json['status'] == "pending"):
        j = requests.get(url=URL_get)
        result_json = json.loads(j.text)

    for items in result_json['result']['lineItems']:
        nutr_url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
        headers = {
            'x-app-id': '5e5a70f8',
            'x-app-key': '247d06b35f3d414d67179247f2b5287c',
            'x-remote-user-id': '0',
            'accept': 'application/json'
                }
        body = {
            "query": "string",
            "num_servings": 1,
            "aggregate": "string",
            "line_delimited": False,
            "use_raw_foods": False,
            "include_subrecipe": False,
            "timezone": "string",
            "consumed_at": "string",
            "lat": 0,
            "lng": 0,
            "meal_type": 0,
            "use_branded_foods": True,
            "locale": "string"
                }

        data = {'query': items["descClean"]}
        r1 = requests.post(nutr_url, headers=headers, data=data, json=body)
        nutr_data = json.loads(r1.text)
    print("Handled Reciept Image")


def handleSearchBar(text):

    item = text
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
    
    
