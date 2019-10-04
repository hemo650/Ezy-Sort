from django.shortcuts \
    import HttpResponse, render
import json
import requests


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

def Login(request):
    return render(request, 'intro/Login.html')

def addItem(request):
    if request.method == 'POST' and request.FILES['myfile']:
        URL_post = 'https://api.tabscanner.com/KuxAxBfl8w4FvTaNwqwHD3ajxzQBOoyVuaYqRXcgUPKQbtPezCMmxBloThkV3Ico/process'
        myImage = request.FILES['myfile']
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        # imageArray = np.array(myImage)
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
        print(j.text)

    if request.method == 'GET':
        result_json = {}
    return render(request, 'intro/addPage.html', {'list': result_json})