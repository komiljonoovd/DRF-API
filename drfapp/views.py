from .models import Classes, Pupils, Teachers, Parents
# Create your views here.
from .serializers import ClassSerializer, ClassPupilSerializer, MalePupilsSerializer, TeachersClassesSerializer, \
    PupilDeletedSerializer, TeachersSerializer, ParentSerializer, PupilSerializer, PupilInfoSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


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


# DELETE
# class ClassesDeleteView(APIView):
#     def delete(self,request,pk):
#         delete = Classes.objects.filter(pk=pk).delete()
#         if delete:
#             return Response(status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
