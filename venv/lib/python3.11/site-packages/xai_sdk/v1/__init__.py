"""V1 xAI SDK."""

import asyncio

from .. import _v1_sdk_imported

_v1_sdk_imported()


from .client import Client


def does_it_work():
    """Prints "Yes, it does." if API access works.

    This function can be used to quickly check if API access works by running the following command:

    ```shell
    python -c "import xai_sdk; xai_sdk.does_it_work()"
    ```
    """

    async def _run():
        prompt = "Yes, it does. Yes, it does. Yes, it does. Yes, it does. Yes, it does."
        print("Does it work?", end="")
        async for token in Client().sampler.sample(prompt=prompt, stop_strings=["."]):
            print(token.token_str, end="")
        print("")

    asyncio.run(_run())
