import os

path = input('Укажите директорию исходников: ')

# r'D:\#gitRep\UPTG\Signal\SourcesDelphi\Administration\AdmViewTemplates'

for root, dirs, files in os.walk(path):
    for name in files:
        f = os.path.join(root, name)
        if any([f.endswith(extension) for extension in '.dpk,.dproj'.split(',')]):
            with open(f, 'r') as fh:
                data = fh.read()
            for r in (
                    ('advchartdxe13', 'advchartdxe14'),
                    ('TMSVCLUIPackPkgDXE13', 'TMSVCLUIPackPkgDXE14'),
                    ('TMSVCLUIPackPkgExDXE13', 'TMSVCLUIPackPkgExDXE14'),
                    ('TMSVCLUIPackPkgXlsDXE13', 'TMSVCLUIPackPkgXlsDXE14'),
                    ('FlexDX10_4', 'FlexDX11_0'),
                    ('doa41d104', 'doa41d110'),
                    ('PascalScript_Core_D27', 'PascalScript_Core_D28'),
                    ('fqb270', 'fqb280'),
                    ('27,', '28,'),
                    ('27;', '28;'),
                    ('27.dcp', '28.dcp')):
                data = data.replace(*r)
            with open(f, 'w') as fh:
                fh.write(data)
            print('Файл {0} обработан!'.format(f))

print('Завершено.')
