#coding:utf-8
import click
import glob
import os
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

@click.command()
# @click.option('--input_path',help=unicode("content的路径", errors='ignore'))
# @click.option('--result',help=unicode("json输出结果文件", errors='ignore'))
@click.option('--input_path',default='content',help="content的路径")
@click.option('--result',default='public/search_lunr/data.json',help="json输出结果文件")
def tojson(input_path,result):
    temp_dir = 'test'
    if os.path.exists(temp_dir):
        pass
    else:
        os.mkdir(temp_dir)

    for fn in os.listdir(input_path):
        input_path2 = os.path.join(input_path,fn)
        if os.path.isdir(input_path2):
            dir_num = 0
            for fn2 in os.listdir(input_path2):
                input_path3 = os.path.join(input_path2, fn2)
                if os.path.isdir(input_path3):
                    dir_num +=1
                    result_json = '%s/%s-%s.json' % (temp_dir,fn,fn2)
                    context_path = '/%s/%s/' %(fn,fn2)
                    cmd = "hugo-lunr-zh  -o %s --matter-delims --- --matter-type yaml -d %s -c %s" % (result_json,input_path3,context_path)
                    os.system(cmd)
            if dir_num == 0:
                result_json = '%s/%s.json' % (temp_dir,fn)
                context_path = '/%s/' %(fn)
                cmd = "hugo-lunr-zh  -o %s --matter-delims --- --matter-type yaml -d %s -c %s" % (result_json,input_path2,context_path)
                os.system(cmd)

    result_list = []
    for one_result in os.listdir(temp_dir):
        if one_result.startswith('.'):
            continue
        one_result2 = os.path.join(temp_dir,one_result)
        with open(one_result2,'r') as data1:
            data_string1 = json.load(data1)
            result_list += data_string1

    with open(result, 'w') as data3:
        json_info = json.dumps(result_list, ensure_ascii = False).encode('utf-8')
        data3.write(unicode(json_info))


def test1():
    pass
    # python create_json.py --input_path content --result public/search_lunr/data.json

if __name__ == "__main__":
    tojson()
 