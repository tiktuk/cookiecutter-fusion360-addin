import subprocess

if __name__ == '__main__':
    subprocess.call(['git', 'init'])
    subprocess.call(['git', 'add', '*'])
    subprocess.call(['git', 'commit', '-m', 'Initial commit'])
    subprocess.call(['git', 'submodule', 'add', 'https://github.com/tapnair/apper'])

