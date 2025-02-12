from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from config.global_settings import MaxSizes
from django.core.files.storage import FileSystemStorage
import lzma
from django.core.files.base import ContentFile


class RestrictedFileField(FileField):
    def __init__(self, *args, **kwargs):
        self.content_types = kwargs.pop("content_types", [])
        self.max_upload_size = kwargs.pop("max_upload_size", MaxSizes.VIDEOFILE)
        super().__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data = super().clean(*args, **kwargs)   # clean()方法来自于FileField的父类Field, 用于验证
        file = data.file

        try:
            content_type = file.content_type
            # 自定义验证
            if content_type in self.content_types:
                if file.size > self.max_upload_size:
                    raise forms.ValidationError('Please keep filesize under {}. Current filesize {}'.format(filesizeformat(self.max_upload_size), filesizeformat(file.size)))
            else:
                raise forms.ValidationError('This file type is not allowed.')
        except AttributeError:
            pass
        return data

# Credit: DeepSeek
# ========== 1. 自定义 LZMA 存储类 ==========
class CompressedStorage(FileSystemStorage):
    def _save(self, name, content):
        """保存时压缩内容"""
        # 一次性读取原始内容
        raw_content = content.read()
        
        # 使用 LZMA 最高压缩率（可根据需求调整参数）
        compressed = lzma.compress(
            raw_content, 
            format=lzma.FORMAT_XZ, 
            preset=9  # 压缩级别 0-9
        )
        
        # 保存压缩后的内容（默认不修改文件名，但可强制添加 .xz 后缀）
        return super()._save(name, ContentFile(compressed))

    def _open(self, name, mode='rb'):
        """读取时自动解压"""
        file = super()._open(name, mode)
        try:
            # 解压内容
            decompressed = lzma.decompress(file.read())
        except lzma.LZMAError:
            # 如果文件未压缩，直接返回原始内容
            file.seek(0)
            return file
        return ContentFile(decompressed, name=name)
    

# ========== 2. 自定义双属性文件字段 ==========
class CompressedFileField(FileField):
    def __init__(self, *args, **kwargs):
        kwargs['storage'] = CompressedStorage()  # 绑定 LZMA 存储
        super().__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name, **kwargs):
        super().contribute_to_class(cls, name, **kwargs)
        
        # 添加 compressed_xxx 属性（直接返回存储的压缩文件）
        setattr(cls, f'compressed_{name}', property(
            lambda instance: getattr(instance, name)
        ))
        
        # 添加 decompressed_xxx 属性（返回解压后的内容）
        setattr(cls, f'decompressed_{name}', property(
            lambda instance: self._get_decompressed_content(instance, name)
        ))

    def _get_decompressed_content(self, instance, name):
        compressed_file = getattr(instance, name)
        if not compressed_file:
            return None
            
        # 读取并解压
        try:
            compressed_data = compressed_file.read()
            decompressed = lzma.decompress(compressed_data)
        except lzma.LZMAError:
            # 如果文件未压缩，直接返回原内容
            compressed_file.seek(0)
            return compressed_file
        
        return ContentFile(decompressed, name=compressed_file.name)