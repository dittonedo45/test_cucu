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
main()
