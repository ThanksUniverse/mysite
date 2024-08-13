import pytest
from blog.factories import PostFactory
from datetime import datetime

@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'

@pytest.mark.django_db
def test_post_has_published_date(post_published):
    assert post_published.created_on is not None
    assert isinstance(post_published.created_on, datetime)

@pytest.mark.django_db
def test_post_has_slug(post_published):
    assert post_published.slug is not None
    assert post_published.slug != ''
