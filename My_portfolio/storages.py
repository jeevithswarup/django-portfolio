from cloudinary_storage.storage import (
    MediaCloudinaryStorage,
    RawMediaCloudinaryStorage
)

class ImageStorage(MediaCloudinaryStorage):
    pass


class PDFStorage(RawMediaCloudinaryStorage):
    pass
