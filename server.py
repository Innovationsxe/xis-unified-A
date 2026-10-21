#!/usr/bin/env python3
"""XIS Unified MVP: local demo server using Python standard library only."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse
import json, os, uuid, datetime
ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'
DATA.mkdir(exist_ok=True)
FILES = {'tenders': DATA/'tenders.json', 'profiles': DATA/'profiles.json', 'bids': DATA/'bids.json'}
DEFAULTS = {
'tenders': [
 {'id':'TND-001','title':'Supply of Computer and Office Equipment','agency':'Demo Municipal Office','category':'ICT','description':'Supply laptops, monitors, printers and related support. Vendors must provide delivery timelines and warranty details.','closing_date':'2027-02-28','location':'KwaZulu-Natal','status':'Open'},
 {'id':'TND-002','title':'Facilities Maintenance Services','agency':'Demo Public Works Unit','category':'Facilities','description':'Routine building maintenance, minor repairs and grounds services. Include relevant experience and response times.','closing_date':'2027-03-15','location':'National','status':'Open'},
 {'id':'TND-003','title':'Software Development and Support','agency':'Demo Digital Services Office','category':'Technology','description':'Web application development, software support, training and maintenance services.','closing_date':'2027-03-05','location':'Remote / South Africa','status':'Open'}], 'profiles': [], 'bids': []}
def load(name):
 p=FILES[name]
 if not p.exists(): p.write_text(json.dumps(DEFAULTS[name], indent=2))
 try: return json.loads(p.read_text())
 except Exception: return DEFAULTS[name]
def save(name, data): FILES[name].write_text(json.dumps(data, indent=2))
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*a,**kw): super().__init__(*a,directory=str(ROOT/'static'),**kw)
 def send_json(self, obj, status=200):
  raw=json.dumps(obj).encode(); self.send_response(status); self.send_header('Content-Type','application/json; charset=utf-8'); self.send_header('Content-Length',str(len(raw))); self.send_header('Access-Control-Allow-Origin','*'); self.end_headers(); self.wfile.write(raw)
 def do_GET(self):
  path=urlparse(self.path).path
  if path=='/api/tenders': self.send_json(load('tenders')); return
  if path=='/api/profiles': self.send_json(load('profiles')); return
  if path=='/api/bids': self.send_json(load('bids')); return
  if path=='/api/health': self.send_json({'ok':True,'app':'XIS Unified MVP','version':'0.2.0'}); return
  if path=='/': self.path='/index.html'
  return super().do_GET()
 def do_POST(self):
  path=urlparse(self.path).path
  try:
   n=int(self.headers.get('Content-Length','0')); body=json.loads(self.rfile.read(n) or b'{}')
  except Exception: self.send_json({'error':'Invalid JSON body'},400); return
  if path=='/api/tenders':
   required=['title','agency','category','description','closing_date']
   if any(not str(body.get(k,'')).strip() for k in required): self.send_json({'error':'Please complete title, agency, category, description and closing date.'},400); return
   data=load('tenders'); item={'id':'TND-'+uuid.uuid4().hex[:6].upper(), **{k:str(body.get(k,'')).strip() for k in required},'location':str(body.get('location','South Africa')),'status':'Open'}; data.insert(0,item); save('tenders',data); self.send_json(item,201); return
  if path=='/api/profiles':
   required=['business_name','contact_name','email','categories','description']
   if any(not str(body.get(k,'')).strip() for k in required): self.send_json({'error':'Please complete all required profile fields.'},400); return
   data=load('profiles'); item={'id':'BIZ-'+uuid.uuid4().hex[:6].upper(),**{k:str(body.get(k,'')).strip() for k in required},'created_at':datetime.date.today().isoformat()}; data.append(item); save('profiles',data); self.send_json(item,201); return
  if path=='/api/bids':
   required=['tender_id','business_name','contact_email','proposal','price']
   if any(not str(body.get(k,'')).strip() for k in required): self.send_json({'error':'Please complete all bid fields.'},400); return
   tenders=load('tenders')
   if not any(t['id']==body['tender_id'] and t['status']=='Open' for t in tenders): self.send_json({'error':'Tender not found or closed.'},404); return
   data=load('bids'); item={'id':'BID-'+uuid.uuid4().hex[:6].upper(),**{k:str(body.get(k,'')).strip() for k in required},'submitted_at':datetime.datetime.now().isoformat(timespec='minutes'),'status':'Received'}; data.append(item); save('bids',data); self.send_json(item,201); return
  self.send_json({'error':'Unknown API endpoint'},404)
 def log_message(self, fmt, *args): print('%s - %s' % (self.address_string(), fmt%args))
if __name__=='__main__':
 port=int(os.environ.get('PORT','8000')); print(f'XIS Unified MVP running at http://127.0.0.1:{port}'); ThreadingHTTPServer(('0.0.0.0',port),Handler).serve_forever()
