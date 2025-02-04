from rest_framework import serializers

from drfapp.models import Classes, Pupils, Teachers, Parents


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ['number', 'letter', 'isactive']


class PupilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pupils
        fields = ['first_name', 'last_name', 'surname', 'gender']


class ClassPupilSerializer(serializers.ModelSerializer):
    pupils = PupilSerializer(source='pupil', many=True)
    count = serializers.IntegerField(source='pupil.count', read_only=True)

    class Meta:
        model = Classes
        fields = ['number', 'letter', 'isactive', 'count', 'pupils']


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


# class PupilParentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pupils
#         fields = ['id', 'first_name', 'last_name', 'surname', 'gender']


# class ParentsPupilsSerializer(serializers.ModelSerializer):
#     pupils = PupilParentSerializer(source='pupil_relations.', many=True, read_only=True)
#
#     class Meta:
#         model = Parents
#         fields = ['id', 'first_name', 'last_name', 'surname', 'pupils']
# class ParentsPupilsSerializer(serializers.ModelSerializer):
#     pupils = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Parents
#         fields = ['id', 'first_name', 'last_name', 'surname', 'pupils']
#
#     def get_pupils(self, obj):
#         return PupilParentSerializer(obj.pupil_relations.values_list('pupil', flat=True), many=True).data


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
