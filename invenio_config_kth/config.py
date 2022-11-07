# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from flask_babelex import gettext as _

# Invenio-Previewer
# =================

PREVIEWER_MAX_IMAGE_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB

PREVIEWER_MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB


# Invenio-Mail
# ============

SECURITY_EMAIL_SUBJECT_REGISTER = _("Welcome to KTH RDM! 🎉")
"""Email subject for account registration emails."""
