# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AddFormTitleAPITestCase::test_case status'] = 201

snapshots['TestCase01AddFormTitleAPITestCase::test_case body'] = {
    'form_id': 1,
    'form_title': 'my first form'
}

snapshots['TestCase01AddFormTitleAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '45',
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

snapshots['TestCase01AddFormTitleAPITestCase::test_case form title'] = 'my first form'

snapshots['TestCase01AddFormTitleAPITestCase::test_case form_id'] = 1
