from cloudinary_storage.storage import (
    MediaCloudinaryStorage,
    RawMediaCloudinaryStorage
)

class ImageStorage(MediaCloudinaryStorage):
    pass


class PDFStorage(RawMediaCloudinaryStorage):
    resource_type = "raw"
    access_mode = "public"
