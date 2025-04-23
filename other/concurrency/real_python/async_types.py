import asyncio


async def _f(x):
    return x


async def coroutine(x):
    y = await _f(x)  # OK - `await` and `return` allowed in coroutines
    return y


async def async_generator(x):
    yield x  # OK - this is an async generator
    # yield from gen(x)  # No - SyntaxError


@asyncio.coroutine
def py34_coroutine(x):
    """Generator-based coroutine, older syntax"""
    yield from _f(x)

