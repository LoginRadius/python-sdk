from pbkdf2 import PBKDF2
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import datetime
import hashlib
import binascii
import sys

class SOTT:
    CONST_INITVECTOR="tu89geji340t89u2"
    CONST_KEYSIZE=256

    def __init__(self, lr_object):
            self._lr_object = lr_object
            self.bs = 16
    
    def encrypt(self, time = '10', getLRserverTime = False):
        if getLRserverTime:
            from LoginRadius.sdk.authentication import Authentication
            authenticationAPI = Authentication(self._lr_object)
            result = authenticationAPI.getServerTime(time)
            if result.get('Sott') is not None:
                Sott = result.get('Sott')
                for timeKey,val in Sott.items():
                    if timeKey == 'StartTime':
                        now = val;
                    if timeKey == 'EndTime':
                        now_plus_10m = val;                   
            else:
                now = datetime.datetime.utcnow()
                now  = now - datetime.timedelta(minutes=5)
                now_plus_10m=now+datetime.timedelta(minutes=10)
                now = now.strftime("%Y/%m/%d %I:%M:%S")
                now_plus_10m = now_plus_10m.strftime("%Y/%m/%d %I:%M:%S")
     
                
        else:
            now = datetime.datetime.utcnow()
            now  = now - datetime.timedelta(minutes=5)
            now_plus_10m=now+datetime.timedelta(minutes=10)
            now = now.strftime("%Y/%m/%d %I:%M:%S")
            now_plus_10m = now_plus_10m.strftime("%Y/%m/%d %I:%M:%S")
            
        plaintext=now+"#"+self._lr_object._get_api_key()+"#"+now_plus_10m
        padding = 16 - (len(plaintext) % 16)
        if sys.version_info[0] == 3:
            plaintext += (bytes([padding])*padding).decode()
        else:
            plaintext += (chr(padding)*padding).decode()
        
        salt="\0\0\0\0\0\0\0\0"
        cipher_key=PBKDF2(self._lr_object._get_api_secret(), salt,10000).read(self.CONST_KEYSIZE//8)
        
        if sys.version_info[0] == 3:
            iv = bytes(self.CONST_INITVECTOR,'utf-8')
            text = bytes(plaintext,'utf-8')
        else:
            iv = str(self.CONST_INITVECTOR)
            text = str(plaintext)

        backend = default_backend()
        cipher = Cipher(algorithms.AES(cipher_key), modes.CBC(iv), backend=backend)
        encryptor = cipher.encryptor()
        ct = encryptor.update(text) + encryptor.finalize()

        base64cipher=base64.b64encode(ct)
        
        md5=hashlib.md5()
        md5.update(base64cipher.decode('utf8').encode('ascii'))
        return base64cipher.decode('utf-8')+"*"+binascii.hexlify(md5.digest()).decode('ascii')
