// CareerUp AI API Types

export interface ApiResponse<T> {
  status: 'success' | 'error';
  message?: string;
  data?: T;
}

// Interview Coach
export interface InterviewRequest {
  role: 'product_manager' | 'software_engineer' | 'data_scientist' | 'designer';
  company_type: 'faang' | 'startup' | 'enterprise' | 'consulting';
  question_type: 'behavioral' | 'technical' | 'case';
  mode: 'generate' | 'evaluate';
  user_answer?: string;
  question_index: number;
}

export interface InterviewQuestion {
  status: string;
  question: string;
  tip: string;
  question_index: number;
  total_questions: number;
}

export interface InterviewEvaluation {
  status: string;
  evaluation: {
    overall_score: number;
    percentile: number;
    criteria_scores: Record<string, { score: number; feedback: string }>;
    strengths: string[];
    weaknesses: string[];
    improved_version: string;
    quick_fixes: string[];
    insider_tip: string;
  };
  summary: string;
}

// Resume Optimizer
export interface ResumeRequest {
  resume_text: string;
  target_role: string;
  target_company?: string;
}

export interface ResumeAnalysis {
  ats_score: number;
  recruiter_score: number;
  keyword_match: string[];
  missing_keywords: string[];
  improvements: string[];
  optimized_sections: Record<string, string>;
}

// Personality Test
export interface PersonalityQuestion {
  id: number;
  question: string;
  options: Array<{
    value: string;
    text: string;
    trait: string;
  }>;
}

export interface PersonalityResult {
  personality_type: string;
  perception: {
    first_impression: string;
    strengths: string[];
    concerns: string[];
  };
  percentile: string;
  fixes: string[];
  strategy: Record<string, string>;
  shareable_summary: string;
}

// Skill Assessment
export interface SkillQuestion {
  id: number;
  skill: string;
  question: string;
  type: string;
}

export interface SkillResult {
  individual_scores: Array<{
    question_id: number;
    score: number;
    feedback: string;
  }>;
  skill_radar: Record<string, number>;
  percentile: string;
  strengths: string[];
  improvements: string[];
}

// Career Roadmap
export interface RoadmapRequest {
  current_role: string;
  target_role: string;
  target_company?: string;
  timeline_months: number;
}

export interface RoadmapResult {
  weeks: Array<{
    week: number;
    focus: string;
    tasks: string[];
    resources: Array<{ title: string; url: string; type: string }>;
  }>;
  milestones: string[];
  success_probability: string;
}
