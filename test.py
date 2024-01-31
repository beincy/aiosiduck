import asyncio
from aiosiduck import SiduckClient


async def main():
    client = SiduckClient("127.0.0.1", "8083", "cert.pem")
    res = await client.request(b"i am a cat")
    print(res)
    res = await client.request(b"i am a dog")
    print(res)
    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
