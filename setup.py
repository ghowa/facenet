from setuptools import setup, find_packages

setup(
    name='facenet',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "absl-py==0.11.0",
        "astunparse==1.6.3",
        "cachetools==4.2.1",
        "certifi==2020.12.5",
        "chardet==4.0.0",
        "cycler==0.10.0",
        "flatbuffers==1.12",
        "gast==0.3.3",
        "google-auth==1.24.0",
        "google-auth-oauthlib==0.4.2",
        "google-pasta==0.2.0",
        "grpcio==1.32.0",
        "h5py==2.10.0",
        "idna==2.10",
        "joblib==1.0.0",
        "Keras-Preprocessing==1.1.2",
        "kiwisolver==1.3.1",
        "Markdown==3.3.3",
        "matplotlib==3.3.4",
        "numpy==1.19.5",
        "oauthlib==3.1.0",
        "opencv-python==4.5.1.48",
        "opt-einsum==3.3.0",
        "Pillow==8.1.0",
        "protobuf==3.14.0",
        "pyasn1==0.4.8",
        "pyasn1-modules==0.2.8",
        "pyparsing==2.4.7",
        "python-dateutil==2.8.1",
        "requests==2.25.1",
        "requests-oauthlib==1.3.0",
        "rsa==4.7",
        "scikit-learn==0.24.1",
        "scipy==1.6.0",
        "six==1.15.0",
        "tensorboard==2.4.1",
        "tensorboard-plugin-wit==1.8.0",
        "tensorflow==2.4.1",
        "tensorflow-estimator==2.4.0",
        "termcolor==1.1.0",
        "threadpoolctl==2.1.0",
        "typing-extensions==3.7.4.3",
        "urllib3==1.26.3",
        "Werkzeug==1.0.1",
        "wrapt==1.12.1",
    ]
)