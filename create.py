import os

f = open('data.txt', 'r')

sz = 'class ResponseObject(object):\n'
sz = sz + '    def __init__(self):\n'
for line in f:
    ln = line.strip().replace('\n', '')
    sz = sz + '        self._' + ln + ' = None\n'
f.close()

sz = sz + '\n'
f = open('data.txt', 'r')
for line in f:
    ln = line.strip().replace('\n', '')
    sz = sz + '    def _get' + ln + '(self):\n'
    sz = sz + '        return self._' + ln + '\n'
    sz = sz + '    def _set' + ln + '(self, value):\n'
    sz = sz + '        self._' + ln + ' = value\n\n'
f.close()

sz = sz + '\n'
f = open('data.txt', 'r')
for line in f:
    ln = line.strip().replace('\n', '')
    sz = sz + '    ' + ln + ' = property(_get' + ln + ', _set' + ln + ')\n'
f.close()
#print(sz)


f = open('data.txt', 'r')
sz = ''
for line in f:
    ln = line.strip().replace('\n', '')
    sz = sz + "    ro." + ln + " = data['a:" + ln + "']['@i:nil'] if type(data['a:" + ln + "']) == dict else data['a:" + ln + "']\n"
f.close()
print(sz)
