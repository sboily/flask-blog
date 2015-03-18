#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup


setup(
    name='flask_blog',
    version='0.1',

    description='Flask blog',

    author='Sylvain Boily',
    author_email='sboily@avencall.com',

    url='https://github.com/sboily/flask-blog',

    packages=find_packages(),

    entry_points={
        'flask_blog.plugins': [
            'home = flask_blog.plugins.home.load:init_app',
            'about = flask_blog.plugins.about.load:init_app',
            'contact = flask_blog.plugins.contact.load:init_app',
            'posts = flask_blog.plugins.posts.load:init_app',
            'users = flask_blog.plugins.users.load:init_app',
            'installation = flask_blog.plugins.installation.load:init_app',
            'settings = flask_blog.plugins.settings.load:init_app',
        ]
    }
)
