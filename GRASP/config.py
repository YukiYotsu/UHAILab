"""
This is the config file to define the names of files.
"""
import sys
import os
from pathlib import Path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

grandparent_directory = Path(__file__).resolve().parent.parent
# you can define here the file which has users-defined words
USER_DEFINED_CORRECTIONS_FILE_Path = os.path.join(grandparent_directory,'user_defined.csv')