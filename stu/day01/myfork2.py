import os
import time

print('starting....')

ret_value = os.fork()

if ret_value:
    print('In parent..')
    time.sleep(10)
    print('parent exit')
else:
    print('In child')
    for i in range(5):
        time.sleep(1)
        print(f"第{i+1}次，时间为{time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))}")
    print('child exit')