from django.urls import path
from . import views

app_name = 'schools_app'

urlpatterns = [
    path('school/list',views.SchoolListView.as_view(),name='school_list'),
    path('school/detail/<int:pk>/',views.SchoolDetailView.as_view(),name='school_detail'),
    path('school/create/',views.SchoolCreateView.as_view(),name='school_create'),
    path('school/update/<int:pk>/',views.SchoolUpdateView.as_view(),name='school_update'),
    path('school/delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='school_delete')
]
