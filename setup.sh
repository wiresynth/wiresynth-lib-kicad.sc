#!/bin/sh

LIB_VERSION=9.0.3

git clone https://gitlab.com/kicad/libraries/kicad-symbols --depth 1 --branch $LIB_VERSION
git clone https://gitlab.com/kicad/libraries/kicad-footprints --depth 1 --branch $LIB_VERSION

ROOT=`readlink -f $(dirname $0)`

cd $ROOT/kicad-footprints
$ROOT/kicad-footprint-gen.py $ROOT/src/wiresynth/lib/kicad/footprint *.pretty/*.kicad_mod

cd $ROOT/src/wiresynth/lib/kicad/part
$ROOT/kicad-symbol-gen.py $ROOT/kicad-symbols/*.kicad_sym
