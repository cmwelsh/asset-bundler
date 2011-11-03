import os
import subprocess

def javascript(script_filenames):
    command = 'java -jar lib/closurecompiler/compiler.jar'
    for filename in script_filenames:
        if os.path.isfile(filename):
            command += ' --js=%(filename)s' % {'filename': filename}

    print command
    subprocess.call(command, shell=True)