# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
"""KTH Permissions."""

from .generators import DisableIf, DisableIfReadOnly
from .policies import (
    KTHCommunitiesPermissionPolicy,
    KTHRecordPermissionPolicy,
    KTHRequestsPermissionPolicy,
)

__all__ = (
    "KTHCommunitiesPermissionPolicy",
    "KTHRecordPermissionPolicy",
    "KTHRequestsPermissionPolicy",
    "DisableIfReadOnly",
    "DisableIf",
)
