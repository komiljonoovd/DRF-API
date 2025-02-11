from django.core.validators import RegexValidator
from rest_framework import serializers

from drfapp.models import Classes, Pupils, Teachers, Parents, ParentPupil
from rest_framework.exceptions import ValidationError


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['id', 'number', 'letter', 'isactive']


class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupils
        fields = ['first_name', 'last_name', 'surname', 'gender', 'isdeleted']


class PupilInfoSerializer(serializers.ModelSerializer):
    class_of_pupil = ClassSerializer(source='classes')
    parents = serializers.SerializerMethodField()

    class Meta:
        model = Pupils
        fields = ['id', 'first_name', 'last_name', 'surname', 'gender', 'parents', 'class_of_pupil']

    def get_parents(self, pk):
        parent = ParentPupil.objects.filter(pupil=pk)
        parents = [i.parent for i in parent]
        return ParentSerializer(parents, many=True).data


class ClassPupilSerializer(serializers.ModelSerializer):
    pupils = PupilSerializer(source='pupil', many=True)
    count = serializers.IntegerField(source='pupil.count', read_only=True)

    class Meta:
        model = Classes
        fields = ['id', 'number', 'letter', 'isactive', 'count', 'pupils']


class MalePupilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupils
        fields = ['first_name', 'last_name', 'surname', 'gender', 'isdeleted']


class FemalePupilsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupils
        fields = ['first_name', 'last_name', 'surname', 'gender', 'isdeleted']


class ClassesTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['id', 'number', 'letter', 'isactive', 'isdeleted']


class TeachersClassesSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source='classes.count', read_only=True)
    classes = ClassesTeacherSerializer(many=True, read_only=True)

    class Meta:
        model = Teachers
        fields = ['id', 'first_name', 'last_name', 'surname', 'count', 'classes']


class PupilDeletedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupils
        fields = ['id', 'first_name', 'last_name', 'surname', 'gender']


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ['id', 'first_name', 'last_name', 'surname', 'isdeleted']


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = ['id', 'first_name', 'last_name', 'surname', 'isdeleted']


class UpdateSerializer(serializers.Serializer):
    ids = serializers.ListField(
        child=serializers.IntegerField(),
        required=True
    )


class ClassCreateSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(min_value=1, max_value=11)
    letter = serializers.CharField(
        max_length=1,
        validators=[
            RegexValidator(
                regex='^[А-ЯЁ]$',
                message='Буква должна быть одной заглавной русской буквой (А-Я, Ё).'
            )
        ]
    )
    createdby = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Classes
        fields = ['number', 'letter', 'isactive', 'teacher', 'createdby']


class ParentCreateSerializer(serializers.ModelSerializer):
    createdby = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Parents
        fields = ['first_name', 'last_name', 'surname', 'phone', 'createdby', 'note', 'isdeleted']


class TeachersCreateSerializer(serializers.ModelSerializer):
    createdby = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Teachers
        fields = ['first_name', 'last_name', 'surname', 'isdeleted', 'createdby']


class PupilsCreateSerializer(serializers.ModelSerializer):
    createdby = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Pupils
        fields = ['first_name', 'last_name', 'surname', 'gender', 'birthday', 'isdeleted', 'note', 'createdby',
                  'classes']


class ClassPUTSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField(min_value=1, max_value=11)
    letter = serializers.CharField(
        max_length=1,
        validators=[
            RegexValidator(
                regex='^[А-ЯЁ]$',
                message='Буква должна быть одной заглавной русской буквой (А-Я, Ё).'
            )
        ]
    )
    modifiedby = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Classes
        fields = ['number', 'letter', 'isactive', 'teacher', 'isdeleted', 'modifiedby']


class ParentsPUTSerializer(serializers.ModelSerializer):
    modifiedby = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Parents
        fields = ['first_name', 'last_name', 'surname', 'phone', 'isdeleted', 'note', 'modifiedby']


class PupilsPUTSerializer(serializers.ModelSerializer):
    modifiedby = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Pupils
        fields = ['first_name', 'last_name', 'surname', 'gender','birthday','classes','isdeleted', 'note', 'modifiedby']


class TeacherPUTSeriazlier(serializers.ModelSerializer):
    modifiedby = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Teachers
        fields = ['first_name', 'last_name', 'surname', 'isdeleted', 'modifiedby']


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        token['username'] = user.username
        return token