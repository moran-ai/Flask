# 加密技术：md5 sha1 sha224 sha256 sha512
import hashlib

msg = 'Hello World'
md = hashlib.md5(msg.encode('utf-8'))
print(md)  # 返回md5的一个 HASH对象

r = md.hexdigest() # 得到加密的内容
print(r) # 32长度

sha1 = hashlib.sha1(msg.encode('utf-8')).hexdigest()
print(sha1) # 40

sha256 = hashlib.sha256(msg.encode('utf-8')).hexdigest()
print(sha256)  # 64

sha512 = hashlib.sha512(msg.encode('utf-8')).hexdigest()
print(sha512) # 128
