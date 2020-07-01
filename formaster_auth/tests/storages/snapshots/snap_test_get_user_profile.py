# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetUserProfile.test_get_user_profile user_profile_dto'] = GenericRepr("UserDetailsDto(user_id=1, username='username', is_admin=True)")
