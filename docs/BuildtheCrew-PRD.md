# PRD: BuildtheCrew

**Author:** Brent O'Malley
**Date:** 2026-05-08
**Status:** Draft — Stage 4 (Solution Review)

---

## 1. Hypothesis

We believe that giving distributed family + friend "crews" an AI-powered coordination app for aging-in-place loved ones will increase the number of older adults who successfully remain in their homes (vs. moving to assisted living) by reducing coordinator burnout and missed care tasks, measured by **% of loved ones still aging-in-place at 12 months post-crew-formation** (target: lift over the `[NEED: industry baseline]` cited in Section 6).

Because a 12-month outcome is too slow to steer the product, we validate progress against two leading indicators at 6 months:

- **Crew durability:** ≥ `[NEED: target — recommended 60%]` of crews still active 6 months after signup. Tied to Defensibility pillar 1 (multi-party coordination graph forming).
- **Lead-caregiver burnout reduction:** ≥ 25% drop in self-reported burnout score (validated instrument, e.g., Zarit Burden Interview short form) versus the crew founder's intake baseline. Tied directly to the second mechanism in the hypothesis above.

If both leading indicators move and the 12-month outcome does not, the hypothesis is refuted and the product is solving the wrong problem.

## 2. Problem

**Who:** Adult children, siblings, friends, and neighbors of an older adult (typically 75+) who wants to age in place. The person who downloads the app is rarely a single "primary caregiver" — it's a *crew* of 3-12 people scattered across cities, with uneven availability and skills. None of them live with the loved one.

**How bad it is:**

- **Caregiver burden is widespread and severe.** 39% of US family caregivers report high emotional stress directly attributable to caregiving, and 45% report high physical strain. Nearly half experience at least one negative financial impact, and 1 in 5 say their health is fair or poor as a direct result of caregiving (AARP & National Alliance for Caregiving, *Caregiving in the US 2025*).
- **Aging in place is what older adults overwhelmingly want.** 75% of adults 50+ say they want to live in their current home for as long as possible, and 73% want to remain in their current community — yet 44% expect they will have to relocate, with cost and unmet support being the leading drivers (AARP, *2024 Home and Community Preferences Survey*, n=3,000+).
- **The market is large, growing fast, and aging into the problem.** 63 million Americans — roughly 1 in 4 adults — are now family caregivers, a 45% increase (~20 million more caregivers) over the past decade. The 85+ population is projected to triple by 2050, and adults 65+ will outnumber children under 18 by 2030 (AARP/NAC 2025; US Census projections). Today's caregiver is, on average, 51 years old; nearly a third are simultaneously caring for both children and an aging parent.

**Customer evidence:**
- `[NEED: paste 3-5 direct caregiver quotes from your user interviews — the rawer the better]`
- Common themes from interviews: `[NEED: 3 themes from your research, e.g., "the group text is unmanageable," "I don't know who's checking in this week," "Mom needs the gutters cleaned and nobody knows a good handyman"]`

**Current workarounds (proof the pain is real):**
- Group texts / WhatsApp threads that nobody can keep track of
- Shared Google Calendars manually maintained by one exhausted person
- Spreadsheets of meds, doctors, and contractors passed around as PDFs
- One sibling silently absorbing 80% of the coordination labor

**If we don't solve it:** Loved ones get moved to assisted living earlier than they want to, families fracture under uneven labor distribution, and the lead coordinator burns out (a documented health risk in itself).

## Personas

Three crew archetypes drive product decisions. Names are illustrative; quotes are synthesized from PRD themes and standard caregiving research patterns, **not** drawn from real interviews. Replace with verbatim quotes once `[NEED: paste 3-5 direct caregiver quotes]` (Section 2) is filled in.

### Persona 1 — Maya, the Lead Coordinator

*"I'm not the lead caregiver. I'm just the only one who hasn't quit."*

**Demographics.** Adult daughter, mid-40s. Lives in the same metro or 1–2 hours away. Married, two kids in middle/high school, full-time job. Eldest sibling.

