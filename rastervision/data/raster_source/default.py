from abc import (ABC, abstractmethod)
import os

import rastervision as rv


class RasterSourceDefaultProvider(ABC):
    @staticmethod
    @abstractmethod
    def handles(s):
        """Returns True if this provider is a default for this string"""
        pass

    @abstractmethod
    def construct(s, channel_order=None):
        """Constructs default based on the string and an optional channel order."""
        pass


class RasterioSourceDefaultProvider(RasterSourceDefaultProvider):
    @staticmethod
    def handles(uri):
        ext = os.path.splitext(uri)[1]
        return ext.lower() in ['.tif', '.tiff', '.geotiff', '.png', '.jpg']

    @staticmethod
    def construct(uri, channel_order=None):
        return rv.RasterSourceConfig.builder(rv.RASTERIO_SOURCE) \
                                    .with_uri(uri) \
                                    .with_channel_order(channel_order) \
                                    .build()
