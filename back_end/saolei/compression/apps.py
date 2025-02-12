# Credit: DeepSeek
from django.apps import AppConfig
from .registry import register_algorithm
from .strategies import LZMAStrategy, GzipStrategy, ZstdStrategy

class CompressionConfig(AppConfig):
    name = 'compression'
    verbose_name = "文件压缩模块"

    def ready(self):
        """注册默认压缩算法"""
        # 核心算法
        register_algorithm("lzma", LZMAStrategy)
        register_algorithm("gz", GzipStrategy)
        
        # 可选算法（需安装zstandard库）
        try:
            from .strategies import ZstdStrategy
            register_algorithm("zstd", ZstdStrategy)
        except ImportError:
            pass