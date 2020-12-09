from fastapi import FastAPI, HTTPException

from src.database import fake_items, fake_users
from src.models import PaginatedItems, User
from src.settings import SERVER_DEBUG

app = FastAPI(debug=SERVER_DEBUG)


@app.get('/users/me/', response_model=User)
async def read_user_me():
    me = fake_users.get('ecedbc7f-399c-479f-9ff8-da625cad74ae')
    if me is None:
        raise HTTPException(
            status_code=403, detail='User forbidden for this feature.'
        )

    return me


@app.get('/users/{user_id}/', response_model=User)
async def read_user(user_id: str):
    user = fake_users.get(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail='User not found.')

    return user


@app.get('/items/', response_model=PaginatedItems)
async def read_items(offset: int = 0, limit: int = 10):
    last_item = offset + limit
    items = fake_items[offset:last_item]
    items_total = len(fake_items)
    items_has_next = last_item < items_total

    return {
        'has_next': items_has_next,
        'total': items_total,
        'items': items,
    }
