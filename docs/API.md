# CareerUp AI API Documentation

## Base URL
```
http://localhost:8000/api
```

## Endpoints

### Interview Coach

#### POST /api/interview/practice
Generate interview questions or evaluate answers.

**Request Body:**
```json
{
  "role": "product_manager",
  "company_type": "faang",
  "question_type": "behavioral",
  "mode": "generate",
  "user_answer": null,
  "question_index": 0
}
```

**Response (generate mode):**
```json
{
  "status": "success",
  "question": "Tell me about a time...",
  "tip": "FAANG PMs love metrics...",
  "question_index": 0,
  "total_questions": 5
}
```

**Response (evaluate mode):**
```json
{
  "status": "success",
  "evaluation": {
    "overall_score": 85,
    "percentile": 75,
    "criteria_scores": {...},
    "strengths": [...],
    "weaknesses": [...],
    "improved_version": "...",
    "quick_fixes": [...]
  },
  "summary": "You outperform 75% of candidates"
}
```

---

### Resume Optimizer

#### POST /api/resume/optimize
Analyze and optimize resume for ATS and recruiter appeal.

**Request Body:**
```json
{
  "resume_text": "Full resume text...",
  "target_role": "Senior Product Manager",
  "target_company": "Google"
}
```

---

### LinkedIn Optimizer

#### POST /api/linkedin/optimize
Optimize LinkedIn profile for recruiter search.

**Request Body:**
```json
{
  "profile_text": "LinkedIn profile text...",
  "target_role": "Senior PM",
  "target_companies": "Google, Meta, Stripe"
}
```

---

### Cover Letter Generator

#### POST /api/cover-letter/generate
Generate personalized cover letter.

**Request Body:**
```json
{
  "job_description": "JD text...",
  "resume_text": "Resume text...",
  "company_name": "Stripe",
  "tone": "professional"
}
```

---

### Personality Tests

#### POST /api/personality/test
Get test questions or analyze personality.

**Request Body (get questions):**
```json
{
  "test_type": "interview_perception",
  "target_role": "Product Manager"
}
```

**Request Body (analyze):**
```json
{
  "test_type": "interview_perception",
  "answers_json": "{\"1\": \"A\", \"2\": \"B\", ...}",
  "target_role": "Product Manager"
}
```

---

### Skill Assessment

#### POST /api/skills/assess
Role-specific skill assessment with market percentile.

**Request Body:**
```json
{
  "role": "product_manager",
  "experience_years": 3,
  "answers_json": null
}
```

---

### Career Roadmap

#### POST /api/roadmap/generate
Generate personalized career roadmap.

**Request Body:**
```json
{
  "current_role": "Junior PM",
  "target_role": "Senior PM at FAANG",
  "target_company": "Google",
  "timeline_months": 12
}
```

---

### Insider Tips

#### POST /api/tips/search
Search for insider career tips.

**Request Body:**
```json
{
  "topic": "FAANG PM interviews",
  "role": "product_manager",
  "company_type": "faang"
}
```

---

## Error Handling

All endpoints return errors in this format:
```json
{
  "status": "error",
  "message": "Error description"
}
```

## Rate Limits

- 60 requests per minute per IP
- OpenAI API limits apply to AI-powered features
