import unittest
import time
import os
import sys
from TestCase.App import EHomePayPassport
from Core.HTMLTestRunner import HTMLTestRunner
from Plugins import Mail, Jenkins

job_name = sys.argv[1]
# job_name = 'LFT_test_9.27_java_ehome_app-native-http_liuyu8080'
x, y, z = Jenkins.get_job_info(job_name)
jenkins_ls = [('Job Name', job_name),
              ('Version', x),
              ('Builder', y),
              ('Build Finish Time', z)]

test_suite = unittest.TestSuite()
test_suite.addTests([EHomePayPassport('testLogin')])

timeStampArr = time.localtime(time.time())
folder = './html/' + time.strftime('%Y-%m-%d', timeStampArr) + '/'
os.makedirs(folder, exist_ok=True)
file = folder + time.strftime('%H-%M-%S') + '.html'

with open(file, 'w', encoding='utf-8') as f:
    HTMLTestRunner(stream=f, title='Automation Script Report', description=u'').run(test_suite, jenkins_ls)

with open(file, 'r') as f:
    content = f.read()
if Mail.send_mail('Automation Script Report', content):
    print('邮件发送成功！')
