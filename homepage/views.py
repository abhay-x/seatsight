from django.shortcuts import render

# Create your views here. //controllers
# these mtds called from urls.py[controller?] with param HttpRequest
def home(request):
    # render mtd takes param HttpRequest,template,context and return HttpResponse
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")
