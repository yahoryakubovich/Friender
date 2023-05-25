from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('friends/', FriendListView.as_view(), name='friends'),
    path('establishments/', EstablishmentListView.as_view(), name='establishments'),
    path('hosts/', HostListView.as_view(), name='hosts'),
    path('guests/', GuestListView.as_view(), name='guests'),
    path('user_rating/', UserRatingListView.as_view(), name='user_rating'),
    path('establishment_rating/', EstablishmentRatingListView.as_view(), name='establishment_rating'),
    re_path(r"^user_rating/(?P<id>[\d-]+)$", UserRatingFormView.as_view(), name="user_form_rating"),
    re_path(r"^establishment_rating/(?P<id>[\d-]+)$", establishment_form_rating, name="establishment_form_rating"),
    path('create_user/', UserCreateView.as_view(), name='create_user'),
    path('create_appointment/', create_appointment_form, name='create_appointment'),
    path('make_an_order/', make_an_order, name='make_an_order'),
]
