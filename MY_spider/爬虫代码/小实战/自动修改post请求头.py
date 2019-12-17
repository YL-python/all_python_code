import re

head_post = '''
type: catL13
paged: 2
'''
pattern = '^(.*?): (.*?)$'

for line in head_post.splitlines():   # \\1  \\2 是反向引用
    print(re.sub(pattern,'\'\\1\': \'\\2\',',line))