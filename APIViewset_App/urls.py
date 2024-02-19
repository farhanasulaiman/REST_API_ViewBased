from rest_framework.routers import SimpleRouter

from APIViewset_App import views

router = SimpleRouter()
router.register('studentapi', views.StudentViewset, basename='student')
urlpatterns = router.urls
