# Credit: DeepSeek
from .registry import register_algorithm, get_compressor
from .exceptions import CompressionError, UnsupportedAlgorithm
from .strategies import CompressionStrategy

__all__ = [
    'register_algorithm',
    'get_compressor',
    'CompressionError',
    'UnsupportedAlgorithm',
    'CompressionStrategy'
]