from django.shortcuts \
    import HttpResponse, render


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