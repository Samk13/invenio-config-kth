# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.


from .permissions import KTHRecordPermissionPolicy, KTHRequestsPermissionPolicy

# KTH Invenio config
# =================
CONFIG_KTH_COMMUNITY_MANAGER_ROLE = "community-admin"
CONFIG_KTH_READ_ONLY_MODE = False


# Invenio-Records
# ================
RDM_PERMISSION_POLICY = KTHRecordPermissionPolicy


# Invenio-Requests
# ================
REQUESTS_PERMISSION_POLICY = KTHRequestsPermissionPolicy
