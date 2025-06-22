"""xAI Software Development Kit (SDK).

This SDK lets you interact with the xAI API. In order to access the API, you need to generate an
API key in our IDE, which is available under ide.x.ai. After signing in, click on your username in
the top right hand corner and select "API Keys". Generate a new API key and make sure to assign the
correct ACLs. In order to sample from the model, you need the `chat:write` or `sampler:write` ACLs.

You can either import the v1 SDK or the v2 SDK. You cannot import both in the same process. To
import the v1 SDK, write:

```python
import xai_sdk
client = xai_sdk.Client()
```

To import the v2 SDK, write:

```python
import xai_sdi.v2
client = xai_sdk.v2.ClientV2()
```

If you try to import both, an error is raised.
"""

import deprecated

# Note: In the past, we used to simply import the v1 `Client` class here. Because we now need to
# ensure the v1 SDK isn't loaded when the v2 SDK is loaded, we lazily import the class.
V1_SDK_IMPORTED = False
V2_SDK_IMPORTED = False

# The v1 SDK cannot be imported a process when the v2 SDK has previously been imported. Doing so
# will trigger a cryptic error that is difficult for users to understand. We raise a more readable
# error here instead.


def _v1_sdk_imported():
    """Marks the v1 SDK is having been imported. Checks the v2 SDK hasn't been imported before."""
    global V1_SDK_IMPORTED
    if V2_SDK_IMPORTED:
        raise ImportError(
            "The xai_sdk.v1 SDK cannot be imported if the the xai_sdk.v2 SDK has "
            "previously been imported. Note that for backwards compatibility reasons, "
            "the default SDK is the v1 SDK. If you want to use the v1 SDK, remove any "
            "imports of the v2 SDK. If you want to use the v2 SDK, remove any references "
            "to the v1 SDK including importing the default client xai_sdk.Client and the "
            "default check xai_sdk.does_it_work()."
        )
    V1_SDK_IMPORTED = True


def _v2_sdk_imported():
    """Marks the v2 SDK is having been imported. Checks the v1 SDK hasn't been imported before."""
    global V2_SDK_IMPORTED
    if V1_SDK_IMPORTED:
        raise ImportError(
            "The xai_sdk.v2 SDK cannot be imported if the the xai_sdk.v1 SDK has "
            "previously been imported. Note that for backwards compatibility reasons, "
            "the default SDK is the v1 SDK. If you want to use the v1 SDK, remove any "
            "imports of the v2 SDK. If you want to use the v2 SDK, remove any references "
            "to the v1 SDK including importing the default client xai_sdk.Client and the "
            "default check xai_sdk.does_it_work()."
        )
    V2_SDK_IMPORTED = True


@deprecated.deprecated(
    reason="The default SDK client has been deprecated. Please explicitly "
    "import the v1 SDK instead: from xai_sdk.v1 import Client"
)
def Client(*args, **kwargs):
    """Lazily loads the v1 SDK client for backwards compatibility.

    Args:
        *args: Args passed to the v1 client.
        **kwargs: Args passed to the v2 client.

    Returns:
        The v1 SDK client.
    """
    from .v1 import Client

    return Client(*args, **kwargs)


@deprecated.deprecated(
    reason="The default SDK client has been deprecated. Please explicitly "
    "import the v1 SDK instead: from xai_sdk.v1 import does_it_work"
)
def does_it_work():
    """Lazily loads the v1 SDK check."""
    from .v1 import does_it_work

    does_it_work()
