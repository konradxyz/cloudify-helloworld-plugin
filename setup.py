from setuptools import setup

setup(

    name='cloudify-helloworld-plugin',

    version='0.1',
    packages=['helloworld_plugin'],

    zip_safe=False,
    install_requires=[
        "cloudify-plugins-common"
    ]
)
