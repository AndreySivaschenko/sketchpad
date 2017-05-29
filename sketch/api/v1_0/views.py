from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from .Serializers import NoteSerializer
from sketch.models import Note

class NoteListApiView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

