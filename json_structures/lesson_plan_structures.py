from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class LearningObjective(BaseModel):
    description: str
    successCriteria: List[str]

class StarterActivity(BaseModel):
    questions: List[str]

class ActivityTypeEnum(str, Enum):
    Explanation = "explanation"
    Discussion = "discussion"
    GroupWork = "group_work"  
    IndividualWork = "individual_work"
    Starter = "starter"
    Plenary = "plenary"
    Assessment = "assessment"  # For activities that assess understanding
    Homework = "homework"  # For activities assigned as homework
    Practical = "practical"  # For hands-on or practical activities
    Research = "research"  # For activities that involve research or investigation
    Quiz = "quiz"  # For activities that involve quizzes or tests
    Project = "project"  # For project-based activities
    Presentation = "presentation"  # For activities that involve presentations
    Game = "game"  # For activities that involve games or gamified learning 
    Simulation = "simulation"  # For activities that involve simulations
    CaseStudy = "case_study"  # For activities that involve case studies
    Reflection = "reflection"  # For activities that involve reflection on learning
    Debate = "debate"  # For activities that involve debates
    PeerReview = "peer_review"  # For activities that involve peer review
    FieldTrip = "field_trip"  # For activities that involve field trips or excursions
    Other = "other"  # For any other type of activity not listed

class LessonActivity(BaseModel):
    duration: str
    topic: str
    sub_topic: Optional[str] = None  # Optional sub-topic for the activity
    activity: str
    activity_type: ActivityTypeEnum  # Type of activity, e.g., explanation, discussion, group work, etc.
    materials: Optional[str] = None  # Optional materials needed for the activity

class StarterLessonActivity(BaseModel):
    topic: str
    sub_topic: Optional[str] = None 
    duration: str

class PlenaryActivity(BaseModel):
    topic: str
    sub_topic: Optional[str] = None 
    duration: str
    take_home_messages: List[str]

class LessonStructure(BaseModel):
    starter: StarterLessonActivity
    main_activities: List[LessonActivity]
    plenary: LessonActivity

class LessonPlan(BaseModel):
    lessonTitle: str
    lessonCode: str
    subject: str
    topic: str
    level: str
    yearGroup: str
    term: str
    duration: str
    summary: str
    link_to_specification: str #Reference to the specification or curriculum document
    link_to_resources: Optional[str] = None  # Optional link to additional resources or materials
    learning_objectives: List[LearningObjective]
    lesson_structure: LessonStructure
    teacher_notes: Optional[str] = None


lesson_plan_structure ={
  "lessonTitle": "", 
  "lessonCode": "",
  "subject": "",
  "topic": "",
  "level": "",
  "yearGroup": "",
  "term": "",
  "duration": "",
  "summary": "",
  "link_to_specification": "",
  "link_to_resources": None,
  "learning_objectives": [
    {
      "description": "",
      "successCriteria": []
    }
  ],
  "lesson_structure": {
    "starter": {
      "topic": "",
      "sub_topic": None,
      "duration": ""
    },
    "main_activities": [
      {
        "duration": "",
        "topic": "",
        "sub_topic": None,
        "activity": "",
        "activity_type": "explanation",
        "materials": None
      }
    ],
    "plenary": {
      "duration": "",
      "topic": "",
      "sub_topic": None,
      "activity": "",
      "activity_type": "plenary",
      "materials": None
    }
  },
  "teacher_notes": None
}



