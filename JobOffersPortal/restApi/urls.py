from restApi import views
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'jobOffers', views.JobOffersViewSet, basename = 'JobOffers')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', views.RegisterView.as_view()),
]