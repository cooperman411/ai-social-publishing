import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POST = ROOT / 'skills/social-publishing/examples/fictional-post.json'

class SocialFixtureTests(unittest.TestCase):
    def test_demo_never_publishes(self):
        d = json.loads(POST.read_text())
        self.assertEqual(d['approval']['status'], 'draft')
        self.assertFalse(d['approval']['approved_at'])
        self.assertTrue(all(x['state'] == 'draft' and not x['remote_id'] for x in d['destinations']))

    def test_only_meta_destinations(self):
        d = json.loads(POST.read_text())
        self.assertEqual({x['platform'] for x in d['destinations']}, {'facebook', 'instagram', 'threads'})
        self.assertTrue(d['variants']['threads'])
        self.assertTrue(d['assets'][0]['license_or_permission'].startswith('UNKNOWN'))

if __name__ == '__main__':
    unittest.main()
