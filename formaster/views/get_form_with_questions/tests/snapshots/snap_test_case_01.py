# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetFormWithQuestionsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetFormWithQuestionsAPITestCase::test_case body'] = {
    'form_id': 1,
    'form_title': 'title_0',
    'question_and_response_list': [
        {
            'choices': [
            ],
            'description': 'description',
            'question_id': 1,
            'question_text': 'question_0',
            'question_type': 'WELCOME_SCREEN',
            'required': False
        },
        {
            'choices': [
            ],
            'description': 'description',
            'question_id': 2,
            'question_text': 'question_1',
            'question_type': 'LARGE_TEXT',
            'required': False
        },
        {
            'choices': [
            ],
            'description': 'description',
            'question_id': 3,
            'question_text': 'question_2',
            'question_type': 'SMALL_TEXT',
            'required': False
        },
        {
            'choices': [
            ],
            'description': 'description',
            'question_id': 4,
            'question_text': 'question_3',
            'question_type': 'MCQ',
            'required': False
        }
    ]
}

snapshots['TestCase01GetFormWithQuestionsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '652',
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
