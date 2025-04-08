from mcp.server.fastmcp import FastMCP

from mcp_nckuhub_server.tools import (
    fetch_all_course_impl,
    fetch_course_impl,
    fetch_all_dpmt_impl,
    fetch_all_course_prev_impl,
    search_department_id_by_name_impl,
    search_courses_by_department_id_impl,
)
from mcp_nckuhub_server.prompts import parse_semester_from_query_impl

# Initialize the server
mcp = FastMCP("mcp-nckuhub-server", log_level="ERROR")

# Tools


@mcp.tool()
async def get_all_course() -> list[dict]:
    """取得所有課程資訊"""
    return await fetch_all_course_impl()


@mcp.tool()
async def get_course(course_id: int) -> dict:
    """取得指定課程的評價，包含甜度 (給分)、涼度 (課堂 loading)"""
    return await fetch_course_impl(course_id)


@mcp.tool()
async def get_all_dpmt() -> list[dict]:
    """取得所有系所資訊"""
    return await fetch_all_dpmt_impl()


@mcp.tool()
async def get_all_course_prev() -> list[dict]:
    """取得所有課程現況資訊"""
    return await fetch_all_course_prev_impl()


@mcp.tool()
async def search_department_id_by_name(DepName: str) -> str:
    """用系所名稱搜尋系所代碼"""
    return await search_department_id_by_name_impl(DepName)


@mcp.tool()
async def search_courses_by_department_id(DepPrefix: str = "") -> list[dict]:
    """用系所代碼搜尋課程"""
    return await search_courses_by_department_id_impl(DepPrefix)


# Prompts
@mcp.prompt()
async def parse_semester_from_query(query: str) -> str:
    """將使用者的自然語言查詢轉換為學期格式"""
    return parse_semester_from_query_impl(query)


def main():
    print("正在啟動 NCKUHub MCP 服務器...")
    mcp.run()


if __name__ == "__main__":
    main()
