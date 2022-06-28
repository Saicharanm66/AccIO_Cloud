from django.db import models

class PhotoGallery(models.Model):
    # upload=models.ImageField(upload_to='images/')
    upload=models.ImageField(upload_to='images/')
    
    def __str_(self):
        return str(self.pk)
    def delete(self, using=None, keep_parents=False):
        self.upload.storage.delete(self.upload.name)
        super().delete()
        