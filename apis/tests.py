from django.test import TestCase

# Create your tests here.


# Commandes à entrer pour tester rapidement apis.voca.OutfileCreate
# ssh
cd /home/common/shade
python3 manage.py shell
# python
from apis.voca import *
raw_filename = '001_raw'
ref_list = ['ligne1','ligne2','ligne3','ligne4','ligne5']
log = ['la cucaracha']
OutFileCreate(raw_filename,ref_list,log)
