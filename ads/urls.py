from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListAdAPIView.as_view(), name="ad_list"),
    path("create/", views.CreateAdAPIView.as_view(), name="ad_create"),
    path("update/<int:pk>/", views.UpdateAdAPIView.as_view(),
         name="update_ad"),
    path("delete/<int:pk>/", views.DeleteAdAPIView.as_view(),
         name="delete_ad"),
]
