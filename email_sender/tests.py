
import sys
import os
import django

# 这两行很重要，用来寻找项目根目录，os.path.dirname要写多少个根据要运行的python文件到根目录的层数决定
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CQUTieba.settings')
django.setup()
from email_sender.util import EmailVerifyRecord
from email_sender.email_send import send_register_email,random_str
if __name__ == "__main__":
    send_register_email("2669188718@qq.com",send_type="email_sender")