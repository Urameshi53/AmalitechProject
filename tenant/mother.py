# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:10:09 2024

@author: Daniel Akey
"""

import datetime
import string 
import random 


'''
Access Key Manager - Features
    1. Key Generation
    2. Key Storage
    3. Key distribution
    4. Key Rotation
    5. Key Revocation
    6. Access Control
    7. Audit & Loggin

'''

class Key(object):    
    def __init__(self):
        self.status = self.check_status()
        self.key_plain = ''.join(random.sample(string.ascii_letters, 5))
        self.key_encrypted = self.encrypt()
        
    def encrypt(self):
        k = str(random.randint(100, 999))
        self.key_encrypted = self.key_plain + k
        return self.key_encrypted
    
    def decrypt(self):
        self.key_plain = self.key_encrypted[:-3]
        print(self.key_plain)
        return self.key_plain
        
    def check_status(self):
        l = ['Active', 'Expired', 'Revoked']
        return random.sample(l, 1)[0]
    
    def __str__(self):
        return self.key_encrypted
    
    


class Mother(object):
    def __init__(self):
        self.keys = []
        self.data = {}
    
    def generate_key(self):
        a = Key()
        self.keys.append(a)
        return a 
    
    def grantkey(self, school):
        if not school.key:
            key = self.generate_key(school)
            return key
        elif school.key.status == 'Expired':
            key = self.generate_key(school)
            return key
        elif school.key.status == 'Revoked':
            print(str(school), 'Your access key has been revoked')
        else:
            print(str(school),'You already have an active key')
    
    def revoke_key(self, key):
        pass
    
    def rotate_key(self, key):
        pass
    
    def print_keys(self):
        for i in self.keys:
            print(i, i.status, i.proc_date_formatted)
            
    def print_data(self):
        for i in self.data.keys():
            print(str(i), str(self.data[i]), self.data[i].status)
    

    
    
    
    
    
    
    
    