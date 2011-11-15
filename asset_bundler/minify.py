import os
import subprocess

def javascript(script_filenames):
    output_filename = 'site.min.js'
    # erase file
    subprocess.call('echo '' > %(filename)s' % { 'filename': output_filename }, shell=True)
    # run closure compiler
    command = 'java -jar lib/closurecompiler/compiler.jar'
    for filename in script_filenames:
        if os.path.isfile(filename):
            command += ' --js=%(filename)s' % {'filename': filename}

    command += (' >> %(output_filename)s' %
        {
            'output_filename': output_filename
        }
    )
    
    subprocess.call(command, shell=True)
    subprocess.call('gzip -c site.min.js > site.min.gz.js', shell=True)

def styles(style_filenames):
    def concatenate_stylesheets(filenames):
        # FIXME: directly appending the binary contents is an invalid way to
        #        concatenate text files, but the step after this will fix the
        #        byte order mark (BOM) and all that stuff
        output_filename = 'concat.css'
        subprocess.call('echo '' > %(filename)s' % { 'filename': output_filename }, shell=True)

        for filename in filenames:
            if filename.endswith('.less'):
                subprocess.call(
                    'java -jar lib/lesscssengine/lesscss-engine-1.1.4-jar-with-dependencies.jar %(filename)s >> %(output_filename)s' %
                        {
                            'filename': filename,
                            'output_filename': output_filename
                        },
                    shell=True
                )
            else:
                subprocess.call(
                    'cat %(filename)s >> %(output_filename)s' %
                        {
                            'filename': filename,
                            'output_filename': output_filename
                        },
                    shell=True
                )
    def minify_stylesheet():
        input_filename = 'concat.css'
        output_filename = 'site.min.css'
        subprocess.call(
            'java -jar lib/yuicompressor/yuicompressor.jar %(input_filename)s > %(output_filename)s' %
                {
                    'input_filename': input_filename,
                    'output_filename': output_filename
                },
            shell=True
        )


    concatenate_stylesheets(style_filenames)
    minify_stylesheet()

    subprocess.call('gzip -c site.min.css > site.min.gz.css', shell=True)