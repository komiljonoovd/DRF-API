from django.urls import path

from drfapp import views

urlpatterns = [
    path('Classes/active/', views.ClassViewTrue.as_view(), name='class-view-true'),
    path('Classes/not-active/', views.ClassViewFalse.as_view(), name='claass-view-false'),
    path('Classes/include/Pupils/', views.ClassPupilView.as_view(), name='class-pupil-view'),

    path('Male/pupils/', views.MalePupilsView.as_view(), name='male-pupils-view'),
    path('Female/pupils/', views.FemalePupilsView.as_view(), name='male-pupils-view'),

    path('Teachers/<int:pk>/',views.TeacherIDView.as_view(),name='teacher-id-view'),
    path('Teachers/Classes/', views.TeachersClassesView.as_view(), name='teacher-classes-view'),
    path('Teachers/Deleted/', views.TeacherDeletedView.as_view(), name='deleted-teachers-view'),
    path('Teachers/Not/Deleted/', views.TeacherNotDeletedView.as_view(), name='not-deleted-teachers-view'),

    path('Parents/Deleted/', views.ParentDeletedView.as_view(), name='parent-not-deleted-view'),

    path('Pupils/<int:pk>/', views.PupilIDView.as_view(), name='pupil-id-view'),
    path('Pupils/Deleted/', views.PupilDeletedView.as_view(), name='pupils-deleted-view'),
    path('Pupils/Not/Deleted/', views.PupilNotDeletedView.as_view(), name='pupils-deleted-view'),
    path('Pupils/not-linked-to-class/', views.PupilsNotLinkedView.as_view(), name='not-linked-view'),
    path('Pupils/linked-to-class/', views.PupilsLinkedView.as_view(), name='linked-view'),

]
