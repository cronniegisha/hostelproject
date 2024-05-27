from django.urls import path
from .views import *

urlpatterns = [
    path('', AllRoomsListView.as_view(), name='all-room-list'),
    path('rooms/add/', RoomListCreateView.as_view(), name='room-list-create'),
    path('rooms/all/', AllRoomsListView.as_view(), name='all-room-list'), 
    path('rooms/update/<int:pk>/', RoomUpdateView.as_view(), name='room-update'),  
    path('rooms/delete/<int:pk>/', RoomDeleteView.as_view(), name='room-delete'), 
    path('protected-class/',ProtectedView.as_view(), name='protected_class'),
    path('protected-function/', protected_function_view, name='protected_function'),
]
