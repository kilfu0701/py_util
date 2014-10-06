import hashlib
import binascii
import random
import string


"""
@description:
    generate a string with format [a-zA-Z0-9]{length}

@param:
    length: int
"""
def random_string(length=64):
    random = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(length)])
    return random


"""
@description:
    maybe 'hashlib.pbkdf2_hmac' not found.
"""
def gen_sha256_pbkdf2_hmac(source, salt=b'agkppwlcm!@$ffjax', itertime=100):
    dk = hashlib.pbkdf2_hmac('sha256', source, salt, itertime)
    return binascii.hexlify(dk)


def gen_md5(source, salt='agkppwlcm!@$ffjax'):
    m = hashlib.md5()
    m.update(source + salt)
    return m.hexdigest()


def gen_sha1(source, salt='agkppwlcm!@$ffjax'):
    m = hashlib.sha1()
    m.update(source + salt)
    return m.hexdigest()


def gen_sha256(source, salt='agkppwlcm!@$ffjax'):
    m = hashlib.sha256()
    m.update(source + salt)
    return m.hexdigest()


