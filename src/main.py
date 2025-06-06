from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

import scraping_request

mcp = FastMCP("mantis")

@mcp.tool()
async def get_mantis_tasks(php_session_id: str, mantis_string_cookie: str, project_id: str) -> str:
    """
    Scrape tasks/activities from Mantis for a specific user and project.
    Ask the user for their PHP session ID, Mantis string cookie and project ID.
    Args:
        php_session_id (str): PHP session ID for Mantis.
        mantis_string_cookie (str): Mantis string cookie for authentication.
        project_id (str): The ID of the Mantis project to scrape tasks from.
    """
    bugnotes = scraping_request.scrape_project(php_session_id, mantis_string_cookie, project_id)
    
    if not bugnotes:
        return "No Mantis tasks found."
    
    return bugnotes

if __name__ == "__main__":
    mcp.run(transport="stdio")