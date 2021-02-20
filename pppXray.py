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
    except Exception as e:
        print(e)
        pass
    return

if __name__ == '__main__':
    main()