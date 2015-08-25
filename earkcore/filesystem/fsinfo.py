import os,sys
import json
from earkcore.utils.fileutils import remove_protocol

def path_to_dict(path):
    import sys
    reload(sys)
    sys.setdefaultencoding('utf8')
    d = {'text': os.path.basename(unicode(path).encode('utf-8'))}
    if os.path.isdir(unicode(path).encode('utf-8')):
        d['icon'] = "glyphicon glyphicon-folder-close"
        d['children'] = [path_to_dict(os.path.join(unicode(path).encode('utf-8'),x)) for x in os.listdir(unicode(path).encode('utf-8'))]
    else:
        d['icon'] = "glyphicon glyphicon-file"
    return d

def fsize(file_path, wd=None):
    fp = remove_protocol(file_path)
    path = fp if wd is None else os.path.join(wd,fp)
    return int(os.path.getsize(path))

def main():
    print json.dumps(path_to_dict('.'), indent=4, sort_keys=False)
    print fsinfo

if __name__ == "__main__":
    main()
