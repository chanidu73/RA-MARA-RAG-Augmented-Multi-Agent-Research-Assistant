import uuid
from datetime import datetime

def build_acp_message(performative, sender, receiver, content):
    return {
        "performative": performative,        
        "sender": sender,
        "receiver": receiver,
        "content": content,
        "timestamp": datetime.utcnow().isoformat(),
        "conversation_id": str(uuid.uuid4())
    }
