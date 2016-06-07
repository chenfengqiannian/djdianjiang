
import rsa
import os
from dianjiang   import settings
import base64
from rsa import verify
def sign(message):
    print os.path.join(settings.BASE_DIR,'rsa_public_key.pem')
    op=os.path.join(settings.BASE_DIR,'rsa_public_key.pem')
    oi=os.path.join(settings.BASE_DIR,'rsa_private_key.pem')
    
   
    with open(oi) as privatefile:
        p=privatefile.read()
        privkey=rsa.PrivateKey.load_pkcs1(p)
    signature=rsa.sign(message,privkey,"SHA-1")
    print base64.b64encode(signature)
    
    
 
        
   
    
    return base64.b64encode(signature)
        
