from setuptools import Extension, setup, find_packages


module_ext = Extension('wincext.ccode',
                       sources=['wincext/ccode/ccode.c'],
                       include_dirs=['wincext/ccode'],
                       )

setup(
    name="wincext",
    version="0.1",
    author="Gregor Patof",
    description="Just a test for a C extension in a cross-platform module",
    packages=find_packages(),
    package_data={'wincext': ['ccode/*.c', 'ccode/*.h']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    ext_modules=[module_ext],
    python_requires='>=3.6',
)