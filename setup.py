from distutils.core import setup

#Esta clase se utiliza para generar el .ex ,python setup.py sdist, python setup.py install
#pero solo genera un targz con una clase y un script

setup(name="Clinica Dental",
      version="0.1",
      description="software para la gestion de una clinica dental",
      author="Marcos Cividanes",
      author_email="mcividanes",
      url="http://mundogeek.net/tutorial-python/",
      license="GPL",
      scripts=["setup.py"],
      py_modules=["Metodos"]
)