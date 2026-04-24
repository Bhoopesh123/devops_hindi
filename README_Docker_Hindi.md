# OpenLit_LLM

docker build -t gemini-chat-app:latest .

docker login
docker tag gemini-assistant-2026 bhoopeshsharma/gemini-assistant-2026:latest
docker push bhoopeshsharma/gemini-assistant-2026:latest

curl -X POST http://localhost:8080/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello from k3d"}'
