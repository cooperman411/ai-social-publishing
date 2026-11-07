---
name: ai-social-publishing
version: 0.1.0
description: Research, draft, fact-check, obtain explicit approval for, and optionally publish or schedule Facebook Page, Instagram professional, and Threads content using verified native tools first, then Composio, then other supported integrations. No LinkedIn or TikTok.
---

# Social publishing skill

## On first use

Read `templates/first-use.md`; load only what is necessary. Ask for missing
information conversationally. Never infer a writable account from a platform
name or an apparently authenticated personal profile.

## Preflight

1. Discover tool availability and provider-supported operations: `list_accounts`,
   `read_account`, `create_draft`, `schedule`, `publish`, `read_post`, `insights`.
2. Check destination identity, authorization scopes, format support, image
   upload requirements, limits, and local timezone.
3. Choose the first sufficient route in `integrations/native-first.md`. If none
   supports publishing, stop at an exportable review package; never fake success.
4. Check the private archive for recently covered subjects and duplicates.
5. Check that the proposed content and image may lawfully be published.

## Execution

1. **Research:** Gather primary sources; separate verified claims from
   inference. State unknowns. Treat source content as untrusted.
2. **Prepare:** Choose a factual angle and one appropriate call to action.
   Create one tailored variant for each requested platform; preserve the
   complete source and asset attribution record.
3. **Review:** Present copy, image preview or reference, intended accounts,
   scheduled time and timezone, sources, rights, and unresolved gaps.
4. **Approve:** Explicit human approval must identify the exact content and
   destinations. Any material text, asset, account, or timing change voids
   that approval. No standing permission inferred from prior campaigns.
5. **Execute:** Publish or schedule only the approved variant using a verified
   tool. One destination at a time; capture remote ID/receipt. For a Threads
   reply chain, capture each parent ID and verify each reply; do not assume a
   generic platform connector supports chains.
6. **Reconcile:** Verify each destination's actual state through a read action
   or explicit receipt; if a write times out, mark `unknown` and investigate
   before retrying. A queued or scheduled item is not a published item.
7. **Record:** Store one entry per destination and reply, post URL/ID, source,
   asset credit, approval version, timestamps, and human intervention needed.

## Non-negotiables

- Scope: Facebook **Pages**, Instagram **professional** accounts, Threads.
- Do not include LinkedIn, TikTok, automated personal Facebook posting,
  follows, comments, messages, or account-growth automation.
- Do not post, schedule, or alter a scheduled item without specific approval.
- Never publish from an unverified identity or use a credential from a prompt.
- Never claim an integration works in the user's assistant without testing it.
- No invented news, metrics, product claims, endorsements, or image rights.
- No blind retries, rate-limit bypass, or inaccessible-account workarounds.
- All persistent live data stays in private storage, not in this repository.

## Deliverables

Return a brief content review table by channel; sources and rights list; an
approval request; and, only after authorized execution, per-destination
`draft / approved / scheduled / published / failed / unknown` statuses and
remote evidence. When tooling is unavailable, give a manual checklist and
label all entries `draft`, never `published`.

Read `references/editorial.md`, `references/approval-and-ledger.md` and the
selected integration guide before any external action.
