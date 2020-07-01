# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetProfileAPITestCase::test_case status'] = 200

snapshots['TestCase01GetProfileAPITestCase::test_case body'] = {
    'is_admin': False,
    'user_id': 1,
    'username': 'username'
}

snapshots['TestCase01GetProfileAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '57',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}

snapshots['TestCase01GetProfileAPITestCase::test_case name'] = 'username'

snapshots['TestCase01GetProfileAPITestCase::test_case id'] = 1

snapshots['TestCase01GetProfileAPITestCase::test_case is_admin'] = False
