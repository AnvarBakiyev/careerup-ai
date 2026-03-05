# CareerUp AI - Product Backlog

## Sprint Overview

| Sprint | Focus | Duration | Points |
|--------|-------|----------|--------|
| S1 | Foundation + Core MVP | Week 1-2 | 26 |
| S2 | Intelligence Layer | Week 3-4 | 26 |
| S3 | Tests & Polish | Week 5-6 | 21 |
| S4 | Growth & Scale | Week 7-8 | 20 |

---

## SPRINT 1: Foundation (Week 1-2)
**Goal:** Working MVP with Interview Coach + Resume Optimizer

### [P1-ARCH] Project Architecture & Tech Stack Setup (5 pts)
**Priority:** Urgent

#### Scope
- Initialize monorepo structure
- Setup FastAPI backend skeleton
- Setup React + TypeScript frontend
- Configure TailwindCSS + shadcn/ui
- Setup PostgreSQL + pgvector
- Configure CI/CD pipeline (GitHub Actions)

#### Acceptance Criteria
- [ ] Backend runs on localhost:8000
- [ ] Frontend runs on localhost:3000
- [ ] Database migrations work
- [ ] GitHub Actions configured
- [ ] Docker Compose for local dev

---

### [P1-CORE] Interview Coach Expert - MVP (8 pts)
**Priority:** Urgent

#### Scope
Create Dronor expert for mock interviews:
- Generate interview questions based on role/company
- Evaluate user answers (text input first)
- Provide data-driven feedback (not motivational)
- Track improvement metrics

#### Key Features
- Question bank by role (PM, SWE, Design, Data)
- STAR method evaluation
- Concrete improvement suggestions
- Score: 'You outperform X% of candidates'

#### Acceptance Criteria
- [ ] Expert runs via Dronor API
- [ ] Generates 5+ relevant questions per role
- [ ] Provides actionable feedback (not generic)
- [ ] Returns percentile score
- [ ] Tracks user improvement over sessions

---

### [P1-CORE] Resume Optimizer Expert - MVP (8 pts)
**Priority:** Urgent

#### Scope
Create Dronor expert for resume optimization:
- Parse PDF/DOCX resume
- ATS compatibility check
- Keyword optimization for target role
- Quantification suggestions (add metrics)
- Before/after score comparison

#### Key Features
- ATS score (0-100) with breakdown
- Missing keywords detection
- 'Add 3 numbers = +15% score' suggestions
- Industry-specific improvements

#### Acceptance Criteria
- [ ] Parses resume correctly (PDF + DOCX)
- [ ] ATS score is accurate vs real ATS systems
- [ ] Suggestions are actionable and specific
- [ ] Returns percentile vs market
- [ ] Shows before/after comparison

---

### [P1-UI] MVP Dashboard - Core Layout (5 pts)
**Priority:** Urgent

#### Scope
Build main dashboard interface:
- User profile header with progress
- Module cards (Interview, Resume, LinkedIn, etc)
- Progress visualization (not gamified)
- Today's priorities section

#### Design Principles
- Data-first (numbers, not motivational quotes)
- Clean, professional aesthetic
- Information density over decoration
- No 'success theater'

#### Acceptance Criteria
- [ ] Responsive design (mobile + desktop)
- [ ] All module cards clickable
- [ ] Progress bars show real data
- [ ] Today's priorities based on impact

---

## SPRINT 2: Intelligence (Week 3-4)
**Goal:** Smart recommendations + Roadmaps

### [P2-INTEL] Insider Tips Database & Collector (8 pts)
**Priority:** High

#### Scope
Build system for real career intelligence:
- Curate tips from Reddit/Blind/Twitter
- Categorize by role/company/topic
- Vector search for relevant tips
- Quality scoring (upvotes, engagement)

#### Initial Categories
- Application timing tips
- Interview hacks by company (FAANG, etc)
- Salary negotiation patterns
- Networking effectiveness data
- Resume/LinkedIn patterns that work

#### Sources
- r/cscareerquestions (top posts)
- Blind app (verified employees)
- Lenny's Newsletter
- Top career Twitter accounts

#### Acceptance Criteria
- [ ] 500+ quality tips in DB
- [ ] Semantic search works accurately
- [ ] Tips are non-obvious (not 'prepare for interviews')
- [ ] Quality scores reflect actual usefulness

---

### [P2-INTEL] Personalized Roadmap Generator (8 pts)
**Priority:** High

#### Scope
Generate concrete career roadmaps:
- Input: current state + target role/company
- Output: week-by-week action plan
- Include: books, courses, networking steps
- ROI-based prioritization

#### Key Differentiators
- Concrete timelines (not 'learn more')
- Insider tips integrated
- Competition data ('300 applicants avg')
- Success probability estimate

#### Example Output
```
Goal: Senior PM @ Stripe in 6 months

Month 1-2: Foundation
- Read "Decode and Conquer" (skip ch 7-8)
- Complete 3 Product School cases
- Rewrite resume in XYZ format

Month 3-4: Practice
- 20 mock interviews (minimum)
- Find study buddy on Blind
- Do 5 case studies on Exponent

Month 5-6: Applications
- Apply Tuesday-Wednesday 10-11am
- Target <50 applicants listings
- 3 referral conversations/week
```

#### Acceptance Criteria
- [ ] Roadmap is week-specific
- [ ] Resources are curated (not generic lists)
- [ ] Progress tracking works
- [ ] Probability estimates are realistic

