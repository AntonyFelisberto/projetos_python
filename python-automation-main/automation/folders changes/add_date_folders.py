from pathlib import Path
from datetime import datetime

root_dir = Path("automation\\folders changes\\files")

for path in root_dir.glob("**/*"):
    if path.is_file:
        created_date = datetime.fromtimestamp(path.stat().st_ctime)
        created_date_str = created_date.strftime("%Y-%m-%d_%H:%M:%S")
        new_file = created_date_str + "_" + path.name
        new_filepath = path.with_name(new_file)
        path.rename(new_filepath)