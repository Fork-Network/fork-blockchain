import os
from pathlib import Path

DEFAULT_ROOT_PATH = Path(os.path.expanduser(os.getenv("TACO_ROOT", "~/.fork/mainnet"))).resolve()
