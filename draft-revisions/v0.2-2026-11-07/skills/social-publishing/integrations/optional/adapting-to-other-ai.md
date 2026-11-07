# Appendix: Adapting to Another AI

This skill is built for Muse. It is plain text, so another AI can read it. It is not tested outside Muse, and there are no guarantees there.

Read this file before you try the skill in another AI. Do not assume another AI can do what Muse can do.

## What transfers

These parts should transfer to most AIs, because they are instructions, not connections:

- The intake interview in [First Use](../../templates/first-use.md): personal or company, audience, goal, topics, voice, cadence, media rule, and approver.
- The story, writing, and approval rules in [Editorial](../../references/editorial.md) and [Approval and Records](../../references/approval-and-ledger.md): exact approval first, owned media first, no invented facts, and a recorded result per account.
- The media rights checks in [Image Search and Rights](../../references/images.md): your own photos and video first, permission for customer files, and a public domain file only as a fallback, with the exact file checked.
- The post record in [post.json](../../templates/post.json): one post, with variants, accounts, approval, and state per account.

## What does not transfer automatically

These parts depend on Muse, and you must prove them again in the other AI:

- Muse's direct connections to Facebook Pages, Instagram professional accounts, and Threads. Another AI may have no connection, a different connection, or a connection with different permissions.
- Muse's approval prompts and scheduling checks. Another AI may approve in a different way, or not at all.
- Muse's browser route for LinkedIn, TikTok, and other add-ons. Another AI may not have a browser, or may handle sign-in differently.
- Any claim in this repo about what a tool can do, what it costs, or what its limits are. Check the current provider terms and the actual tool in the other AI, at the time of use.

## How to adapt it, with no guarantees

Do these steps in order.

1. Start with the core rules only: intake, story, owned media, exact approval, and a private record. Do not start with publishing.
2. In the other AI, do a read-only check for each account you want. Ask it to list the account, and to confirm what it can do: upload the chosen media, post now, schedule, support a reply chain, and confirm the result. If it cannot prove that, treat publishing as untested.
3. Do one trial post, with a draft only, then with manual publishing. Give yourself the approved copy, file, credit, account, and due time, and ask for the live link afterward. Move to direct publishing only after that trial works.
4. For each add-on, repeat step 2 and step 3 for that channel. An add-on that works in Muse may not work in the other AI.
5. If a step depends on a Muse connection, mark it untested in the other AI until that AI proves it with a read-only check. Do not rewrite the skill to claim it works there.
6. Keep the approval rule the same in every AI: nothing is scheduled or published without approval of the exact version, for that exact account.

## What to tell the user

Tell the user, in plain words, that this skill was built for Muse, that another AI can read the instructions, and that publishing, scheduling, and verification are untested there until that AI proves them. Do not promise a result the other AI has not shown it can do.
