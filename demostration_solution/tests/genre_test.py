from unittest.mock import MagicMock

import pytest as pytest

from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.genre import Genre
from demostration_solution.service.genre import GenreService
from demostration_solution.setup_db import db


@pytest.fixture()
def genre_dao():
    gd = GenreDAO(db.session)
    genre1 = Genre(id=1, name='test_genre1')
    genre2 = Genre(id=2, name='test_genre2')
    genre3 = Genre(id=3, name='test_genre3')

    gd.get_one = MagicMock(return_value=genre1)
    gd.get_all = MagicMock(return_value=[genre1, genre2, genre3])
    gd.create = MagicMock()
    gd.update = MagicMock()
    gd.delete = MagicMock(return_value=Genre(id=3))
    return gd


class TestGenreService():
    @pytest.fixture()
    def genre_service(self, genre_dao):
        genre_service = GenreService(dao=genre_dao)
        return genre_service

    def test_get_one(self, genre_service):
        assert genre_service.get_one(1).name == 'test_genre1'
        assert genre_service.get_one(1) is not None
        assert genre_service.get_one(1).id is not None

    def test_get_all(self, genre_service):
        assert genre_service.get_all() is not None
        assert genre_service.get_all()[0] is not None
        assert genre_service.get_all()[0].id is not None

    def test_create(self, genre_service):
        data = {'id': 100, 'name': '123'}
        assert genre_service.create(data) is not None

    def test_update(self, genre_service):
        assert genre_service.update({"id": 1, "name": '123'}) is not None

    def test_delete(self, genre_service):
        assert genre_service.delete(1) is None
