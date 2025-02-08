from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Classes, Pupils, Teachers, Parents
# Create your views here.
from .serializers import ClassSerializer, ClassPupilSerializer, MalePupilsSerializer, TeachersClassesSerializer, \
    PupilDeletedSerializer, TeachersSerializer, ParentSerializer, PupilSerializer, PupilInfoSerializer, \
    UpdateSerializer, ClassCreateSerializer, ParentCreateSerializer, TeachersCreateSerializer, PupilsCreateSerializer, \
    ClassPUTSerializer, ParentsPUTSerializer, PupilsPUTSerializer, TeacherPUTSeriazlier
from rest_framework import generics, viewsets, mixins, permissions
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response


# class ClassViewTrue(generics.ListAPIView):
#     queryset = Classes.objects.filter(isactive=True).order_by('-number')
#     serializer_class = ClassSerializer
#
#
# class ClassViewFalse(generics.ListAPIView):
#     queryset = Classes.objects.filter(isactive=False).order_by('-number')
#     serializer_class = ClassSerializer


class ClassViewTrue(APIView):
    def get(self, request):
        cls = Classes.objects.filter(isactive=True).order_by('-number')
        serializer = ClassSerializer(cls, many=True)

        return Response({
            "count": len(serializer.data),
            "result": serializer.data

        })


class ClassViewFalse(APIView):
    def get(self, request):
        cls = Classes.objects.filter(isactive=False).order_by('-number')
        serializer = ClassSerializer(cls, many=True)

        return Response({
            "count": len(serializer.data),
            "result": serializer.data

        })


