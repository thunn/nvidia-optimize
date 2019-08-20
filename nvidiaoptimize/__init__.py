import os
import subprocess

dir_path = os.path.dirname(os.path.realpath(__file__))
script = os.path.join(dir_path, 'nvidiaoptimize.sh')

subprocess.call([script])