from django.urls import path
from blog import views


urlpatterns = [
    path("", views.get_hello),
    path("blogs/", views.index_page),
    path("blogs/<int:pk>/", views.detail_page, name="detail"),
]