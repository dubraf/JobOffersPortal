from restApi import views
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'jobOffers', views.JobOffersViewSet, basename = 'JobOffers')
router.register(r'jobTags', views.JobTagsViewSet, basename = 'JobTags')
router.register(r'employerProfiles', views.EmployerProfileViewSet, basename = 'EmployerProfiles')
router.register(r'favOffers', views.FavoriteJobOffersViewSet, basename = 'FavoriteOffers')
router.register(r'cv', views.CVViewSet, basename = 'CV')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/', views.RegisterView.as_view()),
]