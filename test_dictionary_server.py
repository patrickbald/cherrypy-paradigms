#!/escnfs/home/csesoft/2017-fall/anaconda3/bin/python3

import unittest
import requests
import json

class TestCherrypyPrimer(unittest.TestCase):

        
       
        SITE_URL = 'http://student10.cse.nd.edu:51075' #Replace this your port numberand machine. if testing on localhost, replace machine name and number with localhost
        DICT_URL = SITE_URL + '/dictionary/'

        def reset_data(self):
                r = requests.delete(self.DICT_URL) # note, that most tests depend on DELETE_INDEX working correctly

        def is_json(self, resp):
                try:
                        json.loads(resp)
                        return True
                except ValueError:
                        return False

        def test_dict_get_key(self):
                self.reset_data()
                key = 'HarryPotter'
                r = requests.get(self.DICT_URL + key)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'error')

        def test_dict_put_key(self):
                self.reset_data()
                key = 'HarryPotter'

                m = {}
                m['value'] = 'Gryffindor'
                r = requests.put(self.DICT_URL + key, data = json.dumps(m))
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DICT_URL + key)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['value'], m['value'])

        def test_dict_delete_key(self):
                self.reset_data()
                key = 'HarryPotter'

                m = {}
                m['value'] = 'Gryffindor'
                r = requests.put(self.DICT_URL + key, data = json.dumps(m))
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.delete(self.DICT_URL + key)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DICT_URL + key)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'error')

        def test_dict_index_get(self):
                self.reset_data()

                key = 'HarryPotter'
                m = {}
                m['value'] = 'Gryffindor'
                r = requests.put(self.DICT_URL + key, data = json.dumps(m))
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DICT_URL)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                entries = resp['entries']
                mkv = entries[0]
                self.assertEqual(mkv['key'], key)
                self.assertEqual(mkv['value'], m['value'])

        def test_dict_index_post(self):
                self.reset_data()

                m = {}
                m['key'] = 'HarryPotter'
                m['value'] = 'Gryffindor'

                r = requests.post(self.DICT_URL, data = json.dumps(m))
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                r = requests.get(self.DICT_URL)
                self.assertTrue(self.is_json(r.content.decode()))
                resp = json.loads(r.content.decode())
                self.assertEqual(resp['result'], 'success')

                entries = resp['entries']
                mkv = entries[0]
                self.assertEqual(mkv['key'], m['key'])
                self.assertEqual(mkv['value'], m['value'])

if __name__ == "__main__":
        unittest.main()
