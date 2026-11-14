#!/usr/bin/env python3
"""DataMint: reproducible synthetic data generator using only Python's standard library."""
import argparse,csv,io,json,random,string,sys
from datetime import date,timedelta
from pathlib import Path
def make_value(spec,rng,index):
 kind=spec.get("type","string")
 if kind=="id": return index+1
 if kind=="integer": return rng.randint(int(spec.get("min",0)),int(spec.get("max",100)))
 if kind=="number": return round(rng.uniform(float(spec.get("min",0)),float(spec.get("max",1))),int(spec.get("precision",2)))
 if kind=="boolean": return bool(rng.getrandbits(1))
 if kind=="choice":
  values=spec.get("choices")
  if not isinstance(values,list) or not values: raise ValueError("choice fields need a non-empty choices list")
  return rng.choice(values)
 if kind=="email": return f"user{index+1}@example.test"
 if kind=="date": return (date(2020,1,1)+timedelta(days=rng.randrange(2200))).isoformat()
 if kind=="string":
  prefix=str(spec.get("prefix","item-")); length=max(1,min(int(spec.get("length",8)),128))
  return prefix+"".join(rng.choice(string.ascii_lowercase+string.digits) for _ in range(length))
 raise ValueError("Unsupported field type: "+str(kind))
def generate(schema,count,seed=42):
 if not isinstance(schema,dict) or not isinstance(schema.get("fields"),dict) or not schema["fields"]: raise ValueError("Schema must contain a non-empty fields object")
 if not 0<=count<=100000: raise ValueError("count must be between 0 and 100000")
 rng=random.Random(seed)
 return [{name:make_value(spec,rng,i) for name,spec in schema["fields"].items()} for i in range(count)]
def main():
 p=argparse.ArgumentParser(description="Generate deterministic synthetic JSON or CSV data")
 p.add_argument("schema"); p.add_argument("-n","--count",type=int,default=20); p.add_argument("--seed",type=int,default=42); p.add_argument("-f","--format",choices=("json","csv"),default="json"); p.add_argument("-o","--output",default="-")
 a=p.parse_args()
 try:
  schema=json.loads(Path(a.schema).read_text(encoding="utf-8")); rows=generate(schema,a.count,a.seed)
  if a.format=="json": output=json.dumps(rows,ensure_ascii=False,indent=2)+"\\n"
  else:
   buffer=io.StringIO(); writer=csv.DictWriter(buffer,fieldnames=list(schema["fields"])); writer.writeheader(); writer.writerows(rows); output=buffer.getvalue()
  if a.output=="-": sys.stdout.write(output)
  else: Path(a.output).write_text(output,encoding="utf-8")
 except (OSError,ValueError,KeyError,json.JSONDecodeError) as exc: p.error(str(exc))
if __name__=="__main__": main()
