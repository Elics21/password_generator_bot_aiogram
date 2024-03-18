from aiogram.types import Message
from aiogram.filters import BaseFilter
from filters import ADMINS


class IsAdmin(BaseFilter):

    async def check(self, message: Message):
        return message.from_user.id in ADMINS
