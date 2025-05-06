import asyncio
import json
import random
import websockets

async def simulate_kpi(websocket, path):
    while True:
        data = {
            "active_sessions": random.randint(50, 100),
            "pending_sessions": random.randint(5, 20),
            "rejected_requests": random.randint(0, 5)
        }
        await websocket.send(json.dumps(data))
        await asyncio.sleep(2)  # Simulate data every 2 seconds

start_server = websockets.serve(simulate_kpi, "localhost", 8765)

print("WebSocket server started at ws://localhost:8765")
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

