from os.path import dirname, abspath
import subprocess

subprocess.Popen(['git', 'apply', './opt/fix_build.patch'], cwd = dirname(dirname(abspath(__file__))))