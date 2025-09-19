# from daos.user_dao import UserDAO
from daos.user_dao_mongo import UserDAOMongo
from models.user import User

# dao = UserDAO()
dao = UserDAOMongo()

def test_user_select():
    # Assurer que la base de données est propre avant le test
    dao.delete_all()
    user = User(None, 'Margaret Hamilton', 'hamilton@example.com')
    dao.insert(user)
    user = User(None, 'Margaret Hamilton', 'hamilton@example.com')
    dao.insert(user)
    user = User(None, 'Margaret Hamilton', 'hamilton@example.com')
    dao.insert(user)

    user_list = dao.select_all()
    assert len(user_list) >= 3

    # Assurer que la base de données est propre apres le test
    dao.delete_all()

def test_user_insert():
    user = User(None, 'Margaret Hamilton', 'hamilton@example.com')
    dao.insert(user)
    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert user.email in emails

def test_user_update():
    user = User(None, 'Charles Babbage', 'babage@example.com')
    assigned_id = dao.insert(user)

    corrected_email = 'babbage@example.com'
    corrected_name = 'Charles Babbage1'
    user.id = assigned_id
    user.email = corrected_email
    user.name = corrected_name

    dao.update(user)

    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert corrected_email in emails
    names = [u.name for u in user_list]
    assert corrected_name in names

def test_user_delete():
    user = User(None, 'Douglas Engelbart', 'engelbart@example.com')
    assigned_id = dao.insert(user)
    dao.delete(assigned_id)

    user_list = dao.select_all()
    emails = [u.email for u in user_list]
    assert user.email not in emails

def test_user_delete_all():
    user = User(None, 'Test User', 'test@example.com')
    dao.insert(user)
    dao.delete_all()
    user_list = dao.select_all()
    assert len(user_list) == 0