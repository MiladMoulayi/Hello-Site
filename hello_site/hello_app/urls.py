from django.contrib import admin
from django.urls import include, path
from hello_app.views import HelloWorldView, HelloView

urlpatterns = [
    path('world/', HelloWorldView.as_view()),
    path('<name>/', HelloView.as_view())
]