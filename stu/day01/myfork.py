import os

# print('starting....')
# ret_value=os.fork() # fork 一旦执行 后续代码会拉出一个进程 使的hello，world 打印两次
# # print(ret_value)
# print('hello,world')


print('starting.....')
ret_value=os.fork()
if ret_value: # 值非0 为真 否则为假
    print('In parent')
else:
    print('In child')

print('Done')