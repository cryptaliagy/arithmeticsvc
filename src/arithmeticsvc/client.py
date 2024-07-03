import httpx

from arithmeticsvc.arithmetic import OutputBase


class ArithmeticClient:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.client = httpx.AsyncClient()

    def prepare_request(self, left: int, right: int) -> dict[str, int]:
        return {"left": left, "right": right}

    async def add(self, left: int, right: int) -> dict[str, str]:
        response = await self.client.post(
            f"http://{self.host}:{self.port}/add",
            json=self.prepare_request(left, right),
        )
        return response.json()

    async def subtract(self, left: int, right: int) -> dict[str, str]:
        response = await self.client.post(
            f"http://{self.host}:{self.port}/subtract",
            json=self.prepare_request(left, right),
        )
        return response.json()

    async def multiply(self, left: int, right: int) -> dict[str, str]:
        response = await self.client.post(
            f"http://{self.host}:{self.port}/multiply",
            json=self.prepare_request(left, right),
        )
        return response.json()

    async def integer_divide(self, left: int, right: int) -> dict[str, str]:
        response = await self.client.post(
            f"http://{self.host}:{self.port}/integer_divide",
            json=self.prepare_request(left, right),
        )
        return response.json()

    async def output(self, output_type: OutputBase) -> dict[str, str]:
        response = await self.client.get(
            f"http://{self.host}:{self.port}/output/{output_type}",
        )
        return response.json()

    async def close(self):
        await self.client.aclose()
