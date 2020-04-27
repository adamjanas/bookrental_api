from django.urls import path, include
from . import views
from rest_framework import routers



router = routers.DefaultRouter()
router.register('books', views.BookView, basename="books")
router.register('kinds', views.KindView)
router.register('readers', views.ReaderView)

urlpatterns = router.urls

