import os


RootPath = os.path.dirname(os.path.abspath(__file__))
saveDir = "{}\\save".format(RootPath)
# saveXrayReport = '{}\\save\\xrayReport'.format(RootPath)

targetFileName=""
plugins=""

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
                            v1.1
                            author:springbird
    '''
    return logo