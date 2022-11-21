# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from flask import current_app
from flask_principal import RoleNeed
from invenio_access import action_factory
from invenio_access.permissions import any_user
from invenio_records_permissions.generators import Generator

administration_access_action = action_factory("administration-access")


class Administration(Generator):
    """Allows administration-access."""

    def __init__(self):
        """Constructor."""
        super(Administration, self).__init__()

    def needs(self, **kwargs):
        """Enabling Needs."""
        return [administration_access_action]


class CommunityManager(Generator):
    """Allows users with the "trusted-user" role."""

    def needs(self, record=None, **kwargs):
        """Enabling Needs."""
        role_name = current_app.config.get(
            "CONFIG_KTH_COMMUNITY_MANAGER_ROLE", "community-manager"
        )
        return [RoleNeed(role_name)]


class DisableIf(Generator):
    """Denies ALL users including super users, if a condition is met."""

    def __init__(self, check=lambda: True):
        """Constructor."""
        super().__init__()
        self.check = check

    def excludes(self, **kwargs):
        """Preventing Needs."""
        if self.check():
            return [any_user]
        else:
            return []


def DisableIfReadOnly():
    """Disable permissions for everybody if the repository is set as read only."""
    return DisableIf(lambda: current_app.config.get("CONFIG_KTH_READ_ONLY_MODE", False))
