# Credit: DeepSeek
from django.conf import settings
from .exceptions import UnsupportedAlgorithm

class _AlgorithmRegistry:
    def __init__(self):
        self._algorithms = {}
        self._default_params = getattr(settings, 'COMPRESSION_PARAMS', {})

    def register(self, ext: str, strategy_cls):
        """注册压缩算法扩展名"""
        self._algorithms[ext.lower()] = strategy_cls

    def get(self, ext: str):
        """获取压缩器实例（带配置参数）"""
        ext = ext.lower()
        if ext not in self._algorithms:
            raise UnsupportedAlgorithm(f"未支持的压缩格式: {ext}")
        
        # 从配置中获取参数
        params = self._default_params.get(ext, {})
        return self._algorithms[ext](**params)

# 单例模式注册中心
registry = _AlgorithmRegistry()

# 快捷方法
register_algorithm = registry.register
get_compressor = registry.get