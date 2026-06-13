from src.model.groqcloud import build_llm
from src.prompt.langfuse_client import get_langchain_prompt
from src.memory.chat_history import get_session_history

class EPTAgent:
    def __init__(self, session_id: str, user_name: str):
      self.session_id = session_id
      self.user_name = user_name
      
    def stream(self, message: str):
      ...
      
    async def astream(self, message: str):
      ...
      
    async def ainvoke(self, message: str):
      ...
    
    def invoke(self, message: str):
      ...
    