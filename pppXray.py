import os
import hashlib
import re
import time

def logo():
    logo='''
 _ __  _ __  _ __         
| '_ \| '_ \| '_ \        
| |_) | |_) | |_) |       
| .__/| .__/| .__/        
| |   | |   | |           
|_|   |_|   |_|           
   __   __                
   \ \ / /                
    \ V / _ __ __ _ _   _ 
    /   \| '__/ _` | | | |
   / /^\ \ | | (_| | |_| |
   \/   \/_|  \__,_|\__, |
                     __/ |
                    |___/ 
                            v1.0
                            author:springbird
    '''
    return logo


def xrayScan(targeturl,outputfilename="test"):
    scanCommand="xray.exe webscan --basic-crawler {} --html-output {}.html".format(targeturl,outputfilename)
    print(scanCommand)
    os.system(scanCommand)
    return

# def test():
#     pattern = re.compile(r'^http://')
#     m = pattern.match('http://www.baidu.com')
#     n = pattern.match('hta')
#     print(m)
#     print(n)
#     return

def pppGet():
    f = open("target.txt")
    lines = f.readlines()
    pattern = re.compile(r'^http://')
    for line in lines:
        try:
            if not pattern.match(line.strip()):
                targeturl="https://"+line.strip()
            else:
                targeturl=line.strip()
            print(targeturl.strip())
            outputfilename=hashlib.md5(targeturl.encode("utf-8"))
            xrayScan(targeturl.strip(), outputfilename.hexdigest())
            # print(type(line))
        except Exception as e:
            print(e)
            pass
    f.close()
    print("Xray Scan End~")
    return

def main():
    print(logo())
    pppGet()
    return

if __name__ == '__main__':
    main()