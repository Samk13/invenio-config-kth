# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

# Quit on errors
set -o errexit

# Quit on unbound symbols
set -o nounset

python -m check_manifest --no-build-isolation
python -m pytest $@
tests_exit_code=$?
exit "$tests_exit_code"
