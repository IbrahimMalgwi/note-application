from rest_framework import viewsets
from .models import Note
from .serializers import NoteSerializer
import logging
logger = logging.getLogger(__name__)

def create_note(request):
    # Your create note logic
    logger.info("Note created: {}".format(note_id))

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer