from django.urls import path
from . import views

urlpatterns=[

    path("blogposts/",views.TestListCreate.as_view(),name="craetblog")
]