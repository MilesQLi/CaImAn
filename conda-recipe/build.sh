#!/bin/bash

echo "Running bash.sh"
#conda env update -f environment_mac.yml
#conda install -c conda-forge tensorflow -y
#conda install -c conda-forge keras -y
#conda install -c menpo opencv3=3.1.0 -y
#conda install -c menpo opencv3 -y

#$PYTHON setup.py build_ext -i
$PYTHON setup.py install  # --single-version-externally-managed --record=record.txt
$PYTHON setup.py build_ext -i

mkdir notebook_interface
cp -a $SRC_DIR/nb_interface/. $PREFIX/bin/nb_interface
