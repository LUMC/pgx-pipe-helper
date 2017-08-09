from setuptools import setup
setup(
    name="pipe_helper",
    version="0.0.1",
    description="Simple helper for common functionality",
    autor="Guy Allard",
    author_email="w.g.allard AT lumc DOT nl",
    url="https://git.lumc.nl/wgallard/pipe_helper.git",
    license="MIT",
    platforms=['linux'],
    packages=["pipe_helper"],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Operating System :: Linux',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'License :: MIT License',
    ],
    keywords = 'bioinformatics snakemake'
)
