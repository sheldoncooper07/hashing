# -*- coding: utf-8 -*-
import unittest
from my_hash import CuckooHash


class TestCuckooHashConstruction(unittest.TestCase):
	def test_construction_valid_arg(self):
		self.assertEqual(3, CuckooHash(3.0).size)
		self.assertEqual(200, CuckooHash(200).size)
		self.assertEqual(0, CuckooHash(0).size)
		self.assertEqual(1000, CuckooHash(1000).size)

	def test_construction_bad_type(self):
		with self.assertRaises(TypeError):
			CuckooHash('string')

	def test_construction_bad_value(self):
		with self.assertRaises(ValueError): 
			CuckooHash(-1)
		with self.assertRaises(ValueError): 
			CuckooHash(-1.0)
		with self.assertRaises(ValueError):
			CuckooHash(2.2)


class TestCuckooHashSetGet(unittest.TestCase):
	def setUp(self):
		self.small_hash_map = CuckooHash(20)
		self.big_hash_map = CuckooHash(1000)
		self.alice_text = open('alice.txt', 'r').read()

	def test_set_get_full(self):
		bulk_set_results = self._bulk_set(self.small_hash_map, 20)
		self.assertTrue(all(bulk_set_results))
		bulk_get_results = self._bulk_get(self.small_hash_map, 20)
		self.assertEqual(range(20), bulk_get_results)

	def test_good_keys(self):
		self.assertTrue(self.big_hash_map.set("", "somevalue"))
		self.assertTrue(self.big_hash_map.set("somekey", (1, 2, 3)))
		self.assertTrue(self.big_hash_map.set("ʕ•ᴥ•ʔ", "(•ω•)"))
		self.assertTrue(self.big_hash_map.set(self.alice_text, 'alice'))

		self.assertEqual(self.big_hash_map.get(""), "somevalue")
		self.assertEqual(self.big_hash_map.get("somekey"), (1, 2, 3))
		self.assertEqual(self.big_hash_map.get("ʕ•ᴥ•ʔ"), "(•ω•)")
		self.assertEqual(self.big_hash_map.get(self.alice_text), 'alice')

	def test_set_by_assignment(self):
		value = [1, 2, 3]
		self.big_hash_map.set("list", value)
		value.append(4)
		self.assertEqual(value, self.big_hash_map.get("list"))

	def test_bad_keys(self):
		with self.assertRaises(TypeError):
			self.small_hash_map.set([1], 0)
			self.small_hash_map.set(10, 20)

	def test_failed_set(self):
		self._bulk_set(self.small_hash_map, 20)
		self.assertFalse(self.small_hash_map.set('20th item', 5))

	def test_set_overwrite(self):
		self.small_hash_map.set('somekey', 0)
		self.assertTrue(self.small_hash_map.set('somekey', 1))
		self.assertEqual(1, self.small_hash_map.get('somekey'))

	def _bulk_set(self, hash_map, nitems):
		return [hash_map.set("key" + str(i), i) for i in range(nitems)]

	def _bulk_get(self, hash_map, nitems):
		return [hash_map.get("key" + str(i)) for i in range(nitems)]


class TestCuckooHashDelete(unittest.TestCase):
	def setUp(self):
		self.hash_map = CuckooHash(50)

	def test_delete_existing(self):
		self.hash_map.set("somekey", 20)
		self.assertEqual(self.hash_map.delete("somekey"), 20)
		self.assertIsNone(self.hash_map.get("somekey"))

	def test_delete_nonexisting(self):
		self.assertIsNone(self.hash_map.delete("somekey"))


class TestCuckooHashLoad(unittest.TestCase):
	def setUp(self):
		self.hash_map = CuckooHash(5)

	def test_load(self):
		self.assertEqual(self.hash_map.load(), 0)
		self.hash_map.set('key', 0)
		self.assertAlmostEqual(self.hash_map.load(), 0.2)
		self.hash_map.set('otherkey', 0)
		self.assertAlmostEqual(self.hash_map.load(), 0.4)
		self.hash_map.delete('key')
		self.assertAlmostEqual(self.hash_map.load(), 0.2)
		self.hash_map.delete('otherkey')
		self.assertEqual(self.hash_map.load(), 0)

if __name__ == '__main__':
	unittest.main()
