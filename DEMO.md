# Demo run

A real run of `mine-chats` on the 30 invented chats in `examples/`. They're from a fictional freelancer, "Sam", across Claude Code, Codex, Hermes and ChatGPT.

**The prompt:** `find the ideas in my old chats, use the example chats`

**What ran:**
1. `scripts/extract.py --examples` found 30 chats (11 claude-code, 7 chat-export, 8 codex, 4 hermes-or-jsonl) and wrote 1 shard.
2. One `chat-reader` subagent read the whole shard and wrote 25 findings: 15 sellable, 3 insights and 7 repeated jobs, each with an exact quote.
3. `rank-ideas` merged them into 3 sellable ideas, 3 insights, 2 skills and 1 wish.
4. Three `demand-scout` subagents ran in parallel, one per idea, searching the web, Reddit, forums and X. They kept 17 real posts and named 20 existing products.
5. `write-report` wrote the four files below.

The demand step searches the live web, so your run will find different posts.

---

# Ideas in your chats

Read 30 chats (11 claude-code, 7 chat-export, 8 codex, 4 hermes-or-jsonl), 2026-01-08 to 2026-10-20.

## Do this one first: Quotes from a voice memo, for tradespeople
A tradesperson records a voice memo walking the job and gets a priced quote PDF from their own price list.
- **Why it's first:** Four people asked for it unprompted (a plumber, an electrician, a roofer, and a supplier rep with about 400 trade customers), one paid $200, and it turns a Sunday of typing quotes into 10 minutes.
- **Your chats that show it:**
  - 2026-03-04 (c0003): "this is actually working. he just sent 3 quotes from the van in 10 min instead of his sunday"
  - 2026-04-19 (c0007): "Dave's electrician mate Priya wants the quote thing too. she asked if she can pay for it."
  - 2026-06-02 (c0013): "a plumber and an electrician have been using a quote tool I hacked. Priya paid me $200 for setup. what would I charge if I turned it into a monthly thing for trades?"
  - 2026-08-21 (c0022): "third tradie this month asking about the voice memo quotes thing (a roofer this time). should I just make this a product?"
  - 2026-10-12 (c0028): "a supplier rep asked if he could offer the voice memo quote tool to his trade customers. he has like 400 of them"
- **Who wants it right now:** see [WHO-WANTS-IT.md](WHO-WANTS-IT.md). Short version: the app already exists (about a dozen launched this year, from $29.99 a month). Nobody sells it set up on a tradesperson's own price list. Your supplier rep with about 400 trade customers is the way in.

## 2. Stripe payouts matched to QuickBooks, done for you
Splits each Stripe payout into its charges, fees and refunds so it matches the bank deposit in QuickBooks.
- **Why:** Three people asked for it (a candle shop owner, then two sellers in a Shopify group), the first now wants to pay monthly, and it cut month-end from 4 hours to 20 minutes.
- **Your chats:**
  - 2026-02-10 (c0001): "spent 4 hours again matching stripe payouts to quickbooks deposits. stripe batches fees and refunds into one payout and quickbooks shows one lump. write me a script that splits each payout into its charges, fees and refunds"
  - 2026-05-07 (c0009): "the payout splitter script broke on disputes. also my friend Lena who runs a candle shop asked for it, she has the same problem every month"
  - 2026-09-15 (c0025): "month end again. ran my payout splitter, 20 minutes instead of 4 hours. two people in the shopify sellers group asked me for it after I mentioned it"
  - 2026-10-20 (c0029): "Lena asked if I can run the payout splitter for her every month and she'll pay"

## 3. Why customers return things, for Shopify stores
Groups free-text return reasons into causes and shows which products get sent back for which reason.
- **Why:** One client asked for it monthly after it cut returns on two styles by fixing a size chart; a real result, but only one asker so far.
- **Your chats:**
  - 2026-07-12 (c0017): "client sells shoes on shopify and has no idea why people return stuff. the return reasons are free text. can we group them into reasons and show which products get returned for sizing"
  - 2026-07-30 (c0019): "client loved the returns breakdown, they cut returns on two styles by fixing the size chart. they want it monthly"

