from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from . import views 

app_name = "tenant"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #path("<int:discussion_id>/post_comment/", views.post_comment , name="post_comment"),
    #path("", views.SearchView.as_view(), name="search"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
