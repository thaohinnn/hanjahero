from rest_framework import serializers
from home.models.question import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question_id', 'question_text', 'option_1', 'option_2', 'option_3', 'option_4', 'correct_option',
                  'exam', 'skill', 'format', 'level', 'question_meta_data']
