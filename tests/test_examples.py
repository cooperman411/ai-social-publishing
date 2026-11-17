import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POST = ROOT / 'skills/social-publishing/examples/fictional-post.json'
SKILL = ROOT / 'skills/social-publishing/SKILL.md'
README = ROOT / 'README.md'
FIRST_USE = ROOT / 'skills/social-publishing/templates/first-use.md'
IMAGES = ROOT / 'skills/social-publishing/references/images.md'

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

    def test_muse_first_and_no_fixed_cadence(self):
        skill = SKILL.read_text()
        self.assertIn('Muse first', skill)
        self.assertIn('Meta first', skill)
        self.assertIn('no fixed cadence', skill.lower())
        intake = FIRST_USE.read_text()
        self.assertIn('personally, or for a company', intake)
        self.assertIn('Schedule', intake)
        self.assertIn('You decide how often to post', intake)
        self.assertIn('Seven times a week is fine', intake)
        self.assertIn('To confirm', intake)
        self.assertIn('never invents a value', intake)

    def test_personal_cross_posting(self):
        skill = SKILL.read_text()
        self.assertIn('Personal cross-posting', skill)
        intake = FIRST_USE.read_text()
        self.assertIn('personal post as well as a company post', intake)
        self.assertIn('Personal Facebook is text only', intake)
        readme = README.read_text()
        self.assertIn('personal', readme.lower())

    def test_fictional_example_marked(self):
        d = json.loads(POST.read_text())
        self.assertIn('Fictional example', d['variants']['facebook'])
        self.assertIn('do not publish', d['assets'][0]['attribution'].lower())
        self.assertIn('Synthetic example', d['notes'])

    def test_public_domain_sources(self):
        images = IMAGES.read_text()
        for name in ('Openverse', 'Internet Archive Book Images', 'Unsplash', 'NASA'):
            self.assertIn(name, images)
        self.assertIn('Use a real photo first', images)

    def test_ongoing_manager_prompt(self):
        readme = README.read_text()
        self.assertIn('ongoing social media manager', readme)
        self.assertIn('walk me through setup one question at a time', readme)

if __name__ == '__main__':
    unittest.main()
