import pytest
from blog.factories import PostFactory
from datetime import datetime

@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')

@pytest.fixture
def post_draft():
    return PostFactory(title='Draft Post', published_date=None)

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'

@pytest.mark.django_db
def test_post_has_published_date(post_published):
    assert post_published.published_date is not None
    assert isinstance(post_published.published_date, datetime)

@pytest.mark.django_db
def test_post_has_slug(post_published):
    assert post_published.slug is not None
    assert post_published.slug == 'pytest-with-factory'

@pytest.mark.django_db
def test_create_draft_post(post_draft):
    assert post_draft.title == 'Draft Post'
    assert post_draft.published_date is None
