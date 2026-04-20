import asyncio
import httpx
import json

async def test_api():
    async with httpx.AsyncClient(timeout=30.0) as client:
        # 1. Health check
        try:
            res = await client.get("http://localhost:8000/api/health")
            print(f"Health Check: {res.status_code} - {res.json()}")
        except Exception as e:
            print(f"Health Check Failed: {e}")

        # 2. Test Fields
        try:
            res = await client.get("http://localhost:8000/api/fields")
            print(f"Fields Count: {len(res.json().get('fields', []))}")
        except Exception as e:
            print(f"Fields Check Failed: {e}")

        # Note: Analyze and Generate require Anthropic API Key.
        # This script confirms the endpoints are wired up correctly.
        print("\nNote: Analyze and Generate endpoints require a valid ANTHROPIC_API_KEY in .env")

if __name__ == "__main__":
    asyncio.run(test_api())
