import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/vision/slamcore/git_codes/empty-odom-publisher/install/publisherodometry'
