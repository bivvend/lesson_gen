from pydantic import BaseModel, HttpUrl, Field
from typing import List, Optional


class Background(BaseModel):
    color: Optional[str] = "#FFFFFF"
    image: Optional[HttpUrl] = None


class TextContent(BaseModel):
    text: str
    fontSize: int = Field(..., gt=0)
    fontColor: str = "#000000"
    bold: Optional[bool] = False
    alignment: Optional[str] = "left"
    bulletPoints: Optional[List[str]] = []

class Question(BaseModel):
    question_text: str  # The question text, full formatting as LaTeX or plain text
    question_type: str  # Type of question, e.g., "multiple-choice", "
    answer_options: List[str] # List of answer options for multiple-choice questions
    correct_answer: str
    marks: int  # Marks allocated for the question
    marking_scheme: Optional[str] = None  # Optional marking scheme for the question
    difficulty: Optional[str] = None  # Optional difficulty level of the question
    common_misconceptions: Optional[List[str]] = None  # Optional list of common misconceptions related to the question
    feedback: Optional[str] = None  # Optional feedback for the question

class Equation(BaseModel):
    latex: str
    description: Optional[str] = None


class Image(BaseModel):
    src: HttpUrl
    alt: Optional[str] = None
    position: Optional[str] = "center"
    size: Optional[dict] = {"width": "auto", "height": "auto"}


class Animation(BaseModel):
    type: str
    target: str
    duration: str
    direction: Optional[str] = None


class Content(BaseModel):
    text: Optional[dict] = {
        "heading": None,
        "body": None
    }
    equations: Optional[List[Equation]] = []
    images: Optional[List[Image]] = []
    videos: Optional[List[HttpUrl]] = []
    questions: Optional[List[Question]] = []  # List of questions 


class LessonSlide(BaseModel):
    slideNumber: int = Field(..., gt=0)
    title: str
    topic: str
    layout: str
    background: Background
    content: Content
    speakerNotes: Optional[str] = None


# Example Usage
example_slide_data = {
  "slideNumber": 1,
  "title": "",
  "topic": "",
  "layout": "",
  "background": {
    "color": "#FFFFFF",
    "image": None
  },
  "content": {
    "text": {
      "heading": None,
      "body": None
    },
    "equations": [],
    "images": [],
    "videos": [],
    "questions": []
  },
  "speakerNotes": None
}

