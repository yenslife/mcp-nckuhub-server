from httpx import AsyncClient
import json

URL = "https://nckuhub.com/"


# helper functions
async def fetch(url: str) -> str:
    async with AsyncClient() as client:
        response = await client.get(url)
        return response.text


async def fetch_all_course_impl() -> list[dict]:
    data = await fetch(URL + "course")
    obj = json.loads(data)
    return obj["courses"]


async def fetch_course_impl(course_id: str) -> dict:
    data = await fetch(URL + "course" + "/" + course_id)
    return json.loads(data)


async def fetch_all_dpmt_impl() -> list[dict]:
    data = await fetch(URL + "course" + "/allDpmt")
    return json.loads(data)


async def fetch_all_course_prev_impl() -> list[dict]:
    data = await fetch(URL + "course" + "/allCoursePrev")
    return json.loads(data)
