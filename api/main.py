from langcorn import create_service

app = create_service(
    "api.chatbot_chain:chat",
)