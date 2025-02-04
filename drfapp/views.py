from django.shortcuts import render

from .models import Classes, Pupils, Teachers, Parents
# Create your views here.
from .serializers import ClassSerializer, ClassPupilSerializer, MalePupilsSerializer, TeachersClassesSerializer, \
    PupilDeletedSerializer, TeachersSerializer, ParentSerializer, PupilSerializer
from rest_framework import generics
from rest_framework import status

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
    def get(self,request):
        pupil = Pupils.objects.filter(classes__isnull=True).order_by('first_name')
        if not pupil.exists():
            return Response({'pupils':'NOT FOUND'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = PupilSerializer(pupil,many=True)
        return Response({
            'count':len(serializer.data),
            'result':serializer.data
        })


class PupilsLinkedView(APIView):
    def get(self,request):
        pupil = Pupils.objects.filter(classes__isnull=False).order_by('first_name')
        if not pupil.exists():
            return Response({'pupils':'NOT FOUND'},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = PupilSerializer(pupil,many=True)
        return Response({
            'count':len(serializer.data),
            'result':serializer.data
        })

