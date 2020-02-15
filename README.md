Computer Vision
===============

The intention of this "Computer Vision" project is to explain in an easy and structured way the common techniques and libraries used in the field of artificial vision. It was thought to people had a series of introductory notebooks to this field of vision. It provides definitions of basic techniques, image descriptors, feature extraction and Content base image retrieval. This repository will be extended with an explanation of the deep learning field.

Entorno Virtual
===============

To create the virtual environment, we have to have anaconda previously installed on our computer.

1. [Descargar anaconda](https://www.anaconda.com/download/)

Create the virtual environment using the * environment.yml * file (contains all the dependencies of conda and pip packages)
`conda env create --file environment.yml`

To activate the created environment
`activate computer-vision-env`

To deactivate the current environment

`deactivate computer-vision-env`

To update the environment with new dependencies (the current environment must be disabled)
`conda env update --file environment.yml`