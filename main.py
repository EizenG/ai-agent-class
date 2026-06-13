import warnings
warnings.filterwarnings("ignore")

from src.model.groqcloud import build_llm
from src.tools.inscription import inscription
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = build_llm()
llm =llm.bind_tools([inscription])

prompt = ChatPromptTemplate.from_template(f"You are a helpful agent that can answer questions about Thies Polytechnic School and register students. Give your response in french. user: {input}")
  
chain = prompt | llm

response = chain.invoke({"input": "inscrit moi à l'école polytechnique de thies. Nom: Naby DIA; Email: dnaby@gmail.com; Phone: 777777777; Address: Fahu, Thiès; City: Thiès"})
print(response.tool_calls)
