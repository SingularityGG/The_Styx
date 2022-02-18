from django.urls import path
from .views import ScrimDetail, ScrimList, TeamList, TeamDetail

urlpatterns = [
    path("", TeamList.as_view(), name="team_list"),
    path("<int:pk>/", TeamDetail.as_view(), name="team_detail"),
    path("scrim/", ScrimList.as_view(), name = "scrim_list"),
    path("scrim/<int:pk>/", ScrimDetail.as_view(), name="scrim_detail"),
]