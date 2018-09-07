from libs import Utility
import os
import subprocess

workspace_path = '/home/bspserver/sda/C2_SourceCode/c2_userdebug_20180907.170246/'
os.chdir(workspace_path)

envsetup_command = "source build/envsetup.sh"
link_command = "source build/link.sh"
lunch_command = "lunch g2-userdebug general"
ulimit_command = "ulimit -c unlimited"
update_command = "make update-api -j8"
make_command = "make -j8"

commands = [
    envsetup_command,
    link_command,
    lunch_command,
    ulimit_command,
    update_command,
    make_command
]
command = " && ".join(commands)

command_exit_code = Utility.execute_command(cmd=command)
if command_exit_code != 0:
    raise IOError
