# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 13:27:30 2024

@author: Daniel Akey
"""

from datetime import datetime
import time
import string
import random


class AccessKey(object):    
    def __init__(self):
        self.status = self.check_status()
        self.key_plain = ''.join(random.sample(string.ascii_letters, 5))
        self.key_encrypted = self.encrypt()
        self.proc_date = datetime.now()
        self.proc_date_formatted = self.proc_date.strftime('%Y-%m-%d') # %H:%M:%S')
        self.exp_date = datetime(2025,1,12)
        self.exp_date_formatted = self.exp_date.strftime('%Y-%m-%d')
        self.id = None
        
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
    
    