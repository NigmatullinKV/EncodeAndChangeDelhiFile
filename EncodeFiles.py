import os
import chardet

path = input('Укажите директорию исходников: ')

# r'D:\#gitRep\UPTG\Signal\SourcesDelphi\Engine\PSConst04'

for root, dirs, files in os.walk(path):
    for name in files:
        f = os.path.join(root, name)
        if f.endswith(".pas"):
            with open(f, "rb") as Ff:
                text = Ff.read()
                enc = chardet.detect(text).get("encoding")
                if enc and enc.lower() != "utf-8":
                    with open(f, encoding='cp1251') as fh:
                        data = fh.read()
                    with open(f, 'wb') as fh:
                        fh.write(data.encode('utf-8'))
                    with open(f, 'rb') as fh:
                        data = fh.read()
                    data = data.replace(b'\n', b'\r\n')
                    with open(f, 'wb') as fh:
                        fh.write(data)
                    print('Файл {0} обработан, установлена кодировка "utf-8"!'.format(f))
                else:
                    print("Файл {0} находится в кодировке {1} и не требует конвертирования.".format(f, enc))
print('Завершено.')
