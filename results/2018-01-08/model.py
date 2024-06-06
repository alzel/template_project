# This script is essentially just experiment-specific configuration
import argparse
import inspect
import json
import tempfile
from pathlib import Path

from ray import tune


_this_filename = inspect.getframeinfo(inspect.currentframe()).filename
_this_path = Path(_this_filename).parent.resolve()

data_dir=str(_this_path / 'data')
output_dir=str(_this_path / 'output')
log_dir=str(_this_path / 'logs')