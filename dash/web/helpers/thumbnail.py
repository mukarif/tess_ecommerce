from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image


def create_thumbnail(image, size=(200, 200)):
    """Create a thumbnail for the given image."""
    img = Image.open(image)
    img.convert("RGB")  # Ensure image is in RGB mode
    img.thumbnail(size, Image.Resampling.LANCZOS)

    # Save the thumbnail to a BytesIO object
    thumb_io = BytesIO()
    img.save(thumb_io, format="JPEG")

    # Create a Django file from the BytesIO object
    thumbnail = ContentFile(thumb_io.getvalue(), name=f"thumb_{image.name}")
    return thumbnail
