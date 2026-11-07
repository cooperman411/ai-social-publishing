# AI Social Publishing

A vendor-neutral, AI-assisted workflow for researching, drafting, approving,
and publishing to **Facebook Pages, Instagram professional accounts, and Threads**.
No LinkedIn, TikTok, or personal Facebook profile automation is implemented.

**Status: initial skill package.** It has documentation, fictional examples, and
offline validation, but has **not** been tested against live social accounts.
It is not a hosted scheduler, an authenticated connector, or an autonomous publisher.

## The simple idea

Tell an AI assistant what you want to share. It researches and verifies the
content, checks image rights, adapts copy for each channel, and presents a
reviewable approval package. Only after an explicit approval may a connected
publishing tool schedule or publish the exact approved content. Each channel
gets an independent status and provider receipt.

**Integration order:** host-native tools (including Muse, where available),
then Composio, then other documented providers such as Buffer, then an
approved manual route. Discover actual capabilities; never assume the same
service exists in ChatGPT, Claude, Hermes, or another host.

## Start with your AI assistant

Copy this prompt:

```text
Help me use the AI Social Publishing skill in this folder or repository.
Read README.md, skills/social-publishing/SKILL.md, and its referenced files.
Check your actual publishing tools and permissions first. Walk me through
short first-use setup, then prepare one fictional or real post for review.
Do not publish, schedule, connect new accounts, or purchase services without
my explicit authorization. Never assume LinkedIn is a destination.
```

If your assistant cannot read a repository, provide the `skills/social-publishing`
folder and the files it references. A manual-only assistant can prepare the
same approval package and record statuses without publishing.

## First run

1. Establish the brand voice, platforms, destination accounts, locale, and any
   prior-publication archive. See `templates/first-use.md`.
2. Probe native read/write/schedule capabilities. Use Composio only if native
   tools do not meet the need. See `integrations/`.
3. Research and verify facts and assets. Prepare one tailored channel variant.
4. Show the exact copy, source links, media credits, destinations, and planned
   timing. Obtain approval tied to that version.
5. Publish or schedule only with a verified supported write tool; reconcile
   status using a post ID or URL. Never retry an uncertain publish blindly.
6. Retain a private post ledger and reuse it to prevent duplicates.

## Contents

- `skills/social-publishing/SKILL.md` — authoritative workflow.
- `skills/social-publishing/references/` — editorial, approval, and ledger rules.
- `skills/social-publishing/integrations/` — integration-specific guidance.
- `skills/social-publishing/templates/` — short setup and portable post schema.
- `skills/social-publishing/examples/` — fictional content, never real profiles.
- `tests/` — offline validation of the example and policy boundaries.
- `SOURCES.md` — vendor and API references, checked 2026-11-06.

Run offline checks: `python3 -m unittest discover -s tests -v`.

## Boundaries

This is a skill, not a subscription service. Publishing requires a supported,
authorized connector or human operator. Platform terms, features, pricing, and
API approval requirements change. Personal accounts are not assumed API-
accessible. Images require rights review. A draft, scheduled item, and live
post are different states. Use at your own risk; the MIT license supplies no
warranty.
