# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from contextlib import contextmanager

from flask import template_rendered
import pytest

from main import app as flask_app


@pytest.fixture
def app():
    """
    fixture connecting Flask app
    """
    yield flask_app


@contextmanager
def captured_templates(app):
    """
    capture template render requests
    """
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)


def test_translate_get(app):
    """
    test GET request to main application
    """
    with captured_templates(app) as templates:
        rv = app.test_client().get('/')
        assert rv.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'index.html'
        assert 'orig' in context and 'trans' in context
        assert len(context['orig']) == len(context['trans']) == 2


def test_translate_post(app):
    """
    test POST request to main application
    """
    SOURCE, TARGET = 'hello world', 'Hola Mundo'
    with captured_templates(app) as templates:
        rv = app.test_client().post('/', data={'text': SOURCE})
        assert rv.status_code == 200
        assert len(templates) == 1
        template, context = templates[0]
        assert template.name == 'index.html'
        assert 'orig' in context and 'trans' in context
        assert context['orig']['text'] == SOURCE
        assert context['trans']['text'] == TARGET
