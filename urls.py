
from django.urls import path 
from . import views


'''def hello(request:HttpRequest):
    return HttpResponse (f"hello {name}")'''

'''def hello(reqest:HttpRequest):
    return render(reqest,"greet/greeting.html")'''


urlpatterns=[
    #path{'hello/<str:name>/', view.hello, name="hello"),
    path('hello/', views.hello, name="hello")
]