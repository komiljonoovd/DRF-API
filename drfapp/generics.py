from rest_framework import generics
from rest_framework.exceptions import ValidationError

from drfapp.models import Teachers, Classes, Parents, Pupils
from drfapp.serializers import TeacherPUTSeriazlier, ClassCreateSerializer, ParentCreateSerializer, \
    TeachersCreateSerializer, PupilsCreateSerializer, ParentsPUTSerializer, PupilsPUTSerializer


class TeacherEditView(generics.UpdateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherPUTSeriazlier
    http_method_names = ['put']

    def perform_update(self, serializer):
        serializer.save(modifiedby=self.request.user.username)


class ClassCreateView(generics.CreateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassCreateSerializer

    # permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        number = serializer.validated_data['number']
        letter = serializer.validated_data['letter']

        if Classes.objects.filter(number=number, letter=letter, isactive=True).exists():
            raise ValidationError({"error": f"Класс {number}-{letter} уже существует ! "})
        if number > 11 or number < 1:
            raise ValidationError({"error": "Классы существуют с 1-го до 11-го  класса !"})

        serializer.save(createdby=self.request.user)


class ParentCreateView(generics.CreateAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentCreateSerializer


class TeachersCreateView(generics.CreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersCreateSerializer


class PupilCreateView(generics.CreateAPIView):
    queryset = Pupils.objects.all()
    serializer_class = PupilsCreateSerializer


class ParentEditView(generics.UpdateAPIView):
    queryset = Parents.objects.all()
    serializer_class = ParentsPUTSerializer
    http_method_names = ['put']

    def perform_update(self, serializer):
        serializer.save(modifiedby=self.request.user.username)


class PupilEditView(generics.UpdateAPIView):
    queryset = Pupils.objects.all()
    serializer_class = PupilsPUTSerializer
    http_method_names = ['put']

    def perform_update(self, serializer):
        serializer.save(modifiedby=self.request.user.username)
