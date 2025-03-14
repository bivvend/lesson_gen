from pydantic import BaseModel
from typing import List, Optional


class LessonActivity(BaseModel):
    duration: str
    activity: str


class LessonStructure(BaseModel):
    starter: LessonActivity
    mainActivities: List[LessonActivity]
    plenary: LessonActivity


class Homework(BaseModel):
    task: str
    dueDate: str


class LessonPlan(BaseModel):
    lessonTitle: str
    lessonCode: str
    subject: str
    topic: str
    level: str
    yearGroup: str
    term: str
    duration: str
    date: str
    summary: str
    contentItems: List[str]
    learningObjectives: List[str]
    materials: List[str]
    lessonStructure: LessonStructure
    assessmentMethods: List[str]
    homework: Homework
    teacherNotes: Optional[str] = None

    

#Json structure for lesson plans
lesson_plan_structure ={
  "lessonTitle": "",
  "lessonCode": "",
  "subject": "",
  "topic": "",
  "level": "",
  "yearGroup": "",
  "term": "",
  "duration": "",
  "date": "",
  "summary": "",
  "contentItems": [
    ""
  ],
  "learningObjectives": [
    ""
  ],
  "materials": [
    ""
  ],
  "lessonStructure": {
    "starter": {
      "duration": "",
      "activity": ""
    },
    "mainActivities": [
      {
        "duration": "",
        "activity": ""
      },
    ],
    "plenary": {
      "duration": "",
      "activity": ""
    }
  },
  "assessmentMethods": [
    "",
  ],
  "homework": {
    "task": "",
    "dueDate": ""
  },
  "teacherNotes": ""
}
