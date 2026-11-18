# AI Social Publishing for Muse

Use Muse as your ongoing social media manager for Facebook Pages, Instagram professional accounts, and Threads. Muse researches stories, drafts each version for its account, and keeps a record of what went out. You review the exact copy, media, and timing, and nothing gets scheduled or published until you approve it. The focus is professional use. Personal cross-posting is an option, occasionally or always.

## Start

Paste this prompt into Muse.

```text
Help me set up Muse as my ongoing social media manager for my Meta accounts using this repository.
https://github.com/cooperman411/ai-social-publishing

Read the README and the publishing playbook, then walk me through setup one question at a time.
```

Muse follows the [publishing playbook](skills/social-publishing/SKILL.md). Give it a topic, an audience, and any photos, video, or sample posts you want it to use. If Muse cannot open the link, give it the playbook and the files it references.

## Install as an agent skill (optional)

For an AI agent that supports the [Skills CLI](https://skills.sh/docs), install from GitHub:

```bash
npx skills add cooperman411/ai-social-publishing
```

The installer discovers the `social-publishing` skill. This does not connect accounts or install the skill into Muse automatically. For the intended Muse workflow, use the **Start** prompt above and follow the account setup guide.

## Plan and Draft

1. Set a goal for the post. For a batch, agree on the topics, accounts, posting times, time zone, and review deadline. See the [publishing brief](skills/social-publishing/templates/first-use.md).
2. Ask Muse to check the facts against primary sources and use your recent post history to avoid repeating a story. See the [editorial guide](skills/social-publishing/references/editorial.md).
3. Start with your own photos or video. For outside media, verify that you can use the exact item and record the required credit. See the [media guide](skills/social-publishing/references/images.md).
4. Have Muse adapt the copy to each account. For example, a shop hosting a repair workshop might use the date and location in a Facebook Page post, a workshop photo on Instagram, and the registration link on Threads.

## Check Your Accounts

Use [Muse’s account setup guide](skills/social-publishing/integrations/muse-first.md) to connect the accounts you choose. Ask Muse to check which actions each account supports, such as attaching media, scheduling, or posting a Threads reply. When an action is unavailable, keep that version in draft. You can use the approved copy and media to post it yourself. For personal cross-posting, Facebook personal is text only in Muse. A personal photo or video needs the browser route or manual posting.

## Approve and Publish

Review the exact copy, media, source, credit, account, and proposed time for each version. Approve the version you want Muse to schedule or publish. Review it again if the copy, media, account, or time changes.

Keep the brief, calendar, approvals, and post history in private storage. Save a scheduling receipt when the platform confirms a future post. Record a live link or post ID when the post goes out. Check the account before retrying an uncertain result.

For recurring work, approve the Muse task separately. Muse checks the current plan and pause status before it acts on due, approved posts. See the [approval and records guide](skills/social-publishing/references/approval-and-ledger.md).

## Files and Examples

- The [fictional draft](skills/social-publishing/examples/fictional-post.json) shows what a post record contains.
- The [MIT License](LICENSE) covers the repository.

## Other Public Projects

- [AteBit.Tech](https://github.com/cooperman411/AteBitTech)
- [AI Sales Prospecting & Outreach](https://github.com/cooperman411/ai-sales-prospecting-outreach)
- [AI Social Publishing for Muse](https://github.com/cooperman411/ai-social-publishing)
- [Hotel Group Sourcing Skill](https://github.com/cooperman411/hotel-group-rfp)
- [Hotel Revenue Management Toolkit](https://github.com/cooperman411/hotel-revenue-management)
- [Job Search Simplified](https://github.com/cooperman411/job-search-simplified)
- [PT/OS One](https://github.com/cooperman411/plain-text-os-one)
- [PT/OS Workspace](https://github.com/cooperman411/plain-text-os)
