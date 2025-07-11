import aiohttp
from aiohttp import web
from acp.message import build_acp_message

routes = web.RouteTableDef()

@routes.post("/query")
async def query_handler(request):
    data = await request.json()
    user_question = data.get("question")

    msg = build_acp_message("request", "QueryAgent", "SourceAgent", user_question)
    
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8001/source", json=msg) as resp:
            reply = await resp.json()
            return web.json_response(reply)

app = web.Application()
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, port=8000)
