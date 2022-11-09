# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from invenio_communities.permissions import CommunityPermissionPolicy
from invenio_records_permissions.generators import SystemProcess

from .generators import Administration, DisableIfReadOnly


class KTHCommunitiesPermissionPolicy(CommunityPermissionPolicy):
    """Communities permission policy of KTH."""

    # fmt: off
    # can create Should replace all
    can_create =                               [Administration(), SystemProcess(), DisableIfReadOnly()]  # noqa
    can_update              = CommunityPermissionPolicy.can_update              + [DisableIfReadOnly()]  # noqa
    can_delete              = CommunityPermissionPolicy.can_delete              + [DisableIfReadOnly()]  # noqa
    can_rename              = CommunityPermissionPolicy.can_rename              + [DisableIfReadOnly()]  # noqa
    can_submit_record       = CommunityPermissionPolicy.can_submit_record       + [DisableIfReadOnly()]  # noqa
    can_members_add         = CommunityPermissionPolicy.can_members_add         + [DisableIfReadOnly()]  # noqa
    can_members_invite      = CommunityPermissionPolicy.can_members_invite      + [DisableIfReadOnly()]  # noqa
    can_members_manage      = CommunityPermissionPolicy.can_members_manage      + [DisableIfReadOnly()]  # noqa
    can_members_bulk_update = CommunityPermissionPolicy.can_members_bulk_update + [DisableIfReadOnly()]  # noqa
    can_members_bulk_delete = CommunityPermissionPolicy.can_members_bulk_delete + [DisableIfReadOnly()]  # noqa
    can_members_update      = CommunityPermissionPolicy.can_members_update      + [DisableIfReadOnly()]  # noqa
    can_members_delete      = CommunityPermissionPolicy.can_members_delete      + [DisableIfReadOnly()]  # noqa
    can_invite_owners       = CommunityPermissionPolicy.can_invite_owners       + [DisableIfReadOnly()]  # noqa
    can_featured_create     = CommunityPermissionPolicy.can_featured_create     + [DisableIfReadOnly()]  # noqa
    can_featured_update     = CommunityPermissionPolicy.can_featured_update     + [DisableIfReadOnly()]  # noqa
    can_featured_delete     = CommunityPermissionPolicy.can_featured_delete     + [DisableIfReadOnly()]  # noqa
    # fmt: on
