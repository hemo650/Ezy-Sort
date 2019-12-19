import requests
import mysql.connector
import json
from mysql.connector import errorcode

apikey = 'KuxAxBfl8w4FvTaNwqwHD3ajxzQBOoyVuaYqRXcgUPKQbtPezCMmxBloThkV3Ico'

cnx = mysql.connector.connect(user='websitedb', password='sql2019')

cursor = cnx.cursor()

DB_NAME = 'test'
exp = ''

i = 0

try:
    cursor.execute("USE {}".format(DB_NAME))  
except mysql.connector.Error as err:
    exit(1)
cnx.commit()


def handleRecieptImage(image):
    map = {}
    URL_post = 'https://api.tabscanner.com/' + apikey + '/process'
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    files = {'receiptImage': image}
    json api processing result
    r = requests.post(url=URL_post, files=files)
    json_data = json.loads(r.text)
    token = json_data['token']
    # receipt json data
    URL_get = 'https://api.tabscanner.com/' + apikey + '/result/' + token
    j = requests.get(url=URL_get)
    result_json = json.loads(j.text)

   #  result_json  = {
   #      "message": "SUCCESS: Result available",
   #      "status": "done",
   #      "status_code": 3,
   #      "result": {
   #    "establishment": "Trader Joes",
   #    "validatedEstablishment": True,
   #    "date": "2015-05-31 22:00:00",
   #    "total": "14.480",
   #    "url": "www.traderjoes.com",
   #    "phoneNumber": "312-951-6369",
   #    "paymentMethod": "",
   #    "address": "Trader Joe'S Chicago, Ontario St, Chicago, IL 60611",
   #    "cash": "0.000",
   #    "change": "0.000",
   #    "alidatedTotal": True,
   #    "subTotal": "14.160",
   #    "validatedSubTotal": True,
   #    "tax": "0.320",
   #    "taxes": [
   #       0.32
   #    ],
   #    "discount": "0.000",
   #    "rounding": "0.000",
   #    "discounts": [],
   #    "lineItems": [
   #       {
   #          "qty": 0,
   #          "desc": "OLIVE OIL POTATO CHIPS",
   #          "unit": "",
   #          "price": "0.000",
   #          "symbols": [],
   #          "discount": "0.000",
   #          "l""ineType": "",
   #          "descClean": "OLIVE OIL POTATO CHIPS",
   #          "lineTotal": "1.990",
   #          "productCode": "",
   #          "customFields": []
   #       },
   #       {
   #          "qty": 0,
   #          "desc": "HUMMUS GARLIC ROASTED EC",
   #          "unit": "",
   #          "price": "0.000",
   #          "symbols": [],
   #          "discount": "0.000",
   #          "lineType": "",
   #          "descClean": "HUMMUS GARLIC ROASTED EC",
   #          "lineTotal": "1.990",
   #          "productCode": "",
   #          "customFields": []
   #       },
   #       {
   #          "qty": 0,
   #          "desc": "CHEDDAR NEW ZEALAND SHARP",
   #          "unit": "",
   #          "price": "0.000",
   #          "symbols": [],
   #          "discount": "0.000",
   #          "lineType": "",
   #          "descClean": "CHEDDAR NEW ZEALAND SHARP",
   #          "lineTotal": "3.710",
   #          "productCode": "",
   #          "customFields": []
   #       },
   #       {
   #          "qty": 5,
   #          "desc": "PITA WHOLE WHEAT 5 ",
   #          "unit": "",
   #          "price": "0.000",
   #          "symbols": [],
   #          "discount": "0.000",
   #          "lineType": "",
   #          "descClean": "PITA WHOLE WHEAT ",
   #          "lineTotal": "1.690",
   #          "productCode": "",
   #          "customFields": []
   #       },
   #       {
   #          "qty": 0,
   #          "desc": "OLIVES MANZANILLA",
   #          "unit": "",
   #          "price": "0.000",
   #          "symbols": [],
   #          "discount": "0.000",
   #          "lineType": "",
   #          "descClean": "OLIVES MANZANILLA",
   #          "lineTotal": "2.290",
   #          "productCode": "",
   #          "customFields": []
   #       },
   #       {
   #          "qty": 0,
   #          "desc": "CREAMY SALTED PEANUT BUTTER",
   #          "unit": "",
   #          "price": "0.000",
   #          "symbols": [],
   #          "discount": "0.000",
   #          "lineType": "",
   #          "descClean": "CREAMY SALTED PEANUT BUTTER",
   #          "lineTotal": "2.490",
   #          "productCode": "",
   #          "customFields": []
   #       }
   #    ],
   #    "summaryItems": [
   #       {
   #          "qty": 0,
   #          "desc": "SUBTOTAL",
   #          "unit": "",
   #          "price": "0.000",
   #          "symbols": [
   #             "$"
   #          ],
   #          "discount": "0.000",
   #          "lineType": "SubTotal",
   #          "descClean": "SUBTOTAL",
   #          "lineTotal": "14.160",
   #          "productCode": "",
   #          "customFields": []
   #       },
   #       {
   #          "qty": 1,
   #          "desc": "STATE TAX 1",
   #          "unit": "",
   #          "price": "0.000",
   #          "symbols": [
   #             "$"
   #          ],
   #          "discount": "0.000",
   #          "lineType": "Tax",
   #          "descClean": "STATE TAX",
   #          "lineTotal": "0.320",
   #          "productCode": "",
   #          "customFields": []
   #       },
   #       {
   #          "qty": 0,
   #          "desc": "TOTAL",
   #          "unit": "",
   #          "price": "0.000",
   #          "symbols": [
   #             "$"
   #          ],
   #          "discount": "0.000",
   #          "lineType": "Total",
   #          "descClean": "TOTAL",
   #          "lineTotal": "14.480",
   #          "productCode": "",
   #          "customFields": []
   #       }
   #    ],
   #    "subTotalConfidence": 0.99,
   #    "taxesConfidence": [
   #       0.99
   #    ],
   #    "discountConfidences": [],
   #    "totalConfidence": 0.99,
   #    "cashConfidence": 0,
   #    "changeConfidence": 0,
   #    "roundingConfidence": 0,
   #    "customFields": {
   #       "URL": "www.traderjoes.com",
   #       "Country": "",
   #       "Currency": "",
   #       "VATNumber": "",
   #       "ExpenseType": "",
   #       "PaymentMethod": "",
   #       "CardLast4Digits": ""
   #    },
   #    "documentType": "receipt",
   #    "currency": "",
   #    "barcodes": [],
   #    "dateISO": "2015-05-31T22:00:00",
   #    "addressNorm": {
   #       "city": "Chicago",
   #       "state": "IL",
   #       "number": "",
   #       "street": "Ontario St",
   #       "suburb": "",
   #       "country": "USA",
   #       "building": "Trader Joe'S",
   #       "postcode": "60611"
   #    },
   #    "expenseType": "None",
   #    "otherData": []
   # },
   # "success": True,
   # "code": 202
