# OpenVidu Connect
The project aims to connect to the OpenVidu Server.
It tries to wrap all the headers and APIs into attributes and methods of a class.
OpenVidu Connect provides support for Sync and Async API calls.
**(Enabled with context manager for both sync and async runs.)**

## What do we have in store?
- Future annotations are used to get the maximum output for support in IDEs
- Built on top of httpx (Get httpx: pip install httpx)

## Code Examples
- Sync Class (OpenViduClient) Example
```python
from openviduconnect import OpenViduClient

ov = OpenViduClient("<HOST>", "<SECRET>")
response = ov.get_sessions()
print(response)

######
# OR #
######

with OpenViduClient("<HOST>", "<SECRET>") as ov:
    response = ov.get_sessions()
print(response)
```

- Async Class (AsyncOpenViduClient) Example
```python
from openviduconnect import AsyncOpenViduClient

aov = AsyncOpenViduClient("<HOST>", "<SECRET>")
"""Async Stuff"""
response = await aov.get_sessions()
print(response)

######
# OR #
######

async with AsyncOpenViduClient("<HOST>", "<SECRET>") as aov:
    response = await aov.get_sessions()
print(response)
```

- We have all forms of specific errors respective to the documentation of the REST APIs
```python
from openviduconnect.exceptions import SessionBodyParameterError
"""SessionBodyParameterError is just an example there are many more"""

print(SessionBodyParameterError.status)  # Provides HTTP Response Status Code
```

## Support
- Runs with Python 3.7 and beyond
- At this point it only supports OpenVidu 2.17.0
- Will try to maintain versions of openviduconnect for different OepnVidu versions

## Known issues?
- Documentation
- Others. *You tell me*
