#!/bin/bash

IMGDIR="public/images"
MAX_JPG_SIZE=250
PNG_OPT_LVL=2

shopt -s nullglob

for image in $IMGDIR/*.{jpg,jpeg,JPG,JPEG}
do
    mogrify -resize '1400>' $image
    jpegoptim --strip-all --size=$MAX_JPG_SIZE $image
done

for image in $IMGDIR/*.{png,PNG}
do
    mogrify -resize '1400>' $image
    optipng -clobber -strip all -o $PNG_OPT_LVL $image
done

for image in $IMGDIR/subjects/*.{png,PNG}
do
    mogrify -resize '1400>' $image
    optipng -clobber -strip all -o $PNG_OPT_LVL $image
done

for image in $IMGDIR/portraits/*.{png,PNG}
do
    mogrify -resize '1400>' $image
    optipng -clobber -strip all -o $PNG_OPT_LVL $image
done

for image in $IMGDIR/portraits/*.{jpg,jpeg,JPG,JPEG}
do
    mogrify -resize '1400>' $image
    jpegoptim --strip-all --size=$MAX_JPG_SIZE $image
done

shopt -u nullglob

exit 0
