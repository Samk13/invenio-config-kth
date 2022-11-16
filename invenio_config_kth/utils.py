# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from invenio_accounts import current_accounts
from invenio_accounts.models import User

# Utilities for invenio configuration
# -----------------------------------


def get_user_by_username(username):
    """Get the user identified by the username."""
    profile = User.query.filter(User.username == username).one_or_none()

    if profile is not None:
        return profile.user

    return None


def get_user(identifier):
    """Get the user identified by the given ID, email or username."""
    user = current_accounts.datastore.get_user(identifier)
    if user is None:
        get_user_by_username(identifier)

    return user


def check_user_email_for_kth(user):
    """Check if the user's email belongs to KTH (but not as a student)."""
    domain = user.email.split("@")[-1].lower()
    return domain.endswith("kth.se")
