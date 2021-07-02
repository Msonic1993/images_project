import os
from django.core.exceptions import ValidationError

class Validator:

    def validateDocumentExtension(self, file):
      ext = os.path.splitext(file.name)[1]
      valid_extensions = ['.png', '.jpg']
      if not ext in valid_extensions:
        raise ValidationError(u'Typ pliku nie jest wspierany. Akceptowane typy plików: '+str(valid_extensions) )