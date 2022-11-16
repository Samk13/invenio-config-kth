# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from invenio_communities.permissions import CommunityPermissionPolicy
from invenio_rdm_records.services import RDMRecordPermissionPolicy
from invenio_records_permissions.generators import SystemProcess
from invenio_requests.services.permissions import (
    PermissionPolicy as RequestsPermissionPolicy,
)

from .generators import Administration, CommunityManager, DisableIfReadOnly


class KTHCommunitiesPermissionPolicy(CommunityPermissionPolicy):
    """Communities permission policy of KTH."""

    # current state: invenio-communities v3.2.3
    # fmt: off
    # can create Should replace all needs
    can_create =           [Administration(), CommunityManager(), SystemProcess(), DisableIfReadOnly()]  # noqa
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


class KTHRecordPermissionPolicy(RDMRecordPermissionPolicy):
    """Record permission policy of KTH.

    Access control configuration for records.
    Note that even if the array is empty, the invenio_access Permission class
    always adds the ``superuser-access``, so admins will always be allowed.
    """

    # current state: invenio-rdm-records v1.0.1

    # can_manage[1] -> CommunityAction("curate")
    # This will enable curators to publish records

    # fmt: off
    can_publish = [RDMRecordPermissionPolicy.can_manage[1]] + [Administration(), CommunityManager(), SystemProcess(), DisableIfReadOnly()]
    # fmt: on


class KTHRequestsPermissionPolicy(RequestsPermissionPolicy):
    """Requests permission policy of KTH."""

    # disable write operations if the system is in read-only mode
    # current state: invenio-requests v1.0.2

    # fmt: off
    can_create         = RequestsPermissionPolicy.can_create         + [DisableIfReadOnly()]
    # fmt: on
