import urllib.request
import re

def get_body(url):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>')
    result = r.findall(html_content.decode('GBK'))
    return result

if __name__ == '__main__':
    body = get_body('http://tech.163.com/14/1219/01/ADPT7MTE000915BF.html')
    file_object = open('result.txt','w')
    for l in body:
        file_object.write(l + '\n')
    file_object.close()
