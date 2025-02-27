from setuptools import find_packages, setup

setup(
    name="ir_exercise",
    version="0.1",
    description="Elasticsearch exercise for the IR course.",  # noqa
    author="Moritz Staudinger",
    author_email="moritz.staudinger@tuwien.ac.at",
    install_requires=[
        "black",
        "elasticsearch==8.4.0",
        "flask",
        "pre-commit",
        "pytest",
        "requests",
        "streamlit",
        "Wikipedia-API",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