## Wishes: ideas you keep coming back to that nobody has asked for yet
- **Mood journal app:** 4 chats, January to September. Nobody has asked for it. Before you build, find one person who wants it.

---

# Who wants it

Real public posts the demand scouts opened and checked. All three found the same thing: apps for each idea already exist, and none of them is sold as a done-for-you service.

## Quotes from a voice memo, for tradespeople

**People asking (4):**
- **2025-11-17 · reddit · u/Ahlanfix, an electrician, r/automation**: "Tried a few things. Templates helped a little. Blocking time in the morning instead of evenings helped a little. Neither solved the core problem which is that the estimate still has to get written from scratch after every visit." ([link](https://www.reddit.com/r/automation/comments/1tcv8lk/how_to_send_estimates_faster_as_an_electrician/))
- **2025-09-21 · reddit · u/Forward_Ad_4117, owner of a small remodeling business, r/artificial**: "i run a small remodeling business and estimating is honestly the worst part… still stuck doing everything in spreadsheets and it takes forever" ([link](https://www.reddit.com/r/artificial/comments/1smb4jd/construction_estimating_software_that_uses_ai_has/))
- **2026-03-19 · forum · Leon M, UK Business Forums, thread starter**: "right now it’s a mix of notes, photos, and doing quotes later at home, which isn’t ideal. There are loads of apps out there (Jobber, Tradify, QuickBooks), but most of them feel quite heavy for solo trades or small teams. Ideally looking for something mobile-first where you can: keep job details / track photos / put together quotes / not spend evenings doing admin" ([link](https://www.ukbusinessforums.co.uk/threads/what-apps-are-trades-using-for-quoting-jobs-now.430559/))
- **2026-10-06 · forum · KaiVenturaPSP, UK Business Forums reply in the same thread**: "photos and a voice note on site, then send a short quote the same day from a saved template" ([link](https://www.ukbusinessforums.co.uk/threads/what-apps-are-trades-using-for-quoting-jobs-now.430559/))

**What they use now:**
- **WalkQuote (iPhone)**: Free for 3 quotes a month; Pro $29.99/month or $199.99/year. iPhone only; the listing does not say quotes are priced from the tradesperson's own price list, and there is no setup help.
- **Kvota**: Free 5 docs/month; Pro $29.99/month (PeerPush listing, 2026-03-27). General voice quoting for any job; no trade-specific price lists or supplier tie-in stated.
- **Easy Invoice & Quote Maker (Quotes & Notes, iPhone)**: Free to use, a paid plan is needed to send; listing shows A$17.99/month or A$199.99/year and inconsistent in-app prices. Voice-to-text fills lines one at a time; it does not read a walkthrough and price it.
- **VoxTrade**: not confirmed (page blocked). Self-serve app that promotes itself in the UKBF thread; does not do setup of the buyer's own prices as a service.
- **Bizzen**: one r/automation poster says his whole Bizzen stack costs about $450/month (likely a promotional post). A whole bundle (calls, invoicing, expenses) rather than a quote tool alone, priced for a business that wants all of it.
- **Jobber (voice mode in its AI assistant, beta)**: $69-$349/month per a third-party guide (not verified). Quoting is called weak by a UKBF reply ('Absolutely do not consider Jobber for quotes') and the app is heavy for solo trades.
- **DIY: ChatGPT voice or Whisper + n8n + Claude**: tool costs only, plus the tradesperson's own build time. Needs a technical person to build and maintain, which a plumber or roofer does not have.

**The opening:** At least a dozen self-serve voice-to-quote apps launched in 2026, so a new app is not the gap; the posts show the pain is real but nobody sells it set up on the tradesperson's own price list, and your own chats show distribution through a supplier rep with about 400 trade customers and one $200 setup sale (inference from your chats, not from these posts).

**First move:** Reply to u/Ahlanfix on the r/automation thread and ask where his prices live (spreadsheet, supplier price list, his head) and what he would need to see in a draft quote to send it unchanged.

## Stripe payouts matched to QuickBooks, done for you

**People asking (8):**
- **2026-06-29 · Make community forum · Monika_Conti, works for a small charity that takes donations through Stripe into QuickBooks (Make community)**: "I have to then do manual journal entries to categorise them correctly" ([link](https://community.make.com/t/stripe-payouts-quickbooks-reconciliations-for-a-charity/111494))
- **2026-02-24 · QuickBooks Community forum · d-m (QuickBooks Community)**: "when I categorize payouts they aren't decreasing the undeposited funds account." ([link](https://quickbooks.intuit.com/community/reports-and-accounting-5/stripe-payouts-integration-transactions-are-not-debiting-from-undeposited-funds-61100))
- **2026-01-06 · Shopify community forum · masonwright757, a seller speaking about their own store (Shopify community, post 14 in the thread)**: "For us, the hardest part has been understanding why the payout amount is different from what we expect." ([link](https://community.shopify.com/t/how-do-you-reconcile-shopify-orders-with-stripe-payouts-without-losing-your-mind/580987))
- **2025-12-26 · Shopify community forum · jennifeergordonn, new Shopify seller (same thread, post 2; follow-up 2026-01-02)**: "I’m still new to Shopify, but I’ve noticed payouts rarely match orders 1:1 because of fees, refunds, and payout timing." ([link](https://community.shopify.com/t/how-do-you-reconcile-shopify-orders-with-stripe-payouts-without-losing-your-mind/580987))
- **2025-08-18 · QuickBooks Community forum · accounting673 (QuickBooks Community); older than 12 months, about 15**: "Having the payouts also go into Undeposited Funds makes the balance of Undeposited Funds duplicate the payments." ([link](https://quickbooks.intuit.com/community/other-questions-9/i-m-using-the-stripe-connect-app-to-integrate-with-stripe-is-there-a-way-to-have-stripe-payouts-create-a-bank-deposit-instead-of-a-transfer-into-undeposited-funds-91513))
- **2025-01-03 · QuickBooks Community forum · IAdventure (QuickBooks UK community); older than 12 months, about 22**: "but do not know how to apply the -£21.50 so that it matches the 3 open invoices and the 2 refund payments." ([link](https://quickbooks.intuit.com/learn-support/en-uk/transactions/stripe-refund-combined-with-customer-payout/00/1519852))
- **2024-06-28 · QuickBooks Community forum · killian-otavo-ie (QuickBooks Community); older than 12 months, about 17**: "it seems stupid that you can import these fees as an expense but then can't match them" ([link](https://quickbooks.intuit.com/learn-support/global/manage-customers-and-income/how-do-you-reconcile-stripe-invoices-fees-against-bank/00/1457973))
- **2024-06-04 · Zapier community forum · Regency Fiction Writers (Zapier community); older than 12 months, about 17**: "I'd like to be able to have Stripe upload bank payout info to our Quickbooks account" ([link](https://community.zapier.com/how-do-i-3/how-to-trigger-zap-for-stripe-bank-payouts-to-update-quickbooks-online-39838))

**What they use now:**
- **QuickBooks Online native Stripe connector (Intuit)**: No separate price on Intuit's help page. Imports sales, refunds, payouts and adjustments, but users in the posts above still fight it: payouts become a transfer into Undeposited Funds that duplicates the payments (accounting673), clicking Add instead of Match creates a second deposit (d-m thread), and the fee will not match without a manual negative line (killian).
- **Synder**: Basic $52/mo (500 synced transactions, billed yearly), Essential from $103, Pro from $240, Pro Max from $480; the page also shows $65/$129/$299/$599 and its structured data differs, so confirm before quoting. Monthly subscription tiered by transaction count, and the pricing page does not itself state per-payout reconciliation; it is software you set up and monitor, not someone who closes the month.
- **S2Q (Show HN, 28 Jul 2026, 2 points)**: Credits per synced Stripe transaction: $10 per 100, $50 per 1,000, $150 per 10,000; no subscription. QuickBooks Online and USD only: no Xero, no QuickBooks Desktop, no multi-currency, no Shopify/PayPal sources. Posts each payout as a deposit through a clearing account with a free dry run. Self-serve, so the seller still owns the exceptions.
- **A2X (for Shopify, Etsy, Amazon sellers)**: From $29/mo per channel (Walmart $79). Its pricing page lists marketplaces and PayPal but does not list Stripe, so a Stripe-only seller is not clearly covered.
- **Freelancers on the Make community (done-for-you builds)**: Quotes to the charity above: $125 mapping review, $149 audit then $499 build, USD 200 to 250 fixed or first milestone, $300 to 700 (n8n), $400 to 600 (Make), US$500 first-stage export. One-off automation builds that the buyer then has to maintain; none quoted a monthly service that runs and checks each payout, and none addressed refunds or disputes in the quotes I read.
- **By hand: Stripe payout report plus a QuickBooks bank deposit with a negative fee line**: Free; the posters report hours of month-end time. The workaround QuickBooks staff actually give; it breaks on refunds netted into later payouts and on duplicate fees (IAdventure, killian).

**The opening:** Software in the threads is either a subscription tiered by transaction count (Synder from $52 a month), QuickBooks Online and USD only (S2Q), or the Intuit connector people say still duplicates deposits; the human help on offer is a one-off build. I found no one offering to run the monthly payout tie-out, including refunds and disputes that land in a later payout, for a flat fee, but that is an absence in what I could search (Reddit was blocked), not proof.

**First move:** Reply to masonwright757 in the Shopify community thread (6 Jan 2026) with a question only: how many Stripe payouts a month do you tie out, how long does one month take, and are the books in QuickBooks Online or Xero?

## Why customers return things, for Shopify stores

**People asking (5):**
- **2026-01-20 · reddit · u/Business_Panda_1529, runs a small Shopify clothing brand (about 22% return rate)**: "Running a small clothing brand on Shopify and hitting about 22% return rate. When I look at the return reasons, most just say "didn't fit" or "wrong size" but that tells me nothing actionable." ([link](https://reddit.sentinel-team.org/posts/1qi6wbx/snapshots/2026-01-21T17%3A10%3A47.38402Z))
- **2026-01-20 · reddit · u/Business_Panda_1529 (same person as the r/ecommerce post, cross-posted the same day)**: "Most returns just say "didn't fit" or "wrong size" with zero specifics." ([link](https://reddit.sentinel-team.org/posts/1qi6y10/snapshots/2026-01-20T21%3A31%3A48.965842Z))
- **2026-05-20 · reddit · u/Camp-Affectionate, commenter on u/hangrsolutions' post '"expected" vs "actual" return rate costs across various DTC categories'**: "they were the ones who actually read their own return reasons every month" ([link](https://reddit.sentinel-team.org/posts/1tia1q4/snapshots/2026-05-21T05%3A34%3A42.738794Z))
- **2026-11-01 · x · Andrew Collins, paid acquisition for apparel and footwear brands (bio: 'Returns-adjusted ROAS')**: "Then export the last 30 days of returns by reason and sort "Too big" and "Too small" by product. That's the size-chart to-do list." ([link](https://x.com/DTCCollins/status/2116931774957965750))
- **2023-12-16 · x · Johnny Hickey, CMO of a $60M women's tee shirt brand (bio), replying to @PurushaPat**: "No! I want a report that cross references CR by product page, returns by product, color, size, deep available stock and CR by traffic source eg FB/google." ([link](https://x.com/johnhickey1970/status/1736082105682043339))

**What they use now:**
- **ReasonWhy (Shopify app)**: Starter $49/mo for 100 analyzed returns, Growth $99/mo for 500, Pro $199/mo unlimited. Listing launched 2026-06-15, 0 reviews. Its own site says the first 50 returns are analyzed free.. Does what the idea does (AI groups return notes into themes like 'runs small', 'not as pictured', ranks products by revenue at stake, suggests page fixes). Gap is price and cap: $49 a month for 100 returns, no reviews yet, and it is software with no one reading the result for the store.
- **ReturnRadar (Shopify app, WiseApps)**: Free up to 100 orders/mo; $9 (1,000 orders); $19 (10,000 orders, adds AI classification); $49 (100,000 orders). Launched 2026-04-06, 0 reviews.. SKU-level return rates and cost per SKU; the AI sort into Size and Fit, Quality and Not as Described is only on the $19 plan and up. Limits are per order, not per return. No reviews, so no evidence stores trust it.
- **Return Audit (Shopify app)**: Free. Launched 2026-08-20, 0 reviews.. Names the products, sizes and customer reasons behind returns with a suggested fix per product, but the listing says it covers only the last 60 days of orders, so a monthly trend or before-and-after needs the store to keep exporting.
- **ReturnGO 'Return Reasons by Product' report**: Not shown on the docs page; not checked.. Table of product, variant, reason and the customer's follow-up answer, with return rate and CSV export. It lives inside ReturnGO's returns portal, so a store on Shopify's own returns or another portal has to switch to get it. The docs do not describe grouping free text into causes.
- **Report Pundit 'Return Reason Analysis' report**: Free under 1,000 lifetime orders; Essential $9 to $45 a month by Shopify plan; Essential Plus $14 to $60.. A general report builder. The page shows return reasons and recurring patterns but does not say it breaks out by product or SKU or groups free text. Someone still has to read the report and decide what to fix.
- **Shopify's own returns-by-reason report plus category reasons**: Included with Shopify.. Since 2026-01-16 apparel returns get 'Too big' and 'Too small' by product category. The changelog does not mention a report broken down by product, and the reasons are fixed labels, not the free text the client's customers write.
- **Free Claude Code skill shopify-admin-return-reason-analysis (40rty-ai)**: Free. Listing seen in search results only; page not opened.. Per the search summary it aggregates returns by reason code, product and SKU with a minimum-returns threshold, and needs Shopify CLI access with read_orders and read_returns scopes. A store owner would not set that up.

**The opening:** Four Shopify apps that do this (ReasonWhy, ReturnRadar, Return Audit, plus ReturnGO's table) listed between April and August 2026 with zero reviews, and the only two asks found (Jan 2026) came before most of them existed, so as a standalone app this is already built three times; what none of them offers is a person who reads the notes each month and tells a shoe or clothing brand which size charts and pages to change, which is the thing the chat client paid for.

**First move:** Reply to @DTCCollins on X (he sells to apparel and footwear brands) and ask how his clients do the 'Too big / Too small by product' sort today and how many returns a month it covers; then ask u/Business_Panda_1529 on r/shopify whether they ever found a way to see why their 22% came back, without naming any product.

---

# Insights worth keeping

- **Open cold emails with a line about their Google review** (2026-04-02): "cold emails to local shops: replies went from 2 to 9 out of 50 when I opened with one line about a review they got on google. writing this down"
- **Charge per job, not per hour, for small automations** (2026-06-18): "stopped charging by the hour for small automations and started charging per job. same work, clients say yes faster and I make more. why does that work"
- **Client setups stick when one person on their side owns it** (2026-08-05): "lesson: every client setup that stuck had one person on their side who owned it. the two that died had nobody"

**Worth posting:** the cold-email one. It has a real before and after: 2 replies out of 50 became 9 when the email opened with a line about the shop's Google review.

---

# Jobs you keep asking for: skills to write

## Chase overdue invoices: 4 times (2026-02-24, 2026-04-24, 2026-06-26, 2026-08-26)
```
1. List invoices over 30 days.
2. Draft a short, friendly nudge for each, naming the invoice and amount.
3. Get firmer on the second nudge.
4. Show the drafts before anything is sent.
5. Log who was nudged and when.
```

## Support thread to FAQ entry: 3 times (2026-05-15, 2026-07-20, 2026-09-28)
```
1. Read the support thread.
2. Pull out the customer's question in their words.
3. Write the answer in 3 to 5 lines.
4. Add one example.
5. Suggest where it goes on the help page.
```
