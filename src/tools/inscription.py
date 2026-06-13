from langchain.tools import tool

@tool
def inscription(name: str, email: str, phone: str, address: str, city: str) -> str:
  """Inscription to the school"""
  return f"Inscription to the school for {name} with email {email} and phone {phone} and address {address} and city {city} and state {state} and zip {zip} and country {country}"

__all__ = ["inscription"]
