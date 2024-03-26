from deep_translator import GoogleTranslator

from hikkatl.types import Message
from .. import loader, utils


@loader.tds
class BetterTranslator(loader.Module):
    """Модуль для перевода текста на любой язык"""

    strings = {
        'name': 'BetterTranslator'
    }

    @loader.command(ru_doc='[текст] [язык] - перевести текст на любой язык')
    async def btr(self, message: Message):
        await utils.answer(message, '⏳ Идет перевод текста...')

        args = utils.get_args_raw(message).split()

        tr = GoogleTranslator(target=args[-1])
        result = tr.translate(text=' '.join(args[:-1]))

        await utils.answer(message, result)
