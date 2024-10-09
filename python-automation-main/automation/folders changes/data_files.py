from pathlib import Path
from datetime import datetime

path = Path("automation\\folders changes\\files")
stats =path.stat()

second = stats.st_ctime
date_created = datetime.fromtimestamp(second)
date_created_str = date_created.strftime("%Y-%m-%d_%H:%M:%S")

print(stats)
print(second)
print(date_created)
print(date_created_str)