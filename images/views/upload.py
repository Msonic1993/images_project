from rest_framework.parsers import FileUploadParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from images.img_validator import Validator
from images.serializers import UploadSerializer
from images.storage.handle_uploaded_file import handleUploadedFile
from images.storage.upload_files_checker import FilesUploadChecker


class FileUploadView(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file = request.FILES['file_uploaded']
        FilesUploadChecker().findOne()
        if file.read() is not None:
            file = request.FILES['file_uploaded']
            Validator().validateDocumentExtension(file)
            handleUploadedFile(file,request)
            content_type = file.content_type
            response = "POST API and you have uploaded a {} file".format(content_type)
            return Response(response)
