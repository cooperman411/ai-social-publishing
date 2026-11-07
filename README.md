# AI Social Publishing

Use your AI assistant to prepare posts for Facebook Pages, Instagram professional accounts, and Threads. Give it a topic, the audience, and any company material you want it to use. It checks the facts and image rights, writes for each channel, and gives you the posts to review.

For example, a shop hosting a repair workshop could give the assistant the event details and a photo it owns. The assistant can draft a Facebook post with the date and location, an Instagram caption for the photo, and a short Threads post with the registration link.

## Try It With One Post

Open the [skill](skills/social-publishing/SKILL.md) in your assistant, or give it the `skills/social-publishing` folder. Paste this request and fill in the details you know.

```text
Prepare one post for [audience] about [topic]. Read the social publishing
skill. Use [brand notes or sample posts] for the voice. Write a version for
each of [channels]. Show me the copy, sources, image and credit, intended
accounts, and proposed timing. Keep everything as a draft for review.
```

The [setup questions](skills/social-publishing/templates/first-use.md) cover the details the assistant needs. Start with an approved source and an image you can use. If an image's rights are unclear, resolve them before approving the post.

## Review and Publish

Review the copy and image for each account. Check the credit and the proposed time. Approve the version you want to publish or schedule. Review any later change to the copy, media, account, or timing before it goes out.

Use a [connected tool](skills/social-publishing/integrations/native-first.md) if it can publish to the account you chose. The assistant checks native tools first, then [Composio](skills/social-publishing/integrations/composio.md) and options such as [Buffer](skills/social-publishing/integrations/buffer.md). You can also take the reviewed copy and image to the platform and post it yourself.

Keep a private record of what went out, where, and when. Record a scheduled post as scheduled. Update the record when you have confirmation that it is live.

## Project Status

The repository contains the workflow, templates, and a [fictional draft](skills/social-publishing/examples/fictional-post.json). Testing so far covers the offline example. Publishing depends on the tools and permissions available for your account.

See the [editorial reference](skills/social-publishing/references/editorial.md) for facts and images, and the [approval and record guide](skills/social-publishing/references/approval-and-ledger.md) for publishing status.
