import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POST = ROOT / 'skills/social-publishing/examples/fictional-post.json'
SKILL = ROOT / 'skills/social-publishing/SKILL.md'
README = ROOT / 'README.md'
FIRST_USE = ROOT / 'skills/social-publishing/templates/first-use.md'

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

    def test_no_blog_mention(self):
        for path in (SKILL, README, FIRST_USE):
            text = path.read_text().lower()
            self.assertNotIn('blog', text, f'{path} must not mention a blog; that is a separate skill')

    def test_muse_first_and_no_fixed_cadence(self):
        skill = SKILL.read_text()
        self.assertIn('Muse first', skill)
        self.assertIn('Meta first', skill)
        self.assertIn('no fixed cadence', skill)
        intake = FIRST_USE.read_text()
        self.assertIn('Personal or company', intake)
        self.assertIn('Cadence', intake)

    def test_appendix_on_home_page(self):
        appendix = ROOT / 'APPENDIX.md'
        self.assertTrue(appendix.exists())
        text = appendix.read_text()
        for name in ('LinkedIn', 'TikTok', 'Composio', 'Buffer', 'another AI'):
            self.assertIn(name, text)
        self.assertIn('APPENDIX.md', README.read_text())
        self.assertIn('Muse first', README.read_text())

if __name__ == '__main__':
    unittest.main()
