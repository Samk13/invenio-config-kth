# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from flask_babelex import gettext as _

from .permissions import KTHRecordPermissionPolicy, KTHRequestsPermissionPolicy

# KTH Invenio config
# =================

CONFIG_KTH_READ_ONLY_MODE = False


# Invenio-Records
# ================
RDM_PERMISSION_POLICY = KTHRecordPermissionPolicy


# Invenio-Requests
# ================
REQUESTS_PERMISSION_POLICY = KTHRequestsPermissionPolicy

# SQLALCHEMY_ECHO = True
# Invenio-Mail
# ============

SECURITY_EMAIL_SUBJECT_REGISTER = _("Welcome to KTH RDM! 🎉")
"""Email subject for account registration emails."""
