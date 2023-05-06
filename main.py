import setuptools

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
def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain')]
    response_body = b'Hello, world!'
    start_response(status, headers)
    return [response_body]
main()
