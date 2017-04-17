import os
import sys
import time
import unittest

from Common import Mappings, Get
from Core.HTMLTestRunner import HTMLTestRunner
from Plugins import Mail, Jenkins

job_name = sys.argv[1]
job_name_list = []
for item in Jenkins.get_jobs_info():
    job_name_list.append(item['name'])
if job_name not in job_name_list:
    print('Please input correct job name!!!')
    exit()

print('\n')
print('==============================================================================')
print('Automation Test Script')
print('==============================================================================')

x, y, z = Jenkins.get_job_info(job_name)
jenkins_ls = [('Job Name', job_name),
              ('Version', x),
              ('Builder', y),
              ('Build Finish Time', z)]
print('Get jenkins info successfully...')

test_suit = unittest.TestLoader().loadTestsFromTestCase(Mappings.test_suite[job_name])
total_test = unittest.TestSuite([test_suit])

timeStampArr = time.localtime(time.time())
folder = Get.base_dir() + '/Html/' + time.strftime('%Y-%m-%d', timeStampArr) + '/'
os.makedirs(folder, exist_ok=True)
file = folder + time.strftime('%H-%M-%S') + '.html'

with open(file, 'w', encoding='utf-8') as f:
    HTMLTestRunner(stream=f, title='Automation Script Report', description=u'').run(total_test, jenkins_ls)
print('Finish to run test case...')
print('Generate report successfully...')

with open(file, 'r') as f:
    content = f.read()
if Mail.send_mail('Automation Script Report', content, job_name):
    print('Email is sent to builder...')
