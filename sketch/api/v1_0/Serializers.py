from rest_framework.serializers import ModelSerializer

from sketch.models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = [
            'id',
            'notes_title',
            'notes_description',
            'notes_time',
            'notes_date',
            'notes_priority'
        ]