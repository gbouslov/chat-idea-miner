# chat-idea-miner (for Codex and other agents)

When the user asks to find ideas in their old chats, follow `skills/mine-chats/SKILL.md` step by step. Where it says "subagent", run that skill yourself for each shard or idea (or in parallel if your tools allow it):
- shard reading: `skills/read-chats/SKILL.md`
- ranking: `skills/rank-ideas/SKILL.md`
- demand search: `skills/find-demand/SKILL.md` (needs web search)
- report: `skills/write-report/SKILL.md`

Codex sessions live in `~/.codex/sessions`, Claude Code in `~/.claude/projects`. Everything stays local; outputs go to `out/`.
