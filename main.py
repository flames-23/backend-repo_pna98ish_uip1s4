import os
from typing import List, Optional, Dict, Any
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="sync.in API", description="AI-powered career counseling backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "sync.in backend is running"}


@app.get("/api/hello")
def hello():
    return {"message": "Hello from sync.in API"}


# ---------- Roadmap Flow ("I know what I want") ----------
class RoadmapInput(BaseModel):
    career: str
    age: Optional[int] = None
    passions_or_skills: Optional[List[str]] = None
    education_level: Optional[str] = None
    lifestyle_or_salary: Optional[str] = None


def course_suggestions(career: str) -> List[Dict[str, str]]:
    c = career.lower()
    catalog = {
        "software": [
            {"title": "CS50: Intro to Computer Science (Free)", "url": "https://cs50.harvard.edu/x/"},
            {"title": "Full-Stack Open (Free)", "url": "https://fullstackopen.com"},
            {"title": "The Odin Project (Free)", "url": "https://www.theodinproject.com"},
            {"title": "Frontend Masters Paths (Paid)", "url": "https://frontendmasters.com/learn/"},
        ],
        "data": [
            {"title": "Kaggle Micro-Courses (Free)", "url": "https://www.kaggle.com/learn"},
            {"title": "Google Data Analytics (Coursera)", "url": "https://www.coursera.org/professional-certificates/google-data-analytics"},
            {"title": "fast.ai Practical Deep Learning (Free)", "url": "https://course.fast.ai"},
        ],
        "design": [
            {"title": "DesignCourse UI/UX (YouTube)", "url": "https://www.youtube.com/@DesignCourse"},
            {"title": "Google UX Design (Coursera)", "url": "https://www.coursera.org/professional-certificates/google-ux-design"},
            {"title": "Figma Crash Course (Free)", "url": "https://www.youtube.com/watch?v=FTFaQWZBqQ8"},
        ],
        "marketing": [
            {"title": "Meta Social Media Marketing (Coursera)", "url": "https://www.coursera.org/professional-certificates/meta-social-media-marketing"},
            {"title": "HubSpot Academy (Free)", "url": "https://academy.hubspot.com/"},
        ],
        "finance": [
            {"title": "Corporate Finance Institute (Mixed)", "url": "https://courses.corporatefinanceinstitute.com/"},
            {"title": "Basics of Stock Market (Zerodha Varsity)", "url": "https://zerodha.com/varsity/"},
        ],
        "medicine": [
            {"title": "NEET UG/PG Prep Resources", "url": "https://www.prepladder.com/"},
            {"title": "WHO Open Courses", "url": "https://openwho.org/"},
        ],
    }
    for key, items in catalog.items():
        if key in c:
            return items
    # default
    return [
        {"title": "How to Plan Your Career (Free eBook)", "url": "https://www.coursera.org/articles/career-development"},
        {"title": "LinkedIn Learning Popular Courses", "url": "https://www.linkedin.com/learning/"},
    ]


def tool_suggestions(career: str) -> List[str]:
    c = career.lower()
    if "software" in c or "developer" in c or "engineering" in c:
        return ["Git/GitHub", "VS Code", "Node.js", "React", "Postman", "Docker (basics)"]
    if "data" in c or "ml" in c or "ai" in c:
        return ["Python", "Pandas", "NumPy", "scikit-learn", "Jupyter", "SQL", "Tableau"]
    if "design" in c or "ux" in c:
        return ["Figma", "Adobe XD", "Notion", "Miro", "Zeplin"]
    if "marketing" in c or "growth" in c:
        return ["Google Analytics", "Meta Ads", "Canva", "Notion", "Ahrefs/SEMrush"]
    return ["Google Workspace", "Notion", "Canva", "Trello"]


def side_projects(career: str) -> List[str]:
    c = career.lower()
    if "software" in c or "developer" in c:
        return ["Build a personal website", "Clone a popular app", "Contribute to open-source", "Ship 3 micro-projects in 3 weeks"]
    if "data" in c:
        return ["Kaggle competitions", "Analyze public datasets (COVID, IPL)", "End-to-end ML pipeline", "Build a portfolio dashboard"]
    if "design" in c:
        return ["Redesign a popular app", "Create a design system", "Run 3 usability tests", "Publish case studies on Behance"]
    if "marketing" in c:
        return ["Grow a niche Instagram page", "SEO case study for a local biz", "Email funnel experiment", "Run A/B ads with small budget"]
    return ["Document your learning on LinkedIn", "Volunteer for a student club", "Assist a startup for 1 month"]


