# Approve, Schedule, and Record Posts

## Approve the Exact Post

Record the operator's approval, time, and version for each destination. Tie the version to the final copy, media, account, and intended time. Return any material change to draft and ask for approval of the revised version.

## Run the Calendar

Plan the cadence during intake. Keep a private calendar with a post ID, subject, angle, due time and time zone, and each destination's version and status. Read the current brief, calendar, and post history before preparing each batch.

If the operator authorizes a recurring run and a scheduler is available, use a single recurring check for the approved queue. Read the current pause state each time. When paused, stop new scheduling and publishing, and report any already scheduled items that may need separate action. For an active run, select only due, approved items. Verify the destination before submitting. Save each receipt as soon as it returns. Skip items already scheduled or published and check any uncertain attempt before retrying.

For manual publishing, give the operator a due list with the copy, image, credit, and account. Record the result when the operator supplies the post link or other confirmation.

## Record the Result

| State | Meaning |
| --- | --- |
| `draft` | Awaiting review or missing a requirement |
| `approved` | The operator approved this version and destination |
| `scheduled` | The provider confirmed a future post |
| `published` | A live post ID, link, or other receipt confirms publication |
| `failed` | The provider confirmed a failure |
| `unknown` | The outcome needs reconciliation before any retry |

Keep scheduling receipts separate from live post IDs. For a reply chain, record each segment's sequence number, parent ID, state, and returned ID or URL. If part of a batch fails, record the result by destination and resume only the affected items after checking their state.

At the end of the batch, update the private post history with the subject, angle, dates, sources, image credit, destinations, and confirmed results. Use this history before selecting new stories.