**Day in the life.** It's 9:47pm on a Tuesday and Maya is texting her brother in Denver about whether Mom remembered to take her evening medication. He responds *"idk, ask Dad?"* — and Maya doesn't have the energy to explain that Dad's been gone for two years. She updates the shared Google Sheet she made eight months ago, the one only she touches. Tomorrow she has to call the gutter guy because the cousin who said he'd handle it never followed up. She has been the family operating system for her mother since 2024 and has started waking up at 4am with a clenched jaw.

**Jobs to be done.**

- When I'm coordinating five people across three time zones, I want one place where everyone can see what's needed and when, so I stop being the human router for every request.
- When I'm exhausted, I want the system to redistribute work without me having to ask, because asking is also work.
- When something goes wrong, I want it logged automatically, so I'm not the only one carrying the memory.

**Pains.**

- Decision fatigue from being the default decider for every micro-task.
- Resentment building toward siblings who "want to help but don't."
- Guilt that she should still be doing more, despite already doing most of it.
- Fear that something critical will fall through the cracks on a day she's depleted.
- The cognitive load of remembering who knows what.

**Gains / needs.**

- Visibility into the full picture (what's done, what's pending, who's slipping).
- The ability to step away for a weekend without things collapsing.
- Evidence the load is being shared — to reduce resentment, not just balance work.
- A diplomatic way to flag overload without seeming like she's complaining.

**Trigger moments.** A missed medication on a Sunday night. A sibling asking *"is there anything I can do?"* for the third time. The realization that she hasn't slept through the night in two months.

**Key product moment.** The first time the AI proposes a balanced weekly schedule and she sees her name on fewer than half the tasks for the first time in two years.

**What we'd build for Maya.** Load-balance dashboards. A "take a week off" mode that pauses her assignments and surfaces work to others. The overload-detection alert (no one wants to *be* Maya, but the alert validates her experience).

**What we'd cut for Maya.** Onboarding screens that demand the loved one's full medical profile up front (she'll abandon — already exhausted). Long setup before showing value. Group-celebration UI ("great job, team!") — feels patronizing when you're doing 80%.

### Persona 2 — Daniel, the Distant Sibling

*"I'm not the bad one. I'm just the far one. I think I am, anyway."*

**Demographics.** Adult son, late 30s to early 40s. Lives 2+ hours away or in a different time zone. Two young kids, demanding career. Often the second or third person invited to the crew. Sends money or gift cards when he doesn't know what else to do.

**Day in the life.** Daniel's group text with his sisters has 247 unread messages. He scrolls back through them on the train, gets to a message from yesterday about Mom's cardiology appointment, and realizes the appointment was *today*. He texts *"how did it go?"* and gets a thumbs-up from Maya 90 minutes later. He feels relief, then guilt about feeling relief. He sends Mom flowers. He has not spoken to his mother on the phone in eleven days, but he is paying for the lawn service. He thinks of himself as someone who wants to be more involved, and is privately not sure if that's true.

**Jobs to be done.**

- When I check in once a week, I want a 90-second summary of what actually happened and what's actually needed, so I'm caught up without scrolling 200 messages.
- When I have time on a Saturday, I want a specific async task assigned to me that I can finish from my couch in Brooklyn, so I'm contributing real labor instead of just sending money.
- When I show up for the holidays, I want to walk in already knowing what's changed, so I'm not the relative who has to be re-briefed.

**Pains.**

- Information overwhelm from the group chat — gives up trying to keep up.
- Status anxiety about being judged by the lead coordinator (probably his sister).
- Guilt about geographic distance he can't change in the short term.
- Awkwardness about asking what's needed (feels like adding to Maya's plate).
- Fear of the moment he realizes how much he missed.

**Gains / needs.**

- Personalized weekly summary that surfaces only what's relevant to him.
- A clear, narrow task he can claim and execute remotely (calling insurance, renewing a prescription, ordering supplies, vendor research).
- Visibility for the contributions he does make — so he doesn't feel invisible.
- An easy on-ramp on a Sunday morning: low effort, high signal.

**Trigger moments.** A Thanksgiving visit where he realized how much had changed without him knowing. His sister snapping at him in the group chat about something he didn't realize he should have done. His own kid asking why Grandma sounded confused on FaceTime.

**Key product moment.** The "What you missed this week" summary that's actually 90 seconds — followed by one specific task with a green "Claim" button next to it.

**What we'd build for Daniel.** Async-first task patterns (calls, paperwork, vendor management, research) that work remotely. Personalized digest, not the full activity feed. Recognition surface — small celebrations when he completes a remote task. A monthly calendar view for at-a-glance phone use.

**What we'd cut for Daniel.** Notifications for in-person events he can't attend. Long onboarding flows. Anything that requires real-time reply during EST work hours.

### Persona 3 — Patricia, the Specialist Friend

*"I have so much to give and I keep waiting for someone to ask."*

**Demographics.** Friend or extended family — the retired neighbor, the RN aunt, the handy cousin, the godparent. 50s–70s, often retired or partly retired. Has a specific high-value skill (medical knowledge, home repair, local presence, transportation). May or may not be in the original group text.

**Day in the life.** Patricia has lived three doors down from Bea since 1998. They had coffee every Wednesday for eleven years until Bea stopped being able to walk over. Patricia is a retired nurse and notices things — the slight new tremor, the meds left out on the counter — but doesn't know what to do with what she notices. She's not family. She's not sure if anyone wants her opinion. When Bea fell last March, Patricia was the first one there and held her hand for 40 minutes waiting for the ambulance. After that she didn't hear anything for two weeks, until Bea's daughter Maya texted to thank her. She would do anything they asked. Nobody asks.

**Jobs to be done.**

- When I see something concerning, I want a clear way to flag it to the family without seeming intrusive.
- When the family needs a skill I have, I want them to know to ask me, so I'm not waiting around hoping I'll be useful.
- When I help, I want my contribution recognized as part of the team, not as a favor I'm doing.

**Pains.**

- Social anxiety about overstepping — *"is it my place?"*
- Being treated as a stranger or afterthought, not part of the crew.
- Being asked to do things outside her expertise (driving in winter when she's nervous on icy roads).
- Watching things go wrong and not feeling she has standing to intervene.
- The loneliness of caring about someone who isn't formally hers to care about.

**Gains / needs.**

- Defined narrow involvement that respects her skill.
- A permission structure — a clear *"you're invited to help with X"* message.
- Recognition as a member of the crew, not an outsider.
- A way to flag concerns without intruding on a private family matter.

**Trigger moments.** A specific incident she witnessed (a fall, a confused conversation, a missed med) that the family never heard about. Hearing through a third party that something the family is struggling with is something she could solve in 20 minutes. Being explicitly invited to the crew for the first time.

**Key product moment.** Receiving a personalized invitation that says *"Bea's family invited you because you're closest and you used to be a nurse. Here's what they think you'd be best at."* And it's right.

**What we'd build for Patricia.** Skill-tagged invitations matching her to qualified tasks. A lightweight "concern flag" UX — non-medical, just a heads-up. A guest-vs-member distinction that respects her position without second-classing her. Per-category opt-in/opt-out (*medical: yes; winter driving: no*).

**What we'd cut for Patricia.** Mandatory profile fields about her relationship that make "other" feel like second-class. Generic group celebrations that don't acknowledge her unique contribution. Pressure to attend non-essential events.

### Cross-persona design principles

Three principles fall out of the personas above:

1. **Default to async.** Maya is depleted, Daniel is remote, Patricia is tentative. None of them benefit from real-time pressure. Notifications, summaries, and task claims should work on weekly cadence by default; real-time only for genuine urgency.
2. **Make labor visible.** Every persona needs the system to *show* contribution — Maya so the load is provably distributed, Daniel so his remote work isn't invisible, Patricia so she's recognized as crew. This is a first-class design constraint, not a "delight" feature.
3. **Permission, not pressure.** The product should never make someone feel guilty for declining. Maya is already drowning in obligation; Daniel is already drowning in guilt; Patricia is already worried about overstepping. Decline UX matters as much as Accept UX.

## 3. Strategic Fit

**Why this, why now:**
- Aging baby boomers — the largest generational cohort — are entering the 75+ window over the next decade.
- Adult children are more geographically dispersed than any prior generation.
- AI is finally good enough to do the coordination work that requires *judgment* (who to assign, what's urgent, summarizing chaos) — not just calendaring.

**Competitive context:**
- **Lotsa Helping Hands / CaringBridge:** Calendar-based meal trains. Built for short-term crises (cancer, surgery), not multi-year aging-in-place. No AI, no service hiring.
- **Papa:** Pairs elders with paid companions. Solves loneliness for the elder, not coordination across the family.
- **Carely:** Family-coordination dashboard — shared calendar, messaging, visit logging, manual task assignment. Functionally a polished group-calendar-plus-chat layer for the family. No AI coordination (assignment, rebalancing, and summarization are all manual), and no integrated services hiring. Free iPhone app today.
- **ianacare:** The closest structural competitor. Explicitly designed to rally a "care team" of friends, family, neighbors, and coworkers around a care recipient via a request-driven team calendar (meals, rides, check-ins, respite). MIT-backed, in market since 2018, already uses statistical matching to route help requests, with new AI features announced for launch in 2025. Two structural gaps vs. our approach: (1) the model is **request-driven** — the caregiver asks, the team responds — rather than continuous coordination of recurring needs, and (2) it does not integrate paid services hiring with elder context. **This is the competitor most likely to verticalize into our space first; monitor closely.**
- **TaskRabbit / Thumbtack:** Solve home services hiring but with zero context about the loved one.

**Why our approach wins:** Crew-peer model (no single "lead caregiver" required) + AI that does the actual coordination work + integrated services hiring with elder-context. No competitor combines all three.

## Defensibility

The defensibility argument starts by being honest about what is *not* the moat. The AI itself is not — OpenAI, Anthropic, and Google build better foundation models than we ever will, and any defense built on model quality alone collapses the moment a competitor wires up the same APIs. The moat is everything around the AI that compounds with usage and is hard to replicate from outside. Four pillars, ordered from fastest- to slowest-to-build.

### 1. Multi-party coordination graph

BuildtheCrew is N-user by design — the unit of value is the crew, not the individual. The graph of who is connected to whom, with what skills, geographies, availability, and history together, exists only inside the product. A general-purpose assistant cannot ingest a brother's calendar, a sister's task history, and a neighbor's medical background in any coordinated way; the user would have to re-explain everything in every session. Once a crew has formed inside BuildtheCrew, that graph is structurally outside the reach of single-user tools.

### 2. Longitudinal context

Every crew accumulates months of compounding context: that Bea's cardiologist is Dr. Chen, that the gutter contractor from October was reliable, that Patricia is good for medical concerns but won't drive in winter, that Daniel hasn't seen Mom since Thanksgiving. ChatGPT starts from zero every conversation; memory features help but are lossy, single-user, and not built to be a family's system of record. Over time this context becomes a body of operational knowledge that a general-purpose tool cannot match without the user re-telling it.

### 3. Services flywheel

Every booking feeds a local-services graph that improves as more crews join: which lawn provider in zip 44109 actually showed up on time, which plumber overcharged, which snow-removal contractor handles 82-year-olds well. ChatGPT can recommend providers in a vacuum; it cannot tell us which one was reliable for an elder in this specific neighborhood. Thumbtack and Angi have the services data but no elder context. The combination is the moat.

### 4. Trust

Families will not casually paste their parent's prescription list, doctor names, home access details, and crew dynamics into a general-purpose assistant — and the privacy posture of those tools makes that hesitation reasonable. BuildtheCrew's right to win here is to be a brand families trust with the sensitive specifics of their parents' lives, the way Apple Health is trusted with biometrics. That trust is not a feature; it is a posture, a privacy story, and consistent year-over-year behavior. It is the slowest of these moats to build, and the most durable once built.

### What we do not have yet

None of the above is a moat on day one. On day one we have zero crews, zero longitudinal context, zero services data, and zero brand. The moat is a bet that we can build the multi-party coordination graph in elder care faster than (a) a general-purpose assistant verticalizes into family caregiving, or (b) the existing caregiving incumbents (Lotsa Helping Hands, Carely, ianacare) ship a competent agentic product. Until the moats compound, our only weapons are speed and category focus — owning the words "elder-care crew" before anyone else does. This is a real strategic risk and should be revisited at every stage gate.

### What we watch

- **Crew durability past day 21** — proxy for the coordination graph forming. Crews that get past three weeks rarely churn.
- **Services re-booking rate** — proxy for the services flywheel taking hold. Once a crew rebooks the same provider, the local graph has captured value.
- **Trust NPS** — specifically on the question "would you trust BuildtheCrew with information about your parent that you would not paste into ChatGPT?" Proxy for the trust posture compounding.

## 4. Solution

A mobile-first app where a crew of family + friends collaboratively cares for a loved one aging in place. AI does three core jobs.

### Why agentic, not rule-based

Caregiving coordination is fundamentally a judgment problem, not a rules problem. Almost every decision the system has to make weighs inputs that don't have crisp values — *who is the right person for this task* depends on availability, geography, skill, recent load, the family dynamic, and what happened last week. A rule engine would force us to enumerate all of that in advance, which is impossible: edge cases only surface in production, and they evolve as the loved one's needs change. The three core capabilities below are each clear examples of this. The Scheduler has to weigh seven dimensions and rebalance when someone cancels at 3pm. The Summarizer has to pull a single sentence about a fall to the top of a feed it has never seen before. The Services assistant has to remember preferences and ask follow-up questions like *"same provider as last time?"*. None of these are rule-shaped problems.

The honest counter-argument is that agentic systems hallucinate, are harder to debug, and create accountability problems in a sensitive domain like elder care. That is exactly why this PRD draws the line where it does: **the judgment lives in the agent (assignment, summarization, recommendation), but the safety-critical guardrails are deterministic rules** — never book over the approval threshold, never authorize home access, never make a medical decision, escalate distress signals to humans within 60 seconds. The agent is permitted to be wrong on the soft cases. It is not permitted to be wrong on the hard ones.

The strategic argument is that this is the first moment an agentic approach is actually viable for this product category. The existing tools — Lotsa Helping Hands, Carely, ianacare — aren't bad products; they are products built before the technology was ready. They settled for shared calendars and chat threads because LLMs couldn't reliably summarize 200 messages or judge vendor fit against context. Building rule-based today would mean building a competitor of those products, not a successor to them.

What this means for the rest of this section: the behavior spec below is not a list of programmed responses. It is the agent's *policy surface* — illustrative examples of how it should reason, not exhaustive coverage of inputs. The Rejection / safety criteria, by contrast, are hard rules the agent must never override.

### Core Capabilities

**(a) AI Care Coordinator / Scheduler**
Crew members add availability, skills, and location. Loved one's needs are entered once (meds, meals, rides, check-ins, recurring tasks). AI proposes a weekly schedule that fairly distributes load, accounts for who lives closest, and re-balances when someone's plans change. Crew members claim, swap, or decline tasks — AI re-assigns gaps.

**(b) AI Crew Comms Summarizer**
The crew chat, doctor visit notes, and event log get summarized into a digestible "What you missed" feed for each crew member based on what's relevant to *them*. Catches up the cousin who checks in on Sundays without forcing them to scroll 200 messages.

**(c) AI Services Hiring Assistant**
When a home task comes up (lawn, gutters, broken dishwasher, snow removal), AI helps the crew find, vet, and book a local service provider. Knows the loved one's home, preferences, and budget. Tracks completion. Surfaces recurring needs proactively ("It's been 3 weeks since the lawn was mowed").

### Primary User Flow

```
1. Crew founder downloads app, creates loved one's profile (name, home, key needs)
2. Invites crew members via SMS/email — each sets availability + skills
3. AI generates Week 1 schedule → crew reviews, claims, edits
4. Crew chats inside app about loved one; AI summarizes per-person daily
5. Home task comes up (e.g., "fridge is making a noise")
   → AI suggests local repair pros, crew approves, AI books + tracks
6. Loved one's status visible to all (last check-in, upcoming visits, open tasks)
```

### Key States
- **Healthy crew:** all needs covered, balanced load, low alert volume
- **Gap detected:** unfilled task within 24h → AI nudges available crew members
- **Overload detected:** one crew member doing >40% of tasks → AI flags + suggests rebalance
- **Loved-one signal:** missed check-in, missed meds → escalation to nearest crew member

### AI Behavior Spec (15+ examples)

**Coordinator / Scheduler**

| # | Input | Expected Output |
|---|-------|-----------------|
| 1 | "Sarah cancels Tuesday 3pm pharmacy run" | Reassigns to next-closest available crew member; if none, posts to crew with 24h deadline |
| 2 | New crew member added with "weekends only, lives 2hrs away" | Assigns Saturday/Sunday tasks only; avoids weekday short-notice |
| 3 | Loved one's doctor adds new med "twice daily with food" | Creates recurring task; assigns to whoever already does meals; flags conflict if someone else owns meds |
| 4 | Crew member marks task "complete" 4 hours late | Logs delay silently; if pattern repeats 3x, surfaces gently to that member, not whole crew |
| 5 | Two tasks scheduled for same crew member 30 min apart, 45 min driving distance | Flags conflict; proposes swap with available member |
| 6 | Crew member with "no medical tasks" preference assigned med pickup | Rejects assignment; reassigns and explains why |
| 7 | Holiday week — 6 of 8 crew members marked unavailable | Surfaces crisis; suggests temporarily hiring a paid visit; does NOT silently overload remaining 2 |

**Crew Comms Summarizer**

| # | Input | Expected Output |
|---|-------|-----------------|
| 8 | 47 chat messages over 3 days, mostly about Mom's cardiology appt | "Mom saw Dr. Chen Tuesday. New BP med, follow-up in 6 weeks. Sarah has the prescription. No major concerns." |
| 9 | Single message: "Dad fell but he's okay" buried in chat about lawn care | Pulls fall to top of summary as priority; lawn care below |
| 10 | Two crew members debating whether to hire a cleaner | Summarizes positions; does NOT take a side; flags as "open decision" |
| 11 | Crew member asks AI "what did I miss this week?" | Personalized summary based on tasks they own + their relationship (e.g., medical updates for the sibling who's an RN) |
| 12 | Doctor visit note uploaded as photo | OCRs, summarizes, tags meds/follow-ups, asks crew to confirm before adding to schedule |
| 13 | Message contains medical jargon ("eGFR dropped to 45") | Summarizes in plain language with optional "what this means" expansion |

**Services Hiring**

| # | Input | Expected Output |
|---|-------|-----------------|
| 14 | "Lawn needs mowing, Dad's in Cleveland 44109" | 3 vetted providers with ratings, prices, availability; remembers preferred one for next time |
| 15 | "Gutters" booking after a previous lawn-care provider did good work | Asks if same provider does gutters; if yes, prefers them |
| 16 | Crew approves $400 dishwasher repair without budget set | Books it; logs cost; suggests setting a monthly budget so future approvals are faster |
| 17 | Loved one calls plumber directly, charges $800 | Logs the cost, doesn't double-book; flags to crew so they can follow up |
| 18 | Provider asks for keys / access to home | Routes to nearest crew member; never authorizes home access without human approval |
| 19 | Repeat seasonal task (snow removal) | Proactively suggests rebooking 1 week before first forecast snow |
| 20 | User asks AI to hire a "home health aide" | Rejects — out of scope for V1 (medical). Suggests crew add this manually or refer to licensed agency |

**Rejection / safety criteria (must hold across all capabilities):**
- Never makes medical decisions or interprets medical advice
- Never authorizes home entry without explicit crew approval
- Never books a paid service over `[NEED: budget threshold, e.g., $250]` without human approval
- Never shares loved one's location, health data, or schedule outside the crew
- If loved one is in distress signal (missed check-in, fall flag), escalates to humans within 60 seconds — does not attempt to handle alone

## 5. Non-Goals

- We are **NOT** providing licensed medical care, telehealth, or home health aide services in V1. We coordinate the humans who do.
- We are **NOT** building a companion chatbot for the loved one in V1. The elder is in the background; the crew is the user. (V2 candidate.)
- We are **NOT** integrating with hospital EHR systems in V1.
- We are **NOT** replacing emergency services. Fall detection / 911 is out of scope — we recommend separate medical alert devices.
- We are **NOT** charging the loved one. Pricing targets the crew (likely the lead coordinator's credit card).
- We are **NOT** building a marketplace of paid caregivers (that's Papa / Honor's space). We coordinate unpaid family + paid services for *home tasks*.

## 6. Success Metrics

| Metric | Type | Baseline | Target | Timeframe |
|--------|------|----------|--------|-----------|
| Active crews at 90 days post-signup | Primary | n/a (new product) | `[NEED: target]` | 90 days |
| % of loved ones still aging-in-place at 12 months | Primary | `[NEED: industry baseline from research]` | `[NEED: target lift]` | 12 months |
| Crew load balance (Gini coefficient of task distribution) | Secondary | n/a | <0.4 (reasonably even) | 90 days |
| Self-reported lead caregiver burnout score | Secondary | `[NEED: baseline from intake survey]` | -25% | 6 months |
| Services bookings per crew per month | Secondary | n/a | `[NEED: target]` | 90 days |

**Guardrails (must NOT get worse):**
- AI assignment rejection rate (crew member declines AI suggestion) <20%
- Summary accuracy (crew rates summary "got the important stuff" thumbs-up) >85%
- Zero incidents of unauthorized home access via services booking
- Zero incidents of AI making a medical decision or recommendation

## 7. Rollout Plan

- **Phase 1 — Closed beta (10 crews):** Hand-recruited from `[NEED: source — your interview pool?]`. Heavy support, weekly check-ins. Goal: prove crews stay active past day 30.
- **Phase 2 — Limited launch (100 crews):** Single geography for services hiring (suggest Cleveland or wherever your interview base is densest). Validate the AI coordinator quality.
- **Phase 3 — Public launch:** Open signups, expand services geography. Marketing focused on the "I'm the one doing everything" sibling.

**Go/no-go criteria to advance phases:**
- Phase 1 → 2: ≥7 of 10 crews still active at day 60, summary thumbs-up >75%
- Phase 2 → 3: Active crews at 90 days >`[NEED: target]`, zero safety guardrail violations

**Rollback plan:** AI features can be disabled per-crew via feature flag; app falls back to manual scheduling + chat. Services hiring can be paused without breaking the rest of the app.

## 8. Open Questions

- `[NEED: pricing model — freemium? per-crew subscription? services markup? — owner: Brent, deadline: TBD]`
- `[NEED: how does the loved one consent to being coordinated? Privacy + dignity question — owner: Brent + legal review]`
- `[NEED: what's the minimum viable crew size? Does this work for a crew of 2?]`
- `[NEED: how do we handle a crew member who goes rogue / abusive — moderation policy]`
- `[NEED: HIPAA posture — we're not a covered entity, but med info is sensitive. Privacy counsel review needed.]`
- `[NEED: services provider vetting — own marketplace, or partner with Thumbtack/Angi API?]`

---

## Stage 4 Checklist

- [x] Edge cases identified (in AI behavior spec)
- [x] Rollout plan determined (phased)
- [ ] Cross-functional requirements specified — **gap:** legal/privacy review, services partnerships, payment processing not yet detailed
- [ ] Tracking and analytics events defined — **gap:** specific event taxonomy missing
- [x] Risks and mitigations documented (guardrails + rejection criteria)

---

**Gaps to fill before this PRD is review-ready:**
1. Paste 3-5 caregiver quotes from your interviews (Section 2)
2. Paste market stats — caregiver burnout %, aging-in-place demand %, market size (Section 2)
3. Paste your competitor list with notes (Section 3)
4. Set targets for the metrics table (Section 6)
5. Resolve the 6 open questions in Section 8
