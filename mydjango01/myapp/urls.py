from django.urls import path
from . import views

#어떤 주소로 요청이 들어오면, 요청에 대한 뷰를 매핑하는 속성명
urlpatterns = [
  path('', views.index)
]