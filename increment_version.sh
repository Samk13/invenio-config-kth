#!/bin/bash

# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.


# check if a path to __init__.py is provided as required first arg
if [ -z "$1" ]; then
    echo "Error: Please provide a path to __init__.py as the first argument."
    exit 1
fi

# check if a path to -ma -mi -pa is provided as optional second arg
increment='patch'
if [ "$2" == "-ma" ]; then
    increment='major'
elif [ "$2" == "-mi" ]; then
    increment='minor'
fi

# read version from __init__.py
version=$(grep -o '[0-9]\+\.[0-9]\+\.[0-9]\+' $1)
IFS='.' read -r -a version_parts <<< "$version"

# increment the provided path version with respective arg
# if no second arg provided default to -pa or patch increment
major=${version_parts[0]}
minor=${version_parts[1]}
patch=${version_parts[2]}

if [ "$increment" == "major" ]; then
    major=$((major + 1))
    minor=0
    patch=0
elif [ "$increment" == "minor" ]; then
    minor=$((minor + 1))
    patch=0
else
    patch=$((patch + 1))
fi

# update __init__.py with the new version
new_version="$major.$minor.$patch"
sed -i "s/$version/$new_version/g" $1

echo "The version number in $1 has been incremented to $new_version"