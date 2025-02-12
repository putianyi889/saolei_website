# Credit: DeepSeek
from abc import ABC, abstractmethod
import lzma
import gzip
from .exceptions import CompressionError

class CompressionStrategy(ABC):
    @abstractmethod
    def compress(self, data: bytes) -> bytes:
        pass

    @abstractmethod
    def decompress(self, compressed_data: bytes) -> bytes:
        pass

class LZMAStrategy(CompressionStrategy):
    def __init__(self, preset=9):
        self.preset = preset

    def compress(self, data):
        try:
            return lzma.compress(data, preset=self.preset)
        except lzma.LZMAError as e:
            raise CompressionError(f"LZMA压缩失败: {str(e)}") from e

    def decompress(self, data):
        try:
            return lzma.decompress(data)
        except lzma.LZMAError as e:
            raise CompressionError(f"LZMA解压失败: {str(e)}") from e

class GzipStrategy(CompressionStrategy):
    def __init__(self, compresslevel=9):
        self.compresslevel = compresslevel

    def compress(self, data):
        try:
            return gzip.compress(data, compresslevel=self.compresslevel)
        except OSError as e:
            raise CompressionError(f"Gzip压缩失败: {str(e)}") from e

    def decompress(self, data):
        try:
            return gzip.decompress(data)
        except OSError as e:
            raise CompressionError(f"Gzip解压失败: {str(e)}") from e

class ZstdStrategy(CompressionStrategy):
    def __init__(self, level=3):
        try:
            import zstandard as zstd # type: ignore[reportMissingImports]
        except ImportError as e:
            raise ImportError("请先安装zstandard库") from e
        self.compressor = zstd.ZstdCompressor(level=level)
        self.decompressor = zstd.ZstdDecompressor()

    def compress(self, data):
        return self.compressor.compress(data)

    def decompress(self, data):
        return self.decompressor.decompress(data)