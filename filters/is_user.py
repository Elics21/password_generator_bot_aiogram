from aiogram.types import Message
from aiogram.filters import  BaseFilter
from filters import ADMINS


class IsUser(BaseFilter):
    async def check(self, message: Message):
        return message.from_user.id not in ADMINS
