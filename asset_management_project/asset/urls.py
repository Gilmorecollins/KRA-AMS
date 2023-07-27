from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DepartmentDetail, DepartmentList, StationListCreateAPIView, StationRetreiveUpdateDestroyAPIView, SectionList, SectionDetail

urlpatterns = [
    path('department/', DepartmentList.as_view(), name='department-list-create'),
    path('department/<int:pk>/', DepartmentDetail.as_view(), name='department-retrieve-update-destroy'),
    
    path('station/', StationListCreateAPIView.as_view(), name='station-list-create'),
    path('station/<int:pk>/', StationRetreiveUpdateDestroyAPIView.as_view(), name='station-retrieve-update-destroy'),

    path('section/', SectionList.as_view(), name='section-list-create'),
    path('section/<int:pk>/', SectionDetail.as_view(), name='section-retrieve-update-destroy')
]

urlpatterns = format_suffix_patterns(urlpatterns)