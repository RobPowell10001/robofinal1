import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/thor10001/finalproject/webots_finalproject/src/webots_finalproject/install/webots_finalproject'
