# Credit: DeepSeek
class CompressionError(Exception):
    """压缩/解压操作基础异常"""
    pass

class UnsupportedAlgorithm(CompressionError):
    """请求了未注册的压缩算法"""
    pass

class CorruptedDataError(CompressionError):
    """数据损坏无法解压"""
    pass