# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_something list'] = [
    1,
    2,
    3,
    4
]

snapshots['test_mything gpg_response'] = 2

snapshots['test_add_float_numbers add_float_numbers_response'] = 4.5

snapshots['test_add_positive_numbers add_positive_numbers_respose'] = 4
