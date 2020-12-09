from src.models import Item, User

fake_items = [
    Item(name='Item 1'),
    Item(name='Item 2'),
    Item(name='Item 3'),
    Item(name='Item 4'),
    Item(name='Item 5'),
    Item(name='Item 6'),
]

fake_users = {
    '000de80d-e5f3-4484-873c-12cd25419b5a': User(
        id='000de80d-e5f3-4484-873c-12cd25419b5a',
        name='Jhon Wick',
        age=46,
        gender='Male',
    ),
    'ecedbc7f-399c-479f-9ff8-da625cad74ae': User(
        id='ecedbc7f-399c-479f-9ff8-da625cad74ae',
        name='Marcos V. Leal',
        age=23,
        gender='Male',
    ),
}
