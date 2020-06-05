# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetFormAPITestCase::test_case status'] = 200

snapshots['TestCase01GetFormAPITestCase::test_case body'] = {
    'questions_list': [
        {
            'description': 'string',
            'mcq_details': [
                'string'
            ],
            'question_id': 1,
            'question_title': 'string',
            'required': True
        }
    ]
}

snapshots['TestCase01GetFormAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '128',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
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
