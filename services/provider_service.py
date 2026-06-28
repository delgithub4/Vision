from providers.ocr_provider import OCRProvider
from providers.caption_provider import CaptionProvider
from providers.object_provider import ObjectProvider


class ProviderService:

    def __init__(self):

        self.ocr = OCRProvider()

        self.caption = CaptionProvider()

        self.objects = ObjectProvider()

    def analyze(self):

        return {

            "ocr": self.ocr.analyze(),

            "caption": self.caption.analyze(),

            "objects": self.objects.analyze()

        }
