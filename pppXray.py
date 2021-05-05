import hashlib
import re
import time
import os
import click
import config

@click.command()
@click.option('-r', '--readfile',default='target.txt',help='xray批量扫描读取文件名,按行读取',type=str)
@click.option('--plugins',help='自定义xray插件 plugins')
def init(readfile,plugins):
    """pppXray : xray 批量扫描\n
       https://github.com/Cl0udG0d/pppXray
    """
    try:
        if not os.path.exists(config.saveDir):
            os.makedirs(config.saveDir)
        config.targetFileName=readfile
        if plugins:
            config.plugins=plugins
        click.echo("读取文件 {} ".format(readfile))
    except Exception as e:
        print(e)
        pass


def advancedMergeReport(tempTypeResult,bugTypeSet):
    pattern2 = re.compile(r'"plugin":"(.*?)"')
    tempType = pattern2.findall(tempTypeResult)[0]
    path = os.path.join(config.saveDir, tempType)
    context = ""
    if tempType not in bugTypeSet:
        bugTypeSet.add(tempType)
        os.makedirs(path)
        with open("{}\\advancedModelFile.html".format(config.RootPath), 'r', encoding='utf-8') as f:
            context += f.read()
        result = "<script class=\'web-vulns\'>webVulns.push({})</script>".format(tempTypeResult)
        context += result
        with open("{}\\{}.html".format(path, tempType), 'w', encoding='utf-8') as f:
            f.write(context)
    else:
        result = "<script class=\'web-vulns\'>webVulns.push({})</script>".format(tempTypeResult)
        context += result
        with open("{}\\{}.html".format(path, tempType), 'a+', encoding='utf-8') as f:
            f.write(context)



def communityMergeReport(tempTypeResult,bugTypeSet):
    pattern2 = re.compile(r'"plugin":"(.*?)"')
    tempType = pattern2.findall(tempTypeResult)[0]
    path = os.path.join(config.saveDir, tempType)
    context = ""
    if tempType not in bugTypeSet:
        bugTypeSet.add(tempType)
        os.makedirs(path)
        with open("{}\\communityModelFile.html".format(config.RootPath), 'r', encoding='utf-8') as f:
            context += f.read()
        result = "<script class=\'web-vulns\'>webVulns.push({})</script>".format(tempTypeResult)
        context += result
        with open("{}\\{}.html".format(path, tempType), 'w', encoding='utf-8') as f:
            f.write(context)
    else:
        result = "<script class=\'web-vulns\'>webVulns.push({})</script>".format(tempTypeResult)
        context += result
        with open("{}\\{}.html".format(path, tempType), 'a+', encoding='utf-8') as f:
            f.write(context)
    return



def assortReport():
    '''
    对 save 文件夹下的漏洞文件进行分类
    依托 "plugin"
    :return:
    '''
    bugTypeSet=set()
    bugReportList=os.listdir(config.saveDir)
    pattern = re.compile(r'<script class=\'web-vulns\'>webVulns.push\((.*?)\)</script>')
    # pattern2 = re.compile(r'"plugin":"(.*?)"')
    for tempReport in bugReportList:
        tempReportPath=os.path.join(config.saveDir,tempReport)
        with open(tempReportPath,'r',encoding='utf-8') as f:
            temp=f.read()
            result=pattern.findall(temp)
            tempResult = eval(result[0])
            if 'snapshot' in tempResult["detail"]:
                for tempTypeResult in result:
                    communityMergeReport(tempTypeResult, bugTypeSet)
            else:
                for tempTypeResult in result:
                    advancedMergeReport(tempTypeResult, bugTypeSet)


def xrayScan(targeturl,outputfilename="test"):
    scanCommand = "xray.exe webscan {} --basic-crawler {} --html-output {}\\{}.html".format('--plugins {}'.format(config.plugins) if config.plugins else '',targeturl, config.saveDir,
                                                                                         outputfilename)
    print(scanCommand)
    os.system(scanCommand)
    return


def pppGet():
    f = open(config.targetFileName)
    lines = f.readlines()
    pattern = re.compile(r'^http')
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
    try:
        print(config.logo())
        init.main(standalone_mode=False)
        pppGet()
        assortReport()
    except Exception as e:
        print(e)
        pass
    return

if __name__ == '__main__':
    main()