class ClassPupilView(APIView):
    def get(self, request):
        cls = Classes.objects.all().order_by('-number')
        serializer = ClassPupilSerializer(cls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MalePupilsView(APIView):
    def get(self, request):
        pupils = Pupils.objects.filter(gender="Мальчик").order_by('first_name')
        serializer = MalePupilsSerializer(pupils, many=True)
        return Response({
            "count": len(serializer.data),
            "result": serializer.data
        })


class FemalePupilsView(APIView):
    def get(self, request):
        pupils = Pupils.objects.filter(gender="Девочка").order_by('first_name')
        serializer = MalePupilsSerializer(pupils, many=True)
        return Response({
            "count": len(serializer.data),
            "result": serializer.data
        })


class TeachersClassesView(APIView):
    def get(self, request):
        teachers = Teachers.objects.all().order_by('first_name')
        serializer = TeachersClassesSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class ParentPupilView(APIView):
#     def get(self, request):
#         parents = Parents.objects.all().order_by('first_name')  # Загружаем всех родителей
#         serializer = ParentsPupilsSerializer(parents, many=True)  # Сериализуем с детьми
#         return Response(serializer.data, status=status.HTTP_200_OK)


class PupilDeletedView(APIView):
    def get(self, request):
        pupil = Pupils.objects.filter(isdeleted=True).order_by('first_name')
        if not pupil.exists():
            return Response({
                'pupils': 'NOT FOUND'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PupilDeletedSerializer(pupil, many=True)
        return Response({
            'count': len(serializer.data),
            'result': serializer.data
        })


class PupilNotDeletedView(APIView):
    def get(self, request):
        pupil = Pupils.objects.filter(isdeleted=False).order_by('first_name')
        if not pupil.exists():
            return Response({
                'pupils': 'NOT FOUND'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PupilDeletedSerializer(pupil, many=True)
        return Response({
            'count': len(serializer.data),
            'result': serializer.data
        })


class TeacherDeletedView(APIView):
    def get(self, request):
        teacher = Teachers.objects.filter(isdeleted=True).order_by('first_name')
        if not teacher.exists():
            return Response({'teachers': 'NOT FOUND'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = TeachersSerializer(teacher, many=True)
        return Response({
            'count': len(serializer.data),
            'result': serializer.data
        })


class TeacherNotDeletedView(APIView):
    def get(self, request):
        teacher = Teachers.objects.filter(isdeleted=False).order_by('first_name')
        if not teacher.exists():
            return Response({'teachers': 'NOT FOUND'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = TeachersSerializer(teacher, many=True)
        return Response({
            'count': len(serializer.data),
            'result': serializer.data
        })


class ParentNotDeletedView(APIView):
    def get(self, request):
        parent = Parents.objects.filter(isdeleted=False).order_by('first_name')
        if not parent.exists():
            return Response({'parents': 'NOT FOUND'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = ParentSerializer(parent, many=True)
        return Response({
            'count': len(serializer.data),
            'result': serializer.data
        })


class ParentDeletedView(APIView):
    def get(self, request):
        parent = Parents.objects.filter(isdeleted=True).order_by('first_name')
        if not parent.exists():
            return Response({'parents': 'NOT FOUND'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = ParentSerializer(parent, many=True)
        return Response({
            'count': len(serializer.data),
            'result': serializer.data
        })


class PupilsNotLinkedView(APIView):
    def get(self, request):
        pupil = Pupils.objects.filter(classes__isnull=True).order_by('first_name')
        if not pupil.exists():
            return Response({'pupils': 'NOT FOUND'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = PupilSerializer(pupil, many=True)
        return Response({
            'count': len(serializer.data),
            'result': serializer.data
        })


class PupilsLinkedView(APIView):
    def get(self, request):
        pupil = Pupils.objects.filter(classes__isnull=False).order_by('first_name')
        if not pupil.exists():
            return Response({'pupils': 'NOT FOUND'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = PupilSerializer(pupil, many=True)
        return Response({
            'count': len(serializer.data),
            'result': serializer.data
        })


class PupilIDView(APIView):
    def get(self, request, pk):
        pupil = Pupils.objects.filter(pk=pk)
        if not pupil.exists():
            return Response({'pupil': 'NOT FOUND'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = PupilInfoSerializer(pupil, many=True)
        return Response({
            'pupil': serializer.data
        })


class TeacherIDView(APIView):
    def get(self, request, pk):
        teacher = Teachers.objects.filter(pk=pk)
        if not teacher.exists():
            return Response(
                {'teacher': 'NOT FOUND'},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = TeachersSerializer(teacher, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ParentsNotDeletedView(generics.ListAPIView):
    queryset = Parents.objects.filter(isdeleted=False).order_by('-first_name')
    serializer_class = ParentSerializer


class TeacherByIdViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = Pupils.objects.all()
    serializer_class = PupilInfoSerializer


# class TeachersDeleteView(APIView):
#     def post(self, request):
#         print('post request')
#         print(request.data)
#         # Передаем данные из запроса в сериализатор
#         serializer = UpdateSerializer(data=request.data)
#
#         # Проверяем, если данные валидны
#         if serializer.is_valid():
#             ids = serializer.validated_data['ids']
#             # Обновляем преподавателей по переданным ID
#             update_count = Teachers.objects.filter(id__in=ids).update(isdeleted=True)
#
#             # Ответ с количеством обновленных преподавателей
#             return Response({'message': f'{update_count} teachers updated successfully.'}, status=status.HTTP_200_OK)
#
#         # Если данные не валидны, возвращаем ошибку
#         print(serializer.errors)  # Лог ошибок
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class ClassDeleteView(APIView):
    http_method_names = ['patch']

    def patch(self, request, pk):
        update = Classes.objects.filter(pk=pk).update(isdeleted=True)
        if update:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ParentDeleteView(APIView):
    http_method_names = ['patch']

    def patch(self, request, pk):
        update = Parents.objects.filter(pk=pk).update(isdeleted=True)
        if update:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class TeacherstDeleteView(APIView):
    http_method_names = ['patch']

    def patch(self, request, pk):
        update = Teachers.objects.filter(pk=pk).update(isdeleted=True)
        if update:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class PupilDeleteView(APIView):
    http_method_names = ['patch']

    def patch(self, request, pk):
        update = Pupils.objects.filter(pk=pk).update(isdeleted=True)
        if update:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


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


class TeacherEditView(generics.UpdateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeacherPUTSeriazlier
    http_method_names = ['put']

    def perform_update(self, serializer):
        serializer.save(modifiedby=self.request.user.username)


class ClassDeleteView(APIView):
    def delete(self,request,pk):
        delete = Classes.objects.filter(pk=pk).delete()
        if delete:
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
