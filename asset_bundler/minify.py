import os
import subprocess

def javascript(script_filenames):
    command = 'java -jar lib/closurecompiler/compiler.jar'
    for filename in script_filenames:
        if os.path.isfile(filename):
            command += ' --js=%(filename)s' % {'filename': filename}

    command += ' >> temp.js'
    subprocess.call(command, shell=True)

def styles(style_filenames):
    def concatenate_stylesheets(filenames):
        subprocess.call('echo '' > temp.css', shell=True)

        for filename in filenames:
            if filename.endswith('.less'):
                subprocess.call(
                    'java -jar lib/lesscssengine/lesscss-engine-1.1.4-jar-with-dependencies.jar %(filename)s >> temp.css' % { 'filename': filename },
                    shell=True
                )
            else:
                subprocess.call(
                    'cat %(filename)s >> temp.css' % { 'filename': filename },
                    shell=True
                )
    def minify_stylesheet():
        filename = 'temp.css'
        #under construction lol
        subprocess.call(
            'cat %(filename)s >> temp.css' % { 'filename': filename },
            shell=True
        )


    concatenate_stylesheets(style_filenames)
    #minify_stylesheet()