from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='ram',
    version='0.1',
    description='API wrapper for ram.moe',
    long_description=long_description,
    url='https://github.com/martmists/ram-api-wrapper',
    author='Martmists',
    author_email='martmists@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    # Add requests because it's available on both 2.7 and 3.5
    install_requires=["requests"],
    packages=["ram"],
    keywords='ram api wrapper',
    python_requires=">=3.0"
)
