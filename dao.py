import asyncio
from sqlalchemy import insert, select, update, delete
from models import User, Order
from database import async_session_maker

async def create_user(name: str,
        login: str,
        password: str,
        age: int,
        nickname: str = None,
        notes: str = None,) -> tuple:
    async with async_session_maker() as session:
        query = insert(User).values(
            name=name,
            login=login,
            password=password,
            age=age,
            nickname=nickname,
            notes=notes,
        ).returning(User.id, User.created_at, User.login)
        data = await session.execute(query)
        await session.commit()
        return tuple(data)[0]


async def fetch_users(skip: int = 0, limit: int = 10) -> list[User]:
    async with async_session_maker() as session:
        query = select(User).offset(skip).limit(limit)
        result = await session.execute(query)
        return result.scalars().all()

async def get_user_by_id(user_id: int) -> User | None:
    async with async_session_maker() as session:
        query = select(User).filter_by(id=user_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()

async def update_user(user_id: int, values: dict):
    if not values:
        return
    async with async_session_maker() as session:
        query = update(User).where(User.id == user_id).values(**values)
        result = await session.execute(query)
        await session.commit()
        return result.scalar_one_or_none

async def delete_user(user_id: int):
    async with async_session_maker() as session:
        query = delete(User).where(User.id == user_id)
        await session.execute(query)
        await session.commit()


async def main():
    await asyncio.gather(create_user(
        name='Dmutro2',
        login='dima20@gmail',
        password='IhateBroccoli123',
        age=12,
        nickname='dimasik',
        notes='If only I could write here whole Shrek 1 plot'
    ),create_user(
        name='Evgeniy',
        login='corpAccount@gmail',
        password='h8hLF$k99',
        age=31,
    ),create_user(
        name='Katya',
        login='qwerty',
        password='1234',
        age=19,
        notes='._.'
    ))
#asyncio.run(main())

async def create_order(
        quantity: int,
        price: float,
        customer: int,
        ) -> tuple:
    async with async_session_maker() as session:
        query = insert(Order).values(
            quantity= quantity,
            price= price,
            customer= customer,
        ).returning(Order.id, Order.created_at)
        data = await session.execute(query)
        await session.commit()
        return tuple(data)[0]

async def fetch_orders(skip: int = 0, limit: int = 10) -> list[Order]:
    async with async_session_maker() as session:
        query = select(Order).offset(skip).limit(limit)
        result = await session.execute(query)
        return result.scalars().all()

async def get_order_by_id(order_id: int) -> Order | None:
    async with async_session_maker() as session:
        query = select(Order).filter_by(id=order_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()

async def update_order(order_id: int, values: dict):
    if not values:
        return
    async with async_session_maker() as session:
        query = update(Order).where(Order.id == order_id).values(**values)
        result = await session.execute(query)
        await session.commit()
        return result.scalar_one_or_none

async def delete_order(order_id: int):
    async with async_session_maker() as session:
        query = delete(Order).where(Order.id == order_id)
        await session.execute(query)
        await session.commit()

async def main_order():
    await asyncio.gather(create_order(
            quantity= 2,
            price= 1.6,
            customer= 1,),
                        create_order(
            quantity=10,
            price=99.99,
            customer=3, ),
    delete_order(1))

asyncio.run(main_order())