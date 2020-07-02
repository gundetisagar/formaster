# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetFormAPITestCase::test_case status'] = 200

snapshots['TestCase01GetFormAPITestCase::test_case body'] = {
    'forms_list': [
        {
            'form_id': 1,
            'form_title': 'title_0'
        },
        {
            'form_id': 2,
            'form_title': 'title_1'
        },
        {
            'form_id': 3,
            'form_title': 'title_2'
        },
        {
            'form_id': 4,
            'form_title': 'title_3'
        },
        {
            'form_id': 5,
            'form_title': 'title_4'
        }
    ]
}

snapshots['TestCase01GetFormAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '221',
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
