# Credit: DeepSeek
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from compression import get_compressor

class CompressedStorage(FileSystemStorage):
    """
    智能压缩存储后端
    文件名格式：原始文件名.原扩展名.压缩扩展名
    示例：report_2023.docx.lzma
    """
    
    def _save(self, name, content):
        # 获取原始文件名信息
        base_name, orig_ext = os.path.splitext(name)
        
        # 获取当前压缩策略
        compressor = get_compressor(settings.ACTIVE_COMPRESSION_EXT)
        
        # 读取并压缩数据
        raw_data = content.read()
        compressed_data = compressor.compress(raw_data)
        
        # 构建新文件名
        # 格式：原始文件名.原扩展名.压缩扩展名
        new_name = f"{base_name}{orig_ext}.{settings.ACTIVE_COMPRESSION_EXT}"
        
        # 调用父类保存压缩文件
        saved_name = super()._save(new_name, ContentFile(compressed_data))
        
        # 传递元数据到模型实例
        if hasattr(content, 'instance'):
            content.instance.compression_type = settings.ACTIVE_COMPRESSION_EXT
            
        return saved_name

    def _open(self, name, mode='rb'):
        # 解析压缩算法扩展名
        *_, compression_ext = os.path.splitext(name)
        compression_ext = compression_ext[1:]  # 去掉点
        
        # 获取解压器
        decompressor = get_compressor(compression_ext)
        
        # 读取压缩文件
        raw_file = super()._open(name, mode)
        compressed_data = raw_file.read()
        
        # 解压数据
        original_data = decompressor.decompress(compressed_data)
        
        return ContentFile(original_data)