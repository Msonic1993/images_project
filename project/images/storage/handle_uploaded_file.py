import logging

from django.core.files.storage import FileSystemStorage


from images.models import Storage



def handleUploadedFile(file,request):
    fs = FileSystemStorage()
    filename = fs.save(file.name, file)
    uploaded_file_url = fs.url(filename)
    print(str(uploaded_file_url))
    instance = Storage(fileName=filename ,path=uploaded_file_url, file=uploaded_file_url, owner_id= request.user.id)
    instance.save()
    return logging.getLogger("django").info("Image file has been uploaded to server to path "), uploaded_file_url