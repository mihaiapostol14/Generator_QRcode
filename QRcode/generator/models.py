from datetime import datetime
from io import BytesIO

import qrcode
from django.core.files import File
from django.db import models


class QRCode(models.Model):
    content = models.CharField(max_length=255)
    qr_image = models.ImageField(upload_to='qr_codes/', blank=True)

    def __str__(self):
        return self.content

    def get_qr_code_image(self):
        if self.qr_image and hasattr(self.qr_image, 'url'):
            return self.qr_image.url
        return None

    def save(self, *args, **kwargs):
        qr_version = 1
        qr_error_correction = qrcode.ERROR_CORRECT_L
        qr_box_size = 10
        qr_border = 4

        fill_color = "black"
        back_color = "white"

        qr_image_factory = None
        qr_mask_pattern = None

        qr = qrcode.QRCode(
            version=qr_version,
            error_correction=qr_error_correction,
            box_size=qr_box_size,
            border=qr_border,
            image_factory=qr_image_factory,
            mask_pattern=qr_mask_pattern,
        )

        qr.add_data(self.content)
        qr.make(fit=True)

        img = qr.make_image(
            fill_color=fill_color,
            back_color=back_color
        )

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        filename = f"qr_{timestamp}.png"

        buffer = BytesIO()
        img.save(buffer, format='PNG')

        self.qr_image.save(filename, File(buffer), save=False)

        super().save(*args, **kwargs)
