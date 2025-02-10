from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from drfapp.models import Teachers, Classes, Parents, Pupils
from drfapp.serializers import TeacherPUTSeriazlier, ClassCreateSerializer, ParentCreateSerializer, \
    TeachersCreateSerializer, PupilsCreateSerializer, ParentsPUTSerializer, PupilsPUTSerializer, ClassPUTSerializer


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


class ClassEditView(generics.UpdateAPIView):
    queryset = Classes.objects.all()
    serializer_class = ClassPUTSerializer
    http_method_names = ['put']

    def put(self, request, pk):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            number = serializer.validated_data.get('number')
            letter = serializer.validated_data.get('letter')

            if Classes.objects.filter(number=number, letter=letter, isactive=True).exclude(pk=pk).exists():
                return Response(
                    {"error": f"Класс {number}-{letter} уже существует!"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save(modifiedby=request.user.username)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_update(self, serializer):
        serializer.save(modifiedby=self.request.user.username)
