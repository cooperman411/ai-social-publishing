# Second route: Composio

Use only when a sufficient native integration is absent or the user chooses it.
Composio is an intermediary for authenticated toolkits, **not** a social
network account or a substitute for platform permission review.

- Connect the intended Facebook Page, Instagram professional account, and/or
  Threads account through their currently supported authentication route.
- Confirm the exact Composio toolkit tool for media creation, publication,
  status lookup, and replies. Tool lists and OAuth scopes can change.
- Check whether the toolkit uses Composio-managed OAuth or requires the user
  to register their own app. Threads may require more setup.
- Explicitly verify account identity and write authorization. Some API routes
  support only certain account types, media formats, or feature subsets.
- Obtain approval in the skill **before** invoking a write tool. Record the
  provider response and read back post details when available.
- Check Composio tool-call limits, third-party provider charges and any premium
  tool costs **live**. The free tier is not a guarantee that every operation is
  free or that a platform grants publishing approval.

Official pricing: https://composio.dev/pricing
Toolkit catalog: https://docs.composio.dev/toolkits
