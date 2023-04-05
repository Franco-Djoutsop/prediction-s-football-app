from django.urls import path
from .views import UserDetailApi,SignUpApiView


#|_________________________________________________________________________________|
#|  les differents endpoints grace auxquels on a access aux infos sur formats json |
#|_________________________________________________________________________________|


urlpatterns = [
  path("get-details",UserDetailApi.as_view()),
  path('register',SignUpApiView.as_view()),
]