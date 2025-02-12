# Credit: DeepSeek
import hashlib

def compute_sha256(data: bytes) -> str:
    """计算数据的SHA256哈希值"""
    return hashlib.sha256(data).hexdigest()

def validate_checksum(data: bytes, expected_hash: str) -> bool:
    """验证数据哈希是否匹配"""
    return compute_sha256(data) == expected_hash