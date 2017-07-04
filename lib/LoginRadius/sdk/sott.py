from pbkdf2 import PBKDF2
from Crypto.Cipher import AES
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
        
        cipher=AES.new(cipher_key, AES.MODE_CBC, self.CONST_INITVECTOR)
        
        base64cipher=base64.b64encode(cipher.encrypt(plaintext))
        
        md5=hashlib.md5()
        md5.update(base64cipher.decode('utf8').encode('ascii'))
        return base64cipher.decode('utf-8').replace("+","%2B")+"*"+binascii.hexlify(md5.digest()).decode('ascii')
    
    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    def decrypt(self,cipher):
        base64token=cipher[:cipher.index("*")].replace("%2B","+");
        cipherBytes=base64.b64decode(base64token)
        salt="\0\0\0\0\0\0\0\0"
        cipher_key=PBKDF2(self._lr_object._get_api_secret(), salt,10000).read(self.CONST_KEYSIZE//8)
        cipher=AES.new(cipher_key, AES.MODE_CBC, self.CONST_INITVECTOR)
        return self._unpad(cipher.decrypt(cipherBytes[AES.block_size:])).decode('utf-8',errors="ignore")
