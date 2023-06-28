import sys
import hashlib
f_hash= open("5.txt", "w",encoding='utf-8')  
for line in range(0,9999): 
    url=str("|/account4a/home/register/acct/handle/user|orgId=" + str(line)).encode('utf-8')
    md5hash = hashlib.md5(url)
    md5 = md5hash.hexdigest()
    f_hash.write(md5 + '\n')
f_hash.close()
