from rest_framework_mongoengine import serializers

from .models import Question


class QuestionSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Question
        fields = '__all__'