def internships_to_target(career: str) -> List[str]:
    c = career.lower()
    if any(k in c for k in ["software", "developer", "engineering"]):
        return ["SDE Intern at product startups", "Open-source fellowships", "Campus tech roles"]
    if "data" in c:
        return ["Data Analyst Intern", "ML Research Intern", "Business Intelligence Intern"]
    if "design" in c:
        return ["Product Design Intern", "UX Research Intern", "Visual Design Intern"]
    if "marketing" in c:
        return ["Growth Intern", "Content/SEO Intern", "Performance Marketing Intern"]
    return ["Operations Intern", "Generalist Intern at early-stage startup"]


def certifications(career: str) -> List[str]:
    c = career.lower()
    if "cloud" in c or "devops" in c:
        return ["AWS Cloud Practitioner", "Azure Fundamentals"]
    if "data" in c:
        return ["Google Data Analytics", "AWS ML Specialty (advanced)"]
    if "marketing" in c:
        return ["Google Analytics IQ", "Meta Blueprint"]
    return []


def mistakes_to_avoid(career: str) -> List[str]:
    return [
        "Trying to learn everything at once",
        "Skipping fundamentals",
        "Not building a visible portfolio",
        "Ignoring networking and referrals",
        "Procrastinating on applications"
    ]


def salary_ranges(career: str, education: Optional[str]) -> Dict[str, str]:
    base = career.title()
    return {
        "entry": "₹3L–8L per year (varies by city and company)",
        "mid": "₹8L–20L per year",
        "senior": "₹20L+ per year with strong portfolio and interviews",
        "note": f"Indicative range for {base} roles in India"
    }


def timeline_stages(career: str) -> List[Dict[str, Any]]:
    return [
        {"stage": "Foundation (0–2 months)", "focus": ["Basics", "Core tools", "1 small project"]},
        {"stage": "Build (2–4 months)", "focus": ["2–3 portfolio projects", "Feedback loops", "Share online"]},
        {"stage": "Apply (4–6 months)", "focus": ["Internships", "Referrals", "Mock interviews"]},
        {"stage": "Breakthrough (6–9 months)", "focus": ["Targeted roles", "Certifications (optional)", "Freelance/part-time gig"]},
    ]


@app.post("/api/roadmap")
def generate_roadmap(payload: RoadmapInput):
    career = payload.career.strip()
    data = {
        "career": career,
        "skills_to_learn": tool_suggestions(career),
        "courses": course_suggestions(career),
        "tools_to_master": tool_suggestions(career),
        "side_projects": side_projects(career),
        "internships": internships_to_target(career),
        "certifications": certifications(career),
        "mistakes_to_avoid": mistakes_to_avoid(career),
        "timeline": timeline_stages(career),
        "salary_ranges": salary_ranges(career, payload.education_level),
        "portfolio_tips": [
            "Keep it simple: 3 solid projects > 10 half-done ones",
            "Write short case-studies explaining decisions",
            "Use a clean personal website + GitHub/Behance",
            "Ask 3 seniors to review your work and iterate",
        ],
        "first_opportunity": [
            "Apply to 5 roles/day with tailored resumes",
            "DM hiring managers with your best project",
            "Leverage alumni groups, Discords, LinkedIn",
        ],
        "meta": payload.dict(),
    }
    return data


# ---------- Discovery Flow ("I don't know yet") ----------
class QuizQuestion(BaseModel):
    id: str
    text: str
    type: str  # "single" | "multi" | "scale"
    options: Optional[List[str]] = None


class DiscoverTest(BaseModel):
    id: str
    title: str
    vibe: str
    questions: List[QuizQuestion]


@app.get("/api/discover/tests", response_model=List[DiscoverTest])
def get_tests():
    tests: List[DiscoverTest] = [
        DiscoverTest(
            id="personality",
            title="Personality Splash",
            vibe="Are you the strategist, the builder, or the vibe curator?",
            questions=[
                QuizQuestion(id="p1", text="Pick your energy", type="single", options=["Calm planner", "Curious hacker", "People magnet", "Aesthetic nerd"]),
                QuizQuestion(id="p2", text="You’re happiest when…", type="single", options=["Solving puzzles", "Designing visuals", "Leading a team", "Analysing trends"]),
            ],
        ),
        DiscoverTest(
            id="interests",
            title="Interest Finder",
            vibe="What topics make you lose track of time?",
            questions=[
                QuizQuestion(id="i1", text="Choose 2 that excite you", type="multi", options=["Apps/Web", "AI/Data", "Design", "Finance", "Marketing", "Medicine", "Content"]),
            ],
        ),
        DiscoverTest(
            id="strengths",
            title="Strengths Map",
            vibe="Your natural power-ups",
            questions=[
                QuizQuestion(id="s1", text="Your top strength", type="single", options=["Logic", "Creativity", "Empathy", "Numbers", "Storytelling"]),
            ],
        ),
        DiscoverTest(
            id="aptitude",
            title="Aptitude Mini-Game",
            vibe="A tiny brain teaser",
            questions=[
                QuizQuestion(id="a1", text="Complete the pattern: 2, 4, 8, ?", type="single", options=["12", "14", "16", "18"]),
            ],
        ),
        DiscoverTest(
            id="prefs",
            title="Work Vibes",
            vibe="How do you like working?",
            questions=[
                QuizQuestion(id="w1", text="Ideal setting", type="single", options=["Remote", "Hybrid", "Office", "Outdoor"]),
                QuizQuestion(id="w2", text="You prefer", type="single", options=["Stable salary", "High-risk high-reward", "Impact + learning"]),
            ],
        ),
    ]
    return tests


