from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Global Variables
PRODUCTION_LIST = {}
COUNT = 0

# Create your views here.
def show_start_page (request):
    params = {
        "boxes": PRODUCTION_LIST
    }
    return render(request,'start.html', params)

def add_production_box(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        component_name = request.POST.get("component_name")
        PRODUCTION_LIST[component_name] = 0
        params = {
            'component_types' : PRODUCTION_LIST
        }
        print(PRODUCTION_LIST)
        return HttpResponseRedirect("/", params)

def perform_add_components(request):
    if request.method != "POST":
        return HttpResponse("Method Not Allowed")
    else:
        quantity = request.POST.get("quantity")
        box_name = request.POST.get("box")
        print(quantity, box_name)
        for key, value in PRODUCTION_LIST.items():
            if key == box_name:
                PRODUCTION_LIST[box_name] = int(value) + int(quantity)
        print(PRODUCTION_LIST)
        return HttpResponseRedirect("/")
