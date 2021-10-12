import os

encoding = [
    'utf-8',
    'utf-8-sig',
    'windows-1251',
    'GBK',
    'cp500',
    'ASCII',
    'US-ASCII',
    'utf-16',
    'Big5'
]

path = r'D:\#gitRep\UPTG\Signal\SourcesDelphi\Engine\PSConst04'

for root, dirs, files in os.walk(path):
    for name in files:
        f = os.path.join(root, name)
        for enc in encoding:
            try:
                open(f, encoding=enc).read()
            except (UnicodeDecodeError, LookupError):
                pass
            else:
                print('"{0}" correct_encoding = {1}'.format(f, enc))
                break
print('End.')
