from django.urls import path
from .views import DepartmentDetail, DepartmentList, StationListCreateAPIView, StationRetreiveUpdateDestroyAPIView

urlpatterns = [
    path('department/', DepartmentList.as_view(), name='department-list-create'),
    path('department/<int:pk>/', DepartmentDetail.as_view(), name='department-retrieve-update-destroy'),
    path('station/', StationListCreateAPIView.as_view(), name='station-list-create'),
    path('station/<int:pk>/', StationRetreiveUpdateDestroyAPIView.as_view(), name='station-retrieve-update-destroy'),
]