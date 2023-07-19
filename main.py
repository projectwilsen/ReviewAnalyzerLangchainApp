from langcorn import create_service

app = create_service(
    "chatbot_chain:chat",
)