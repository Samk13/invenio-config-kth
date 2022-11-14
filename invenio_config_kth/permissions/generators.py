# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.
from flask import current_app
from flask_principal import RoleNeed

# from flask_resources import HTTPJSONException, create_error_handler
from invenio_access import action_factory
from invenio_access.permissions import any_user
from invenio_records_permissions.generators import Generator

# from invenio_records_resources.resources import RecordResourceConfig
# from invenio_records_resources.resources.errors import ErrorHandlersMixin

administration_access_action = action_factory("administration-access")

# class CommunityError(Exception):
#     """Base exception for community errors."""
# class PermissionDeniedError(CommunityError):
#     """The provided set spec does not exist."""

#     def __init__(self, query_arguments):
#         """Initialise error."""
#         super().__init__("A featured community entry with {q} does not exist.".format(q=query_arguments)
#         )

# error_handlers = RecordResourceConfig.error_handlers.copy()
# error_handlers.update(
#     {
#         PermissionDeniedError: create_error_handler(
#             lambda e: HTTPJSONException(
#                 code=403,
#                 description=f"This is a new error message: {e}",
#             )
#         )
#     }
# )
# class KTHErrorHandlersMixin(ErrorHandlersMixin):
#     """Mixin to define common error handlers."""
#     ErrorHandlersMixin.error_handlers["PermissionDeniedError"] = create_error_handler(
#                 HTTPJSONException(
#                     code=403,
#                     description="Permission denied.🐍",
#                 )
#             )
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
        return [RoleNeed("community-manager")]


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
