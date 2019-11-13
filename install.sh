#!/bin/bash

mkdir -p build
cd build
# build as shared library; build examples (built in ./examples,  not installed)
cmake -DBUILD_SHARED_LIBS:BOOL=ON -DMSYM_BUILD_EXAMPLES:BOOL=ON ../.
make
