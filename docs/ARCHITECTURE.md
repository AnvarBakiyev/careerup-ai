# CareerUp AI Architecture

## Overview

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

## Tech Stack

### Frontend
- **React 18** + TypeScript
- **TailwindCSS** + shadcn/ui
- **Zustand** for state
- **React Query** for data fetching

### Backend
- **FastAPI** (Python 3.11+)
- **SQLAlchemy** + Alembic
- **Pydantic** for validation
- **JWT** authentication

### AI Layer
- **Dronor Experts** (hosted)
- **OpenAI GPT-4** (via API)
- **Claude** (via API)

### Data
- **PostgreSQL** + pgvector
- **Redis** for caching
- **S3** for file storage

## Core Modules

### 1. Interview Coach
- Question generation by role/company
- Answer evaluation (STAR method)
- Percentile scoring
- Improvement tracking

### 2. Resume Optimizer
- PDF/DOCX parsing
- ATS compatibility scoring
- Keyword optimization
- Before/after comparison

### 3. LinkedIn Booster
- Profile parsing
- Headline optimization
- Skills prioritization
- Recruiter search optimization

### 4. Cover Letter Generator
- JD keyword matching
- Company customization
- Tone adaptation

### 5. Skill Assessment
- Role-specific tests
- Market comparison
- Improvement resources

### 6. Personality Tests
- Interview Perception
- Decision-Making Style
- Career Archetype

### 7. Roadmap Generator
- Week-by-week planning
- Curated resources
- ROI prioritization
- Progress tracking

### 8. Insider Tips
- Reddit/Blind/Twitter curation
- Vector search
- Quality scoring
