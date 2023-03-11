from unittest.mock import MagicMock

import pytest

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from service.director import DirectorService
from setup_db import db


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)
    dir1 = Director(id=1, name='Иван Иванович')
    dir2 = Director(id=2, name='Петр Петрович')
    dir3 = Director(id=3, name='Тест Тестович')
    director_dao.get_one = MagicMock(return_value=dir1)
    director_dao.get_all = MagicMock(return_value=[dir1, dir2, dir3])
    director_dao.delete = MagicMock(return_value=dir3)
    director_dao.create = MagicMock()
    director_dao.update = MagicMock()
    return director_dao



class TestDirectorService():
    @pytest.fixture()
    def director_service(self, director_dao):
        director_service = DirectorService(dao=director_dao)
        return director_service
    def test_get_one(self, director_service):
        assert director_service.get_one(1).name == 'Иван Иванович'
        assert director_service.get_one(1) is not None
        assert director_service.get_one(1).id is not None

    def test_get_all(self, director_service):
        assert director_service.get_all() is not None
        assert director_service.get_all()[0] is not None
        assert director_service.get_all()[0].id is not None

    def test_create(self, director_service):
        data = {'id': 100, 'name': '123'}
        assert director_service.create(data) is not None

    def test_update(self, director_service):
        assert director_service.update({"id": 1, "name": '123'}) is not None

    def test_delete(self, director_service):
        assert director_service.delete(1) is None
