import os
import time

# 1.需要备份的文件与目录将被
# 指定在一个列表中
# 例如在windows中
# source = ['"C:\\My Documents"','c:\\Code']
# 如在Mac OS X 与 Linux下：
# source = ['/users/swa/notes']
source = ['E:\\Coding\\es6study']
# 在这里需要在字符串中使用双引号，用以括起其中包含空格的名称

# 2.备份文件必须存储在一个主备份目录中
# 例如在windows 下：
# target_dir = 'E:\\Backup'
# 又例如在 Mac OS X 与 Linux 下：
# target_dir = '/users/swa/backup'
target_dir = 'E:\\Testing'

# 3.备份文件将打包压缩成zip文件
# 4.zip压缩文件名由当前日期与时间构成
target = target_dir+os.sep+\
    time.strftime('%Y%m%d%H%M%S')+'.zip'

# 如果目标目录文件不存在需要进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5.我们用zip命令将文件打包成zip格式
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

# 运行备份
print('Zip command is :')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to',target)
else:
    print('Backup Failed!')