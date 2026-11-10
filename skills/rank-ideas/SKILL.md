---
name: rank-ideas
description: Merges what the chat readers found across all shards into one ranked list of sellable ideas, insights and repeated workflows, each with every chat that supports it. Used by mine-chats after read-chats.
---

# rank-ideas

Read every `work/found/*.jsonl`. Merge findings that are the same idea under different words. Write `work/ranked.json`:

```json
{"sell": [{"name", "what", "score", "why_rank", "chats": [{"chat", "date", "file", "quote"}], "signals": {"asked": n, "paid": n, "result": n, "repeat": n}, "first_seen", "last_seen"}],
 "insights": [...], "workflows": [{"name", "times", "chats": [...]}], "wishes": [...]}
```

## How to rank sellable ideas
- **Pull beats polish.** An idea three other people asked for beats a beautiful one nobody asked for. Count distinct askers, not mentions.
- **Money beats praise.** Paid or offered to pay goes above "loved it".
- **A measured result** (4 hours to 20 minutes) makes it easy to sell. Note the number.
- **Still alive:** last seen recently counts more than an idea from a year ago that stopped.
- **Wishes go to their own list** with their chat count, said kindly: "12 chats, nobody asked yet".
- Write `why_rank` as one plain sentence a stranger would follow: "Three tradespeople asked for it unprompted, one paid $200, and it turns a Sunday of typing into 10 minutes."

Keep the top 3 sellable ideas for find-demand. Keep every insight that has a result, and every workflow that came back 3 or more times.
