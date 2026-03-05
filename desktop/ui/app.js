// CareerUp AI - Frontend Logic
let currentQuestion = null;
let currentQuestionIndex = 0;
let personalityAnswers = {};
let personalityQuestions = [];

// Navigation
document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => {
        document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
        document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
        item.classList.add('active');
        document.getElementById(item.dataset.section).classList.add('active');
    });
});

// Settings Modal
function showSettings() { document.getElementById('settings-modal').classList.add('show'); }
function hideSettings() { document.getElementById('settings-modal').classList.remove('show'); }

async function saveSettings() {
    const key = document.getElementById('openai-key').value;
    if (key) {
        const result = await window.pywebview.api.set_openai_key(key);
        if (result.status === 'success') {
            alert('API key saved!');
            hideSettings();
        }
    }
}

// Loading
function showLoading() { document.getElementById('loading').classList.add('show'); }
function hideLoading() { document.getElementById('loading').classList.remove('show'); }

// Interview Coach
async function getQuestion() {
    const role = document.getElementById('interview-role').value;
    const company = document.getElementById('interview-company').value;
    const type = document.getElementById('interview-type').value;
    
    showLoading();
    try {
        const result = await window.pywebview.api.get_interview_question(role, company, type, currentQuestionIndex);
        hideLoading();
        
        if (result.status === 'success') {
            const data = result.result;
            currentQuestion = { role, company, type, index: currentQuestionIndex };
            renderQuestion(data);
        } else {
            alert('Error: ' + (result.message || 'Unknown error'));
        }
    } catch (e) {
        hideLoading();
        alert('Error: ' + e.message);
    }
}

function renderQuestion(data) {
    const container = document.getElementById('interview-content');
    container.innerHTML = `
        <div class="question-card">
            <div class="question-label">Interview Question</div>
            <div class="question-text">${data.question}</div>
            <div class="tip-box">
                <strong>💡 Insider Tip:</strong> ${data.tip}
            </div>
        </div>
        <div class="answer-area">
            <label>Your Answer</label>
            <textarea id="user-answer" placeholder="Type your answer here using the STAR method..."></textarea>
            <button class="btn btn-primary" onclick="submitAnswer()">Get Feedback</button>
            <button class="btn btn-secondary" style="margin-left: 10px" onclick="getQuestion()">Skip Question</button>
        </div>
    `;
}

async function submitAnswer() {
    const answer = document.getElementById('user-answer').value;
    if (!answer.trim()) { alert('Please enter your answer'); return; }
    
    showLoading();
    try {
        const result = await window.pywebview.api.evaluate_answer(
            currentQuestion.role, currentQuestion.company, 
            currentQuestion.type, currentQuestion.index, answer
        );
        hideLoading();
        
        if (result.status === 'success') {
            renderFeedback(result.result);
            currentQuestionIndex++;
        } else {
            alert('Error: ' + (result.message || 'Unknown error'));
        }
    } catch (e) {
        hideLoading();
        alert('Error: ' + e.message);
    }
}

function renderFeedback(data) {
    const container = document.getElementById('interview-content');
    const criteriaHtml = Object.entries(data.criteria_scores || {}).map(([name, info]) => `
        <div class="criteria-item">
            <div class="criteria-name">${name}</div>
            <div class="criteria-score">${info.score}/25</div>
            <div class="criteria-feedback">${info.feedback}</div>
        </div>
    `).join('');
    
    const fixesHtml = (data.quick_fixes || []).map(fix => `<div class="quick-fix">${fix}</div>`).join('');
    
    container.innerHTML = `
        <div class="score-card">
            <div class="score-header">
                <div><div class="score-value">${data.overall_score}/100</div><div class="score-label">Overall Score</div></div>
                <div class="percentile">${data.percentile}</div>
            </div>
            <div class="criteria-grid">${criteriaHtml}</div>
        </div>
        <div class="improved-version">
            <h3>✨ Improved Version</h3>
            <p>${data.improved_version || 'N/A'}</p>
        </div>
        <div class="quick-fixes">
            <h3>🎯 Quick Fixes</h3>
            ${fixesHtml}
        </div>
        <div style="margin-top: 20px">
            <button class="btn btn-primary" onclick="getQuestion()">Next Question</button>
        </div>
    `;
}

// Resume Optimizer
async function analyzeResume() {
    const text = document.getElementById('resume-text').value;
    const role = document.getElementById('resume-role').value;
    if (!text.trim()) { alert('Please paste your resume'); return; }
    
    showLoading();
    try {
        const result = await window.pywebview.api.analyze_resume(text, role, 'full_analysis');
        hideLoading();
        if (result.status === 'success') {
            renderResumeResults(result.result);
        } else {
            alert('Error: ' + (result.message || 'Unknown error'));
        }
    } catch (e) {
        hideLoading();
        alert('Error: ' + e.message);
    }
}

