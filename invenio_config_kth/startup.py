# -*- coding: utf-8 -*-
#
# Copyright (C) 2022 KTH Royal Institute of Technology Sweden
#
# invenio-config-kth is free software, you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file details.

from flask import Blueprint

from .permissions import KTHCommunitiesPermissionPolicy

blueprint = Blueprint("invenio_config_kth_startup", __name__)


@blueprint.record_once
def override_communities_permissions(state):
    """Override permission policy class for communities."""
    # TODO change this as soon as Invenio-Communities allows to do it via config
    app = state.app
    communities = app.extensions.get("invenio-communities", None)
    assert communities is not None

    # Override the permission policy class for all communities services
    svc = communities.service
    svc.config.permission_policy_cls = KTHCommunitiesPermissionPolicy
    svc.files.config.permission_policy_cls = KTHCommunitiesPermissionPolicy
    svc.members.config.permission_policy_cls = KTHCommunitiesPermissionPolicy
