import os
import json
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from schemas import DashboardUI

# 1. Load Environment
load_dotenv()

# 2. Initialize FastAPI
app = FastAPI(title="Generative UI Agent")

# 3. Enable CORS (Allow Frontend to talk to Backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev, allow all. In prod, strict this to your frontend URL.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Setup Groq Client
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

# 5. Define Request Model (What the frontend sends us)
class UserRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"status": "active", "service": "Generative UI Agent"}

@app.post("/generate", response_model=DashboardUI)
def generate_dashboard(request: UserRequest):
    print(f"📩 Received request: '{request.query}'")
    
    schema_definition = json.dumps(DashboardUI.model_json_schema(), indent=2)

    system_prompt = f"""
    You are a UI Generator. Output strictly valid JSON matching this schema:
    {schema_definition}
    
    Ensure 'components' list contains items with 'type' set to 'stat_card' or 'chart_line'.
    Do NOT include markdown formatting (like ```json). Just the raw JSON object.
    """

    try:
        completion = client.chat.completions.create(
            model=os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request.query}
            ],
            response_format={"type": "json_object"},
            temperature=0.1,
        )

        raw_content = completion.choices[0].message.content
        data = json.loads(raw_content)
        
        # Validate and return
        return DashboardUI(**data)

    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    # This allows us to run 'python main.py' to start the server
    uvicorn.run(app, host="0.0.0.0", port=8000)