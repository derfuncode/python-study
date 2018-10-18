import urllib.request

name = 'joe mama'
number = 6 
base = 'http://www/~foo/cgi-bin/s.py'
final = '%s?name=%s&num=%d' % (base, name, number)
print(final)

print(urllib.parse.quote(final))

print(urllib.parse.quote_plus(final))


