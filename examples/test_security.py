import os
import sys

dir_name = os.path.dirname(os.path.abspath(__file__))
sys.path.append(dir_name + '/../')

import security

## test md5
print security.gen_md5('asd')

## test gen_sha256
print security.gen_sha1('asd')

## test gen_sha256
print security.gen_sha256('asd')


