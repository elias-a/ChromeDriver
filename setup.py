import setuptools

with open("README.md", "rt", encoding="utf-8") as f:
    description = f.read()

setuptools.setup(
    name="ChromeDriver",
    version="0.0.1",
    author="Elias Alstead",
    author_email="elias.alstead@gmail.com",
    description="",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/elias-a/ChromeDriver",
    license="MIT",
    packages=["ChromeDriver"],
    package_dir={ "" : "src" },
    install_requires=["selenium"],
)

