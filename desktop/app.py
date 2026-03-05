"""
CareerUp AI - Desktop Application
Powered by PyWebView + Dronor Experts
"""
import webview
import json
import requests
import os
from pathlib import Path

# Dronor API endpoint
DRONOR_API = "http://3.211.238.155:9100/api/expert/run"

class CareerUpAPI:
    """API bridge between JavaScript and Python/Dronor"""
    
    def __init__(self):
        self.openai_key = os.getenv('OPENAI_API_KEY', '')
    
    def set_openai_key(self, key: str) -> dict:
        """Save OpenAI API key"""
        self.openai_key = key
        return {'status': 'success', 'message': 'API key saved'}
    
    def call_expert(self, expert_name: str, params: dict) -> dict:
        """Call a Dronor expert"""
        try:
            # Add OpenAI key to params if needed
            if 'openai_api_key' in params or expert_name in [
                'careerup_interview_coach', 'careerup_resume_optimizer',
                'careerup_linkedin_optimizer', 'careerup_cover_letter_gen',
                'careerup_personality_test', 'careerup_skill_assessor',
                'careerup_roadmap_generator'
            ]:
                params['openai_api_key'] = self.openai_key
            
            response = requests.post(
                DRONOR_API,
                json={
                    'expert_name': expert_name,
                    'params': params
                },
                timeout=120
            )
            
            if response.status_code == 200:
                result = response.json()
                # Parse result if it's a string
                if isinstance(result.get('result'), str):
                    try:
                        result['result'] = eval(result['result'])
                    except:
                        pass
                return result
            else:
                return {'status': 'error', 'message': f'API error: {response.status_code}'}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
    
    # Interview Coach
    def get_interview_question(self, role: str, company_type: str, question_type: str, index: int) -> dict:
        return self.call_expert('careerup_interview_coach', {
            'role': role,
            'company_type': company_type,
            'question_type': question_type,
            'mode': 'generate',
            'question_index': index
        })
    
    def evaluate_answer(self, role: str, company_type: str, question_type: str, index: int, answer: str) -> dict:
        return self.call_expert('careerup_interview_coach', {
            'role': role,
            'company_type': company_type,
            'question_type': question_type,
            'mode': 'evaluate',
            'question_index': index,
            'user_answer': answer
        })
    
    # Resume Optimizer
    def analyze_resume(self, resume_text: str, target_role: str, mode: str = 'full_analysis') -> dict:
        return self.call_expert('careerup_resume_optimizer', {
            'resume_text': resume_text,
            'target_role': target_role,
            'mode': mode
        })
    
    # Personality Test
    def get_personality_questions(self, test_type: str) -> dict:
        return self.call_expert('careerup_personality_test', {
            'test_type': test_type
        })
    
    def analyze_personality(self, test_type: str, answers: dict, target_role: str) -> dict:
        return self.call_expert('careerup_personality_test', {
            'test_type': test_type,
            'answers_json': json.dumps(answers),
            'target_role': target_role
        })
    
    # Insider Tips
    def get_tips(self, role: str = 'any', company: str = 'any', topic: str = 'any', count: int = 5) -> dict:
        return self.call_expert('careerup_insider_tips', {
            'role': role,
            'company': company,
            'topic': topic,
            'count': count
        })
    
    # Roadmap
    def generate_roadmap(self, current_role: str, target_role: str, target_company: str, 
                         timeline_months: int, hours_per_week: int) -> dict:
        return self.call_expert('careerup_roadmap_generator', {
            'current_role': current_role,
            'target_role': target_role,
            'target_company': target_company,
            'timeline_months': timeline_months,
            'hours_per_week': hours_per_week
        })


def main():
    api = CareerUpAPI()
    
    # Get the path to the UI folder
    ui_path = Path(__file__).parent / 'ui'
    index_path = ui_path / 'index.html'
    
    # Create window
    window = webview.create_window(
        title='CareerUp AI',
        url=str(index_path),
        js_api=api,
        width=1200,
        height=800,
        min_size=(900, 600),
        background_color='#1a1a2e'
    )
    
    # Start the application
    webview.start(debug=False)


if __name__ == '__main__':
    main()
