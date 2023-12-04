"""
URL configuration for Employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Work.views import EmployeeView,EMPdeptView,BookView,Booklist,LuminarView,Luminarlist,Book_detailView,StudentsView,Book_delete,Studentlist,Students_detailView,Student_delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',EmployeeView.as_view()),
    path('dept/',EMPdeptView.as_view()),
    path('book/',BookView.as_view()),
    path('book/all',Booklist.as_view(),name='book-al'),
    path('luminar/',LuminarView.as_view()),
    path('luminarlist/',Luminarlist.as_view()),
    path("books/<int:pk>",Book_detailView.as_view(),name="book-det"), # name="book-det":aliasing
    # path("marian/",MarianView.as_view()),
    # path("marianlist/",MarianList.as_view()),
    path("std/",StudentsView.as_view()),
    path("book/<int:pk>/remove",Book_delete.as_view(),name='book-del'),
    path('std/all',Studentlist.as_view(),name='std-al'),
    path("std/<int:pk>",Students_detailView.as_view(),name="std-det"),
    path("std/<int:pk>/remove",Student_delete.as_view(),name='std-del'),
]
