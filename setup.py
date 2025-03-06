from setuptools import setup, find_packages


setup(
    name='heic_converter_cli',
    version="0.1",
    packages=find_packages(),
    author="zackey-heuristics",
    install_requires=["pyheif", "Pillow"],
    description="HEIC Easy Image Converter",
    include_package_data=True,
    url='https://github.com/zackey-heuristics/heic_converter_cli',
    entry_points = {'console_scripts': ['heic_converter_cli = heic_converter_cli.core:main']},
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
    ],
)
