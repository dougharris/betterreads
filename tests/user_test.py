from unittest import skip

from nose.tools import eq_, ok_

from betterreads.user import GoodreadsUser
from betterreads.group import GoodreadsGroup
from betterreads.owned_book import GoodreadsOwnedBook
from betterreads.review import GoodreadsReview
from betterreads.shelf import GoodreadsShelf
from tests.test_fixture import GoodreadsTestClass


class TestUser(GoodreadsTestClass):
    @classmethod
    def setup_class(cls):
        GoodreadsTestClass.setup_class()
        cls.user = cls.client.user("1")

    def test_repr(self):
        eq_(repr(self.user), "otis")

    @skip("Disabled until tests run on fixtures, not live API calls")
    def test_repr_withou_user_name(self):
        user = self.client.auth_user()
        eq_(repr(user), "18185439")

    def test_get_user(self):
        ok_(isinstance(self.user, GoodreadsUser))
        eq_(self.user.gid, "1")

    def test_user_name(self):
        eq_(self.user.user_name, "otis")

    def test_name(self):
        eq_(self.user.name, "Otis Chandler")

    def test_link(self):
        eq_(self.user.link, u"https://www.goodreads.com/user/show/1-otis-chandler")

    def test_image_url(self):
        eq_(
            self.user.image_url,
            u"https://images.gr-assets.com/users/1506617226p3/1.jpg",
        )

    def test_small_image_url(self):
        eq_(
            self.user.small_image_url,
            u"https://images.gr-assets.com/users/1506617226p2/1.jpg",
        )

    def test_user_in_groups(self):
        groups = self.user.list_groups()
        ok_(all(isinstance(group, GoodreadsGroup) for group in groups))

    def test_user_not_in_any_group(self):
        user = self.client.user("25044452")  # A user with no joined groups
        eq_(user.list_groups(), [])

    def test_user_own_books(self):
        owned_books = self.user.owned_books()
        print(owned_books)
        ok_(all(isinstance(book, GoodreadsOwnedBook) for book in owned_books))

    def test_reviews(self):
        reviews = self.user.reviews()
        ok_(all(isinstance(review, GoodreadsReview) for review in reviews))

    def test_shelves(self):
        shelves = self.user.shelves()
        ok_(all(isinstance(shelf, GoodreadsShelf) for shelf in shelves))
