"""
CareerUp AI - Desktop Application
Direct OpenAI API Integration (no Dronor dependency)
"""
import webview
import json
import requests
import os
from pathlib import Path

OPENAI_API = "https://api.openai.com/v1/chat/completions"

class CareerUpAPI:
    """API bridge between JavaScript and Python/OpenAI"""
    
    def __init__(self):
        self.openai_key = os.getenv('OPENAI_API_KEY', '')
    
    def set_openai_key(self, key: str) -> dict:
        """Save OpenAI API key"""
        self.openai_key = key
        # Test the key
        test = self._call_openai("Say 'OK' if you can hear me", max_tokens=10)
        if 'error' in test:
            return {'status': 'error', 'message': f'Invalid API key: {test["error"]}'}
        return {'status': 'success', 'message': 'API key saved and verified!'}
    
    def _call_openai(self, prompt: str, system: str = "You are a helpful career coach.", 
                     max_tokens: int = 2000, json_mode: bool = True) -> dict:
        """Direct OpenAI API call"""
        if not self.openai_key:
            return {'error': 'No API key set. Please add your OpenAI key in Settings.'}
        
        try:
            headers = {
                'Authorization': f'Bearer {self.openai_key}',
                'Content-Type': 'application/json'
            }
            
            payload = {
                'model': 'gpt-4o-mini',
                'messages': [
                    {'role': 'system', 'content': system},
                    {'role': 'user', 'content': prompt}
                ],
                'max_tokens': max_tokens,
                'temperature': 0.7
            }
            
            if json_mode:
                payload['response_format'] = {'type': 'json_object'}
            
            response = requests.post(OPENAI_API, headers=headers, json=payload, timeout=60)
            
            if response.status_code == 401:
                return {'error': 'Invalid API key (401 Unauthorized)'}
            elif response.status_code == 429:
                return {'error': 'Rate limit exceeded. Please wait a moment.'}
            elif response.status_code != 200:
                return {'error': f'API error: {response.status_code}'}
            
            result = response.json()
            content = result['choices'][0]['message']['content']
            
            if json_mode:
                return json.loads(content)
            return {'text': content}
            
        except json.JSONDecodeError:
            return {'error': 'Failed to parse AI response'}
        except Exception as e:
            return {'error': str(e)}
    
    # ==================== INTERVIEW COACH ====================
    def get_interview_question(self, role: str, company_type: str, question_type: str, index: int) -> dict:
        prompt = f"""Generate an interview question for:
- Role: {role}
- Company Type: {company_type}  
- Question Type: {question_type}
- Question Number: {index + 1}

Return JSON with:
{{
    "question": "The interview question",
    "tip": "Insider tip on how to approach this question",
    "what_they_look_for": "What interviewers evaluate with this question"
}}"""
        
        result = self._call_openai(prompt, system="You are an expert interview coach who has conducted 1000+ interviews at top tech companies.")
        
        if 'error' in result:
            return {'status': 'error', 'message': result['error']}
        return {'status': 'success', 'result': result}
    
    def evaluate_answer(self, role: str, company_type: str, question_type: str, index: int, answer: str) -> dict:
        prompt = f"""Evaluate this interview answer:

Role: {role}
Company: {company_type}
Question Type: {question_type}
User's Answer: {answer}

Score using STAR method (Situation, Task, Action, Result).
Return JSON:
{{
    "overall_score": <0-100>,
    "percentile": "Top X% of candidates",
    "criteria_scores": {{
        "Clarity": {{"score": <0-25>, "feedback": "..."}},
        "Relevance": {{"score": <0-25>, "feedback": "..."}},
        "Structure": {{"score": <0-25>, "feedback": "..."}},
        "Impact": {{"score": <0-25>, "feedback": "..."}}
    }},
    "improved_version": "Rewritten better answer",
    "quick_fixes": ["Fix 1", "Fix 2", "Fix 3"]
}}"""
        
        result = self._call_openai(prompt, system="You are a senior interviewer at Google/Meta evaluating candidates strictly but fairly.")
        
        if 'error' in result:
            return {'status': 'error', 'message': result['error']}
        return {'status': 'success', 'result': result}
    
    # ==================== RESUME OPTIMIZER ====================
    def analyze_resume(self, resume_text: str, target_role: str, mode: str = 'full_analysis') -> dict:
        prompt = f"""Analyze this resume for the role: {target_role}

RESUME:
{resume_text}

Return JSON:
{{
    "ats_score": <0-100>,
    "strengths": ["Strength 1", "Strength 2"],
    "weaknesses": ["Weakness 1", "Weakness 2"],
    "missing_keywords": ["keyword1", "keyword2"],
    "suggested_improvements": ["Improvement 1", "Improvement 2"],
    "rewritten_summary": "Optimized professional summary"
}}"""
        
        result = self._call_openai(prompt, system="You are an ATS expert and resume optimizer with 15 years experience in tech recruiting.")
        
        if 'error' in result:
            return {'status': 'error', 'message': result['error']}
        return {'status': 'success', 'result': result}
    
    # ==================== PERSONALITY TEST ====================
    def get_personality_questions(self, test_type: str) -> dict:
        prompt = f"""Generate 5 personality/behavioral assessment questions for: {test_type}

Return JSON:
{{
    "questions": [
        {{
            "question": "Question text",
            "options": ["Option A", "Option B", "Option C", "Option D"]
        }}
    ]
}}"""
        
        result = self._call_openai(prompt, system="You are an industrial-organizational psychologist creating interview assessments.")
        
        if 'error' in result:
            return {'status': 'error', 'message': result['error']}
        return {'status': 'success', 'result': result}
    
    def analyze_personality(self, test_type: str, answers: dict, target_role: str) -> dict:
        prompt = f"""Analyze personality test results for {target_role}:

Test Type: {test_type}
Answers: {json.dumps(answers)}

Return JSON:
{{
    "profile_type": "Type name (e.g., Strategic Visionary)",
    "strengths": ["Strength 1", "Strength 2"],
    "growth_areas": ["Area 1", "Area 2"],
    "interview_advice": "How to present yourself",
    "potential_red_flags": "What interviewers might worry about",
    "role_fit_score": <0-100>
}}"""
        
        result = self._call_openai(prompt, system="You are a behavioral psychologist specializing in career assessment.")
        
        if 'error' in result:
            return {'status': 'error', 'message': result['error']}
        return {'status': 'success', 'result': result}
    
    # ==================== INSIDER TIPS ====================
    def get_tips(self, role: str = 'any', company: str = 'any', topic: str = 'any', count: int = 5) -> dict:
        prompt = f"""Generate {count} insider career tips:
- Role: {role}
- Company Type: {company}
- Topic: {topic}

These should be real, actionable tips like you'd find on Blind or Reddit.

Return JSON:
{{
    "tips": [
        {{
            "category": "Category name",
            "tip": "The actual tip with specific details",
            "source": "Where this insight comes from"
        }}
    ]
}}"""
        
        result = self._call_openai(prompt, system="You are a tech industry insider with connections at FAANG companies sharing real, unfiltered advice.")
        
        if 'error' in result:
            return {'status': 'error', 'message': result['error']}
        return {'status': 'success', 'result': result}
    
    # ==================== ROADMAP ====================
    def generate_roadmap(self, current_role: str, target_role: str, target_company: str,
                         timeline_months: int, hours_per_week: int) -> dict:
        prompt = f"""Create a detailed career roadmap:

From: {current_role}
To: {target_role} at {target_company}
Timeline: {timeline_months} months
Available time: {hours_per_week} hours/week

Return JSON:
{{
    "overview": "High-level strategy",
    "phases": [
        {{
            "phase": "Phase 1: Foundation",
            "weeks": "Weeks 1-4",
            "focus": "Main focus area",
            "tasks": ["Task 1", "Task 2", "Task 3"],
            "resources": ["Resource 1", "Resource 2"]
        }}
    ],
    "milestones": ["Milestone 1", "Milestone 2"],
    "success_metrics": "How to measure progress"
}}"""
        
        result = self._call_openai(prompt, system="You are a career strategist who has helped 500+ people transition to top tech roles.", max_tokens=3000)
        
        if 'error' in result:
            return {'status': 'error', 'message': result['error']}
        return {'status': 'success', 'result': result}


def main():
    api = CareerUpAPI()
    
    ui_path = Path(__file__).parent / 'ui'
    index_path = ui_path / 'index.html'
    
    window = webview.create_window(
        title='CareerUp AI',
        url=str(index_path),
        js_api=api,
        width=1200,
        height=800,
        min_size=(900, 600),
        background_color='#1a1a2e'
    )
    
    webview.start(debug=False)


if __name__ == '__main__':
    main()
