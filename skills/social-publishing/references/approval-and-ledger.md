# Approval, states, and retries

Approval binds a **specific version** of content, media, destination account,
and schedule. The review package must show all of them. Record an approval
receipt (human decision, timestamp, version/reference); never store signatures
or authentication secrets in a public repo. On any material edit, revert to
`draft` and request approval again.

Use one state per destination:

| State | Meaning |
| --- | --- |
| `draft` | Unapproved or incomplete; cannot publish |
| `approved` | Exact version and destination approved, not executed |
| `scheduled` | Provider verified a future scheduled item |
| `published` | Provider verified a live post by ID or URL |
| `failed` | Confirmed failure; remediation required |
| `unknown` | Timeout/ambiguous outcome; reconcile before retry |

Never convert `unknown` to `failed` merely because a request timed out.
Always check provider activity first; retries can create duplicate posts.
Record each individual Threads reply with its parent reference and result.
Multiple platforms may partially succeed: do not report campaign completion
until each selected destination is accounted for.

A schedule is not an automation permission. Scheduled runs may look up due
items, but publishing still requires the approved content/destination version.
No background monitoring should be claimed unless the host provides an active
scheduler and the account connection remains valid.
