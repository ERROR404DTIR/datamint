import unittest
import app
SCHEMA={"fields":{"id":{"type":"id"},"age":{"type":"integer","min":18,"max":80},"tier":{"type":"choice","choices":["free","pro"]}}}
class Tests(unittest.TestCase):
 def test_seed_is_reproducible(self): self.assertEqual(app.generate(SCHEMA,12,9),app.generate(SCHEMA,12,9))
 def test_ids_are_sequential(self): self.assertEqual([r["id"] for r in app.generate(SCHEMA,3)],[1,2,3])
 def test_range(self): self.assertTrue(all(18<=r["age"]<=80 for r in app.generate(SCHEMA,100)))
 def test_empty_schema_rejected(self):
  with self.assertRaises(ValueError): app.generate({"fields":{}},1)
 def test_unknown_type_rejected(self):
  with self.assertRaises(ValueError): app.generate({"fields":{"x":{"type":"wat"}}},1)
if __name__=="__main__": unittest.main()
