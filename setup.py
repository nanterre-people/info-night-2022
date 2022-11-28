from setuptools import setup, find_packages

INSTALL_REQUIRES = [
    'fastapi',
    'uvicorn',
    'pydantic',
    'sqlalchemy',
]

setup(
    name='backend',
    version='0.1',
    description='Backend for the project',
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    entry_points={
        'console_scripts': [
            'night = backend.main:main',
        ],
    },
    extras_require={
        'dev': [
            'mypy',
            'pytest'
        ]
    }
)