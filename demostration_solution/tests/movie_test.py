from unittest.mock import MagicMock

import pytest

from demostration_solution.dao.movie import MovieDAO
from demostration_solution.dao.model.movie import Movie
from setup_db import db


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)
    dir1 = Movie(id=1, name='Иван Иванович')
    dir2 = Movie(id=2, name='Петр Петрович')
    dir3 = Movie(id=3, name='Тест Тестович')
    movie_dao.get_one = MagicMock(return_value=dir1)
    movie_dao.get_all = MagicMock(return_value=[dir1, dir2, dir3])
    movie_dao.delete = MagicMock(return_value=dir3)
    movie_dao.create = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


from unittest.mock import MagicMock

import pytest as pytest

from demostration_solution.dao.movie import MovieDAO
from demostration_solution.dao.model.movie import Movie
from demostration_solution.service.movie import MovieService
from demostration_solution.setup_db import db


@pytest.fixture()
def movie_dao():
    gd = MovieDAO(None)
    d1 = Movie(id=1, title='movie1', description='like description test1', trailer='www.trailer_link_test1.com',
               year=1234,
               rating=2.4, genre_id=1, director_id=2)
    d2 = Movie(id=2, title='movie2', description='like description test2', trailer='www.trailer_link_test2.com',
               year=1456,
               rating=5.5, genre_id=1, director_id=2)
    d3 = Movie(id=3, title='movie3', description='like description test3', trailer='www.trailer_link_test3.com',
               year=9999,
               rating=10.0, genre_id=1, director_id=2)

    gd.get_one = MagicMock(return_value=d1)
    gd.get_all = MagicMock(return_value=[d1, d2, d3])
    gd.create = MagicMock()
    gd.update = MagicMock()
    gd.delete = MagicMock(return_value=Movie(id=3))
    return gd


class TestMovieService():
    @pytest.fixture()
    def movie_service(self, movie_dao):
        movie_service = MovieService(dao=movie_dao)
        return movie_service

    def test_get_one(self, movie_service):
        assert movie_service.get_one(1).title == 'movie1'
        assert movie_service.get_one(1) is not None
        assert movie_service.get_one(1).id is not None

    def test_get_all(self, movie_service):
        assert movie_service.get_all() is not None
        assert movie_service.get_all()[0] is not None
        assert movie_service.get_all()[0].id is not None

    def test_create(self, movie_service):
        data = {'id': 100, 'name': '123'}
        assert movie_service.create(data) is not None

    def test_update(self, movie_service):
        assert movie_service.update({"id": 1, "name": '123'}) is not None

    def test_delete(self, movie_service):
        assert movie_service.delete(1) is None