# }
    while(result_json['status'] == "pending"):
        j = requests.get(url=URL_get)
        result_json = json.loads(j.text)
    date_result = result_json['result']['date'].split()
    date = date_result[0]
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
        # r1 = requests.post(nutr_url, headers=headers, data=data, json=body)
        # nutr_data = json.loads(r1.text)
        item = items["descClean"]
        # map.append([item, date, exp, nutr_data["foods"][0]["nf_calories"]])
        global i
        i += 1
        # map[str(i)] = {"item_name": item, "pur_date": date, "exp_date": "2019-12-03", "cal": nutr_data["foods"][0]["nf_calories"], "item_id": i}
        map[str(i)] = {"item_name": item, "pur_date": date, "exp_date": "2019-12-03", "cal": 0, "item_id": i}
      #   map.put(i: {"item_name": item, "pur_date": date, "exp_date": exp, "cal": 0, "item_id": i})
      #   map.append([item, date, exp, 0])
    
    return map


def insertToDatabase(map, ls):  
   for key in list(map):
      name = map[key]["item_name"]
      pur_date = map[key]["pur_date"]
      exp_date = map[key]["exp_date"]
      cal = map[key]["cal"]
      item_id = map[key]["item_id"]
      print("item_item: ", item_id, " i: ", i)

      for id in ls:
         print("id: ",id)
         if int(id) == item_id:
            print(type(name), type(pur_date), type(exp_date), type(cal), type(item_id))
            try:

               cursor.execute("INSERT INTO Refridgerator(Item_Name, Purchase_Date, Expiration_Date, Calories, ID_Item) VALUES ('{}','{}','{}','{}','{}')".format(name, pur_date, exp_date, cal, item_id))
               cnx.commit()
            except mysql.connector.Error as err:
               print("Error {}".format(err))

            del map[id]
            ls.remove(id)
            break
   return map


def removeFromDatabase(map, ls):
   print(ls)
   i = 0
   for key in list(map):
      name = map[key]["item_name"]
      pur_date = map[key]["pur_date"]
      exp_date = map[key]["exp_date"]
      cal = map[key]["cal"]
      item_id = map[key]["item_id"]
      print("item_item: ", item_id, " i: ", i)

      for id in ls:
         print("id: ",id)
         if int(id) == item_id:
            print(name, pur_date, exp_date, cal, item_id)
            i -= 1
            del map[id]
            ls.remove(id)
            break
      i += 1
   
   return map


def handleSearchBar(text):

    item = text
    print(item)

    try:
        cursor.execute("USE {}".format(DB_NAME))
        cursor.execute(" SELECT lastName,firstName FROM Custome WHERE ")
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
    
    
def getInventory():
   cursor.execute("SELECT * FROM Refridgerator")
   listOFInventory = cursor.fetchall()
   return listOFInventory