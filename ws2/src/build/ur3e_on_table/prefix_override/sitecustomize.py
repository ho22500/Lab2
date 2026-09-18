import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/shay/a/ho225/ece569-fall2026/Lab2/ws2/src/install/ur3e_on_table'
