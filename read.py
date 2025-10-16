import re

ranks = {'PV2': '이병', 'PFC': '일병', 'CPL': '상병', 'SGT': '병장'}
senior = {'송재현', '홍준형', '허재강', '고종우'}

def extract(text):
  pattern = r"^(\w+).*?\(([^)]+)\)"
  match = re.search(pattern, text, re.IGNORECASE)
  
  name = match.group(2).strip()
  rank = match.group(1)
  if name in senior:
    return '선임병장 ', name
  
  if match:
    return ranks[rank], name