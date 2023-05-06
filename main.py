import setuptools
import os, sys
import subprocess
import tornado
import tornado.web
import asyncio

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

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])
async def asleep (y):
    await asyncio.sleep(y)
async def go(x, y):
    print(x)
    await asleep (y)
    pass
async def goo():
    await asyncio.gather(
            *(go (i, i ) for i in range(90))
            )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    asyncio.run (goo())
