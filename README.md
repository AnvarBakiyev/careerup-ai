# CareerUp AI

> Your insider friend who already works there.

AI-powered career development platform that gives you **real data**, not motivational quotes.

## 🎯 Philosophy

Not "believe in yourself" — but **"you're outperforming 78% of candidates"**.

Not generic advice — but **insider tips from Reddit/Blind/Twitter** level intelligence.

## ✨ Features

### Core Modules
- **🎤 Interview Coach** — Mock interviews with data-driven feedback
- **📄 Resume Optimizer** — ATS-ready optimization with keyword analysis
- **💼 LinkedIn Booster** — Profile optimization with recruiter insights
- **✉️ Cover Letter Generator** — Personalized, company-specific letters
- **🧠 Skill Assessment** — Practical tests with honest feedback

### Intelligence Layer
- **📊 Data-Driven Metrics** — "You outperform 78% of candidates"
- **🗺️ Personalized Roadmaps** — Concrete steps, not abstract goals
- **💡 Insider Tips** — Real patterns that actually work
- **📚 Curated Resources** — Only what's worth your time

### Personality Tests (Practical, Not Buzzfeed)
- **Interview Perception** — How interviewers see you
- **Decision-Making Style** — With actionable interview tips
- **Career Archetype** — Matched to real job roles

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    FRONTEND (React)                     │
│  Dashboard │ Interview │ Resume │ Tests │ Roadmap      │
└─────────────────────────────────────────────────────────┘
                           │
┌─────────────────────────────────────────────────────────┐
│                    BACKEND (FastAPI)                    │
│  Auth │ User Progress │ Analytics │ AI Orchestration   │
└─────────────────────────────────────────────────────────┘
                           │
┌─────────────────────────────────────────────────────────┐
│                  DRONOR EXPERTS                         │
│  interview_coach │ resume_optimizer │ linkedin_boost   │
│  cover_letter_gen │ skill_assessor │ roadmap_builder   │
│  insider_tips_collector │ personality_analyzer         │
└─────────────────────────────────────────────────────────┘
                           │
┌─────────────────────────────────────────────────────────┐
│                    DATA LAYER                           │
│  PostgreSQL │ Redis Cache │ Vector DB (tips/patterns)  │
└─────────────────────────────────────────────────────────┘
```

## 📅 Roadmap

### Phase 1: Foundation (Week 1-2)
- [ ] Project setup & architecture
- [ ] Core Interview Coach expert
- [ ] Basic Resume Optimizer
- [ ] MVP Dashboard

### Phase 2: Intelligence (Week 3-4)
- [ ] Data-driven feedback system
- [ ] Insider tips database
- [ ] Personalized roadmaps
- [ ] LinkedIn Optimizer

### Phase 3: Personality & Polish (Week 5-6)
- [ ] Personality tests (3 types)
- [ ] Cover Letter Generator
- [ ] Skill Assessments
- [ ] Beautiful shareable cards

### Phase 4: Growth (Week 7-8)
- [ ] Social sharing features
- [ ] Community features
- [ ] Mobile-responsive design
- [ ] Analytics dashboard

## 🛠️ Tech Stack

- **Frontend:** React + TypeScript + TailwindCSS
- **Backend:** FastAPI + Python
- **AI Layer:** Dronor Experts + OpenAI/Claude
- **Database:** PostgreSQL + pgvector
- **Cache:** Redis
- **Deploy:** Railway / Vercel

## 📊 Success Metrics

- **Target:** 50K+ Twitter impressions on launch
- **Users:** 10K+ in first month
- **Engagement:** 4+ sessions per user
- **NPS:** 60+

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/AnvarBakiyev/careerup-ai.git

# Install dependencies
cd careerup-ai
pip install -r requirements.txt
npm install

# Start development
npm run dev
```

## 📝 License

MIT

---

Built with ❤️ and real insider knowledge.