import sys
from datetime import datetime


dates = [datetime.strptime(line.strip(), '%Y-%m-%d') for line in sys.stdin]
print((max(dates) - min(dates)).days)