function renderResumeResults(data) {
    document.getElementById('resume-results').innerHTML = `
        <div class="score-card">
            <div class="score-header">
                <div><div class="score-value">${data.ats_score || 'N/A'}</div><div class="score-label">ATS Score</div></div>
            </div>
        </div>
        <div class="improved-version">
            <h3>Analysis</h3>
            <pre style="white-space: pre-wrap; font-family: inherit;">${JSON.stringify(data, null, 2)}</pre>
        </div>
    `;
}

// Personality Test
async function startPersonalityTest() {
    const type = document.getElementById('personality-type').value;
    showLoading();
    try {
        const result = await window.pywebview.api.get_personality_questions(type);
        hideLoading();
        if (result.status === 'success') {
            personalityQuestions = result.result.questions || [];
            personalityAnswers = {};
            renderPersonalityQuestions();
        } else {
            alert('Error: ' + (result.message || 'Unknown error'));
        }
    } catch (e) {
        hideLoading();
        alert('Error: ' + e.message);
    }
}

function renderPersonalityQuestions() {
    const container = document.getElementById('personality-content');
    const questionsHtml = personalityQuestions.map((q, i) => `
        <div class="test-question">
            <h4>${i + 1}. ${q.question}</h4>
            <div class="options">
                ${q.options.map((opt, j) => `
                    <label class="option" onclick="selectOption(${i}, ${j}, this)">
                        <input type="radio" name="q${i}" value="${j}">
                        ${opt}
                    </label>
                `).join('')}
            </div>
        </div>
    `).join('');
    
    container.innerHTML = `
        <div class="test-questions">${questionsHtml}</div>
        <button class="btn btn-primary" style="margin-top: 20px" onclick="submitPersonalityTest()">Submit Answers</button>
    `;
}

function selectOption(qIndex, optIndex, el) {
    el.parentElement.querySelectorAll('.option').forEach(o => o.classList.remove('selected'));
    el.classList.add('selected');
    personalityAnswers[`q${qIndex}`] = optIndex;
}

async function submitPersonalityTest() {
    if (Object.keys(personalityAnswers).length < personalityQuestions.length) {
        alert('Please answer all questions');
        return;
    }
    const type = document.getElementById('personality-type').value;
    const role = document.getElementById('personality-role').value || 'Product Manager';
    
    showLoading();
    try {
        const result = await window.pywebview.api.analyze_personality(type, personalityAnswers, role);
        hideLoading();
        if (result.status === 'success') {
            document.getElementById('personality-content').innerHTML = `
                <div class="improved-version">
                    <h3>Your Results</h3>
                    <pre style="white-space: pre-wrap; font-family: inherit;">${JSON.stringify(result.result, null, 2)}</pre>
                </div>
            `;
        }
    } catch (e) {
        hideLoading();
        alert('Error: ' + e.message);
    }
}

// Roadmap
async function generateRoadmap() {
    const current = document.getElementById('roadmap-current').value;
    const target = document.getElementById('roadmap-target').value;
    const company = document.getElementById('roadmap-company').value;
    const timeline = parseInt(document.getElementById('roadmap-timeline').value);
    const hours = parseInt(document.getElementById('roadmap-hours').value);
    
    if (!current || !target) { alert('Please fill current and target roles'); return; }
    
    showLoading();
    try {
        const result = await window.pywebview.api.generate_roadmap(current, target, company, timeline, hours);
        hideLoading();
        if (result.status === 'success') {
            document.getElementById('roadmap-content').innerHTML = `
                <div class="improved-version">
                    <h3>Your Roadmap</h3>
                    <pre style="white-space: pre-wrap; font-family: inherit;">${JSON.stringify(result.result, null, 2)}</pre>
                </div>
            `;
        }
    } catch (e) {
        hideLoading();
        alert('Error: ' + e.message);
    }
}

// Tips
async function getTips() {
    const role = document.getElementById('tips-role').value;
    const company = document.getElementById('tips-company').value;
    const topic = document.getElementById('tips-topic').value;
    
    showLoading();
    try {
        const result = await window.pywebview.api.get_tips(role, company, topic, 5);
        hideLoading();
        if (result.status === 'success') {
            const tips = result.result.tips || [];
            const tipsHtml = tips.map(tip => `
                <div class="tip-card">
                    <div class="tip-category">${tip.category || 'General'}</div>
                    <div class="tip-content">${tip.tip || tip}</div>
                </div>
            `).join('');
            document.getElementById('tips-content').innerHTML = tipsHtml || '<p>No tips found</p>';
        }
    } catch (e) {
        hideLoading();
        alert('Error: ' + e.message);
    }
}