class DiscoverAnswers(BaseModel):
    answers: Dict[str, Any]


@app.post("/api/discover/evaluate")
def evaluate_discovery(payload: DiscoverAnswers):
    ans = payload.answers or {}
    interests = set(map(str.lower, ans.get("i1", []))) if isinstance(ans.get("i1", []), list) else set()
    persona = str(ans.get("p1", "")).lower()
    strength = str(ans.get("s1", "")).lower()

    scores = {
        "Software Developer": 0,
        "Data Scientist": 0,
        "Product Designer": 0,
        "Digital Marketer": 0,
        "Finance Analyst": 0,
        "Content Strategist": 0,
        "Doctor": 0,
    }

    if "apps/web" in interests:
        scores["Software Developer"] += 2
    if "ai/data" in interests:
        scores["Data Scientist"] += 2
    if "design" in interests:
        scores["Product Designer"] += 2
    if "marketing" in interests:
        scores["Digital Marketer"] += 2
    if "finance" in interests:
        scores["Finance Analyst"] += 2
    if "content" in interests:
        scores["Content Strategist"] += 2
    if "medicine" in interests:
        scores["Doctor"] += 2

    if "curious" in persona or "hacker" in persona:
        scores["Software Developer"] += 1
        scores["Data Scientist"] += 1
    if "aesthetic" in persona:
        scores["Product Designer"] += 1
    if "people" in persona:
        scores["Digital Marketer"] += 1

    if strength in ["logic", "numbers"]:
        scores["Software Developer"] += 1
        scores["Data Scientist"] += 1
        scores["Finance Analyst"] += 1
    if strength in ["creativity", "storytelling"]:
        scores["Product Designer"] += 1
        scores["Digital Marketer"] += 1
        scores["Content Strategist"] += 1
    if strength == "empathy":
        scores["Doctor"] += 1
        scores["Product Designer"] += 1

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    best = [r[0] for r in ranked[:3]]
    avoid = [r[0] for r in ranked[-2:]]

    def courses_for(role: str) -> List[Dict[str, str]]:
        return course_suggestions(role)

    out = {
        "best_fit_careers": best,
        "careers_to_avoid": avoid,
        "ask_salary_prompt": "Want to see salary ranges for these roles?",
        "ask_full_roadmap_prompt": "Want a complete personalized roadmap?",
        "ask_counselor_prompt": "Prefer a real human to guide you? We got you.",
        "courses_to_start_now": {r: courses_for(r) for r in best},
    }
    return out


@app.get("/test")
def test_database():
    response = {
        "backend": "✅ Running",
        "database": "❌ Not Available",
        "database_url": None,
        "database_name": None,
        "connection_status": "Not Connected",
        "collections": []
    }
    try:
        from database import db
        if db is not None:
            response["database"] = "✅ Available"
            response["database_url"] = "✅ Configured"
            response["database_name"] = db.name if hasattr(db, 'name') else "✅ Connected"
            response["connection_status"] = "Connected"
            try:
                collections = db.list_collection_names()
                response["collections"] = collections[:10]
                response["database"] = "✅ Connected & Working"
            except Exception as e:
                response["database"] = f"⚠️  Connected but Error: {str(e)[:50]}"
        else:
            response["database"] = "⚠️  Available but not initialized"
    except ImportError:
        response["database"] = "❌ Database module not found (run enable-database first)"
    except Exception as e:
        response["database"] = f"❌ Error: {str(e)[:50]}"

    response["database_url"] = "✅ Set" if os.getenv("DATABASE_URL") else "❌ Not Set"
    response["database_name"] = "✅ Set" if os.getenv("DATABASE_NAME") else "❌ Not Set"
    return response


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