---

### [P2-CORE] LinkedIn Profile Optimizer (5 pts)
**Priority:** High

#### Scope
Optimize LinkedIn profiles:
- Headline optimization
- Summary rewrite
- Skills prioritization
- Keyword density for recruiter search

#### Key Metrics
- Search appearance score
- Recruiter attraction score
- Comparison to top profiles in role

#### Acceptance Criteria
- [ ] Parses LinkedIn profile (URL or text)
- [ ] Provides specific rewrites
- [ ] Shows before/after metrics

---

### [P2-CORE] Cover Letter Generator (5 pts)
**Priority:** High

#### Scope
Generate personalized cover letters:
- Input: job description + resume
- Match keywords from JD
- Highlight relevant experience
- Company-specific customization

#### Quality Standards
- Not generic ('I am excited to apply')
- Specific achievements mentioned
- Company research integrated
- Tone matching (startup vs enterprise)

#### Acceptance Criteria
- [ ] Letter matches JD keywords
- [ ] Sounds human (not AI-generated)
- [ ] Takes <30 seconds to generate

---

## SPRINT 3: Tests & Polish (Week 5-6)
**Goal:** Personality tests + shareable results

### [P3-TEST] Personality Test: Interview Perception (5 pts)
**Priority:** Medium

#### Scope
Create practical personality assessment:
- 10-15 scenario-based questions
- Result: how interviewers perceive you
- Actionable adjustments

#### Output Format
```
Result: Analytical-Assertive

Strength: Your answers are structured and data-driven
Weakness: May come across as cold or distant

Fix: Add 1 personal story to each behavioral answer
(but keep it under 30 seconds)

Example:
❌ "We increased metrics by 40% through A/B testing..."
✅ "I actually had to convince my skeptical PM first — 
    she didn't believe in the approach. After showing 
    the data... we increased metrics by 40%"
```

#### Acceptance Criteria
- [ ] Test takes <5 minutes
- [ ] Results are validated against real interview outcomes
- [ ] Suggestions are concrete and actionable
- [ ] Result card is share-worthy

---

### [P3-TEST] Personality Test: Decision-Making Style (5 pts)
**Priority:** Medium

#### Scope
Assess decision-making patterns:
- Data-driven vs intuitive spectrum
- Risk tolerance level
- Speed vs thoroughness preference

#### Interview Application
- How to frame decisions in STAR format
- Red flags to avoid based on style
- Strengths to emphasize

#### Acceptance Criteria
- [ ] Results map to interview behavior
- [ ] Suggestions are role-specific
- [ ] Shareable result card

---

### [P3-TEST] Skill Assessment Framework (8 pts)
**Priority:** Medium

#### Scope
Practical skill testing:
- Role-specific questions (not trivia)
- Timed assessments
- Comparison to market

#### Initial Roles
- Product Manager
- Software Engineer
- Data Scientist
- Designer

#### Output
- Skill radar chart
- Weak areas identified
- Specific improvement resources

#### Acceptance Criteria
- [ ] Questions are practical (not textbook)
- [ ] Scoring is calibrated to market data
- [ ] Resource recommendations are relevant

---

### [P3-UI] Shareable Result Cards (3 pts)
**Priority:** Medium

#### Scope
Design beautiful shareable cards:
- Test results
- Resume score improvements
- Roadmap progress milestones

#### Requirements
- Instagram/Twitter optimized sizes
- Professional design (not gamified)
- Branding included
- One-click share

#### Acceptance Criteria
- [ ] Cards look premium
- [ ] Social preview works on all platforms
- [ ] Download as image option

---

## SPRINT 4: Growth (Week 7-8)
**Goal:** Viral mechanics + polish

### [P4-GROWTH] Social Sharing & Viral Mechanics (5 pts)
**Priority:** Low

#### Scope
Build viral growth features:
- Share results to Twitter/LinkedIn
- Referral system
- Comparison with friends

#### Viral Loops
- 'I improved my resume by 47%' posts
- 'My career archetype is...' shares
- Challenge friends to skill test

#### Acceptance Criteria
- [ ] One-click sharing works
- [ ] Posts look native to platform
- [ ] Referral tracking works

---

### [P4-GROWTH] Analytics Dashboard (5 pts)
**Priority:** Low

#### Scope
Track user progress over time:
- Interview score progression
- Resume improvements
- Roadmap completion
- Application success rate

#### Visualizations
- Progress charts (clean, minimal)
- Milestone achievements
- Percentile changes

#### Acceptance Criteria
- [ ] Data is accurate
- [ ] Charts are clear and informative
- [ ] Insights are actionable

---

### [P4-POLISH] Mobile Responsive Design (5 pts)
**Priority:** Low

#### Scope
Ensure perfect mobile experience:
- All features work on mobile
- Touch-optimized interactions
- Performance optimization

#### Priority Screens
1. Dashboard
2. Interview practice
3. Personality tests
4. Roadmap view

#### Acceptance Criteria
- [ ] Lighthouse score >90
- [ ] All features accessible on mobile
- [ ] No horizontal scroll issues

---

## Backlog (Future)

- Voice interview practice
- Video interview analysis
- Company-specific prep packs
- Salary negotiation coach
- Networking assistant
- Job application tracker
- Interview calendar integration
- Team/enterprise features
