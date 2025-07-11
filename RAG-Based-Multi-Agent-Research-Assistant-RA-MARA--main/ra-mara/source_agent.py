import asyncio
from aiohttp import web
from rag.langchain_pipeline_by_using_llama import load_rag_pipeline

rag = load_rag_pipeline()
routes = web.RouteTableDef()

@routes.post("/source")
async def handle_source(request):
    data = await request.json()
    content = data.get("content")
    answer = rag.run(content)
    
    return web.json_response({
        "performative": "inform",
        "sender": "SourceAgent",
        "receiver": data["sender"],
        "content": answer,
        "conversation_id": data["conversation_id"]
    })

app = web.Application()
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app, port=8001)
