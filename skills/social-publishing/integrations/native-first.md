# First route: native host integrations

Check for tools **actually exposed to the current session** before naming a
provider. Different ChatGPT, Claude, Hermes, and other environments expose
different integrations. Connected read access is not publish access.

1. Enumerate available social apps and operations, including account listing,
   media upload, draft, scheduling, publishing, post lookup and insights.
2. Validate the account type and intended Page/professional/Threads identity.
3. Use a read-only identity/permission check; do not publish a test post.
4. Confirm that the tool can preserve media and captions on that platform.
5. Use only the least-privileged operation necessary; obtain content-specific
   approval before any external write.

**Muse:** If the host offers authenticated Muse-native Facebook Page, Instagram,
or Threads tools, prefer them. Do not hardcode private account IDs, assume a
universal Muse command-line API, or paste session credentials. Re-probe
supported operations each run. Other hosts do not inherit Muse connections.

**Other native tools:** An official host-installed platform connector or a
vendor MCP connector can be used when it provides the exact required action,
scopes, and confirmation receipt. Do not claim universal one-click availability.

**No direct publishing:** Prepare a reviewed content package. A human may
publish through the official application and supply the URL for ledger update.
Never automate an unsupported personal profile through browser workarounds.
