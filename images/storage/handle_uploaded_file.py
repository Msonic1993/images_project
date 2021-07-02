import logging

from django.core.files.storage import FileSystemStorage


from images.models import Storage



def handleUploadedFile(file,request):
    # fs = FileSystemStorage()
    # filename = fs.save('media/'+file.name, file)
    # uploaded_file_url = fs.url(filename)
    # print(str(uploaded_file_url))
    Storage(fileName=file.name ,path=file,file=file, owner_id= request.user.id).save()
    return logging.getLogger("django").info("Image file has been uploaded to server to path ")