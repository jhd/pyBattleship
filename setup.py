try:
    from setuptools import setup
except ImportError:
    from distuils.core import setup
    
config = {
    'description': 'My Project',
    'author': 'JHD',
    'author_email': 'jonathanhennessydoylety@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['Battleship'],
    'scripts': ['control'],
    'name': 'Battleship'
}

setup(**config)
