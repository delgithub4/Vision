from services.provider_service import ProviderService


class VisionService:

    def __init__(self):

        self.provider = ProviderService()

    def process(self):

        return self.provider.analyze()
