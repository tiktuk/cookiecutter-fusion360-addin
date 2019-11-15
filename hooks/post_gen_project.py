import subprocess
import os
import uuid
import json


if __name__ == '__main__':
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])
    subprocess.call(['git', 'submodule', 'add', 'https://github.com/tapnair/apper'])

    CURDIR = os.path.realpath(os.path.curdir)

    file_path = os.path.join(CURDIR, '{{ cookiecutter.addin_name }}.manifest')
    with open(file_path, 'r+') as f:
        text = f.read()
        manifest = json.loads(text)
        manifest['id'] = str(uuid.uuid4())
        f.seek(0)
        f.write(json.dumps(manifest, indent=4, sort_keys=True))
        f.truncate()


