from django.urls import re_path
from routes_ms.views.FavPlaceViews import FavPlaceView, FavPlaceUserView
from routes_ms.views.RecordViews import RecordView, RecordUserView

urlpatterns = [
    re_path('favplace/user', FavPlaceUserView.as_view()),
    re_path('favplace', FavPlaceView.as_view()),
    re_path('record/user', RecordUserView.as_view()),
    re_path('record', RecordView.as_view()),
]