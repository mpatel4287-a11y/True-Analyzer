"""
Async web search using DuckDuckGo — no API key required.
Runs DDG (sync) in a thread pool so FastAPI stays non-blocking.
"""
from __future__ import annotations

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Any

_executor = ThreadPoolExecutor(max_workers=6)


def _ddg_text(query: str, max_results: int) -> list[dict[str, str]]:
    """Blocking DDG search with retry logic."""
    from ddgs import DDGS  # local import keeps startup fast

    for attempt in range(3):
        try:
            with DDGS() as ddgs:
                results = list(ddgs.text(query, max_results=max_results))
                return results
        except Exception:
            time.sleep(0.8 * (attempt + 1))
    return []


async def search(query: str, max_results: int = 5) -> list[dict[str, str]]:
    """Async wrapper around DDG text search."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(_executor, _ddg_text, query, max_results)


def _snippet(r: dict[str, str], limit: int = 400) -> str:
    title = r.get("title", "")
    body = r.get("body", "")
    href = r.get("href", "#")
    return f"[{title}]({href}): {body}"[:limit]


async def gather_for_analysis(field: str, idea: str) -> dict[str, Any]:
    """Run targeted searches in parallel and return formatted snippets."""
    kw = " ".join(idea.split()[:10])

    queries = [
        f"{field} {kw} technical hardware software component list price USD 2024 2025",
        f"{field} {kw} professional software libraries frameworks tools 2024 2025",
        f"{field} {kw} market size growth CAGR statistics 2024 2025",
        f"{field} {kw} professional market competitors startups products 2024 2025",
        f"{field} {kw} detailed project budget cost estimation breakdown USD 2024 2025",
        f"{field} {kw} user pain points risks challenges limitations reddit",
        f"{field} {kw} latest news trends breakthroughs 2024 2025",
    ]

    results = await asyncio.gather(*[search(q, 10) for q in queries])

    return {
        "components":      "\n".join(_snippet(r) for r in results[0]),
        "tech_stack":      "\n".join(_snippet(r) for r in results[1]),
        "market":          "\n".join(_snippet(r) for r in results[2]),
        "existing":        "\n".join(_snippet(r) for r in results[3]),
        "budget":          "\n".join(_snippet(r) for r in results[4]),
        "risks":           "\n".join(_snippet(r) for r in results[5]),
        "news":            "\n".join(_snippet(r) for r in results[6]),
    }


async def gather_for_generation(field: str, context: str) -> dict[str, Any]:
    """Run searches for idea generation including social trends."""
    queries = [
        f"trending innovative project ideas {field} for students github reddit 2024 2025",
        f"unsolved problems in {field} industry 2024 2025 pain points",
        f"latest breakthroughs {field} tech news 2024 2025",
        f"competition winning student projects {field} winners 2023 2024 2025",
    ]

    results = await asyncio.gather(*[search(q, 10) for q in queries])

    return {
        "ideas":       "\n".join(_snippet(r) for r in results[0]),
        "problems":    "\n".join(_snippet(r) for r in results[1]),
        "trends":      "\n".join(_snippet(r) for r in results[2]),
        "competition": "\n".join(_snippet(r) for r in results[3]),
    }
