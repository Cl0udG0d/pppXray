import re

pattern2 = re.compile(r'"plugin":"(.*?)"')
str2='web.com/guestbook.php"},"identifier":"","plugin":"xss",'
result=pattern2.findall(str2)
print(result)