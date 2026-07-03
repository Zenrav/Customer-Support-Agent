from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class Ticket(BaseModel):
    title: str
    customer_query: str
    system_diagnostic_summary: str
    metadata: dict = {}


@app.post("/api/v1/tickets")
def raise_ticket(ticket: Ticket):
    generated_id = f"TCK-{uuid.uuid4().hex[:6].upper()}"

    return {
        "status": "success",
        "ticket_id" : generated_id,
        "message" : "Customer support incident successfully queued for Tier-3 engineering triage.",
        "record_received": {
            "title": ticket.title,
            "product" : ticket.metadata.get("detected_product", "Unknown")
        }
    }