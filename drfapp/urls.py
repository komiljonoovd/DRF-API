from django.urls import path, include
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
import drfapp.generics
from . import views

urlpatterns = [
    path('Classes/', drfapp.generics.ClassCreateView.as_view(), name='class-create-view'),
    path('Classes/Delete/<int:pk>/',views.ClassDeleteView.as_view(),name='class-delete-view'),
    path('Classes/Edit/<int:pk>/', drfapp.generics.ClassEditView.as_view(), name='class-edit-view'),
    path('Classes/active/', views.ClassViewTrue.as_view(), name='class-view-true'),
    path('Classes/not-active/', views.ClassViewFalse.as_view(), name='claass-view-false'),
    path('Classes/include/Pupils/', views.ClassPupilView.as_view(), name='class-pupil-view'),

    path('Teachers/', drfapp.generics.TeachersCreateView.as_view(), name='teachers-create-view'),
    path('Teachers/Edit/<int:pk>/', drfapp.generics.TeacherEditView.as_view(), name='teacher-edit-view'),
    path('Teachers/Delete/<int:pk>/', views.TeacherstDeleteView.as_view(), name='teachers-delete-view'),
    path('Teachers/<int:pk>/', views.TeacherIDView.as_view(), name='teacher-id-view'),
    path('Teachers/Classes/', views.TeachersClassesView.as_view(), name='teacher-classes-view'),
    path('Teachers/Deleted/', views.TeacherDeletedView.as_view(), name='deleted-teachers-view'),
    path('Teachers/Not/Deleted/', views.TeacherNotDeletedView.as_view(), name='not-deleted-teachers-view'),

    path('Parents/', drfapp.generics.ParentCreateView.as_view(), name='parent-create-view'),
    path('Parents/Edit/<int:pk>/', drfapp.generics.ParentEditView.as_view(), name='pupil-edit-view'),
    path('Parents/Delete/<int:pk>', views.ParentDeleteView.as_view(), name='parent-delete-view'),
    path('Parents/Deleted/', views.ParentDeletedView.as_view(), name='parent-deleted-view'),
    path('Parents/Not/Deleted/', views.ParentsNotDeletedView.as_view(), name='parent-not-deleted-view'),

    path('Pupils/', drfapp.generics.PupilCreateView.as_view(), name='pupil-create-view'),
    path('Pupils/Delete/<int:pk>/', views.PupilDeleteView.as_view(), name='pupil-delete-view'),
    path('Pupils/Edit/<int:pk>/', drfapp.generics.PupilEditView.as_view(), name='pupil-edit-view'),
    path('Pupils/male/', views.MalePupilsView.as_view(), name='male-pupils-view'),
    path('Pupils/female/', views.FemalePupilsView.as_view(), name='male-pupils-view'),
    path('Pupils/<int:pk>/', views.PupilIDView.as_view(), name='pupil-id-view'),
    path('Pupils/Deleted/', views.PupilDeletedView.as_view(), name='pupils-deleted-view'),
    path('Pupils/Not/Deleted/', views.PupilNotDeletedView.as_view(), name='pupils-deleted-view'),
    path('Pupils/not-linked-to-class/', views.PupilsNotLinkedView.as_view(), name='not-linked-view'),
    path('Pupils/linked-to-class/', views.PupilsLinkedView.as_view(), name='linked-view'),

    path('auth/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]