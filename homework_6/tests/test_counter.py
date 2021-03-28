from task02.counter import instances_counter


@instances_counter
class User:
    pass


def test_user_class_create_instances_and_reset_instance():
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3
    assert user.reset_instances_counter() == 3


def test_reset_instances_counter():
    user, _ = User(), User()
    assert user.reset_instances_counter() == 2
    assert user.get_created_instances() == 0
