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


class LessonSlide(BaseModel):
    slideNumber: int = Field(..., gt=0)
    title: str
    topic: str
    layout: str
    background: Background
    content: Content
    animations: Optional[List[Animation]] = []
    speakerNotes: Optional[str] = None


# Example Usage
example_slide_data = {
    "slideNumber": 1,
    "title": "Newton's First Law of Motion",
    "topic": "Forces and Motion",
    "layout": "title_and_content",
    "background": {"color": "#FFFFFF"},
    "content": {
        "text": {
            "heading": {
                "text": "An Object in Motion Stays in Motion...",
                "fontSize": 32,
                "fontColor": "#000000",
                "bold": True,
                "alignment": "center"
            },
            "body": {
                "text": "Newton's First Law states that an object will remain at rest or in uniform motion unless acted upon by an external force.",
                "fontSize": 24,
                "fontColor": "#333333",
                "alignment": "left",
                "bulletPoints": [
                    "Objects resist changes in motion (inertia).",
                    "No force = no change in velocity.",
                    "Real-world examples: seatbelts, hockey pucks."
                ]
            }
        },
        "equations": [
            {
                "latex": "F = ma",
                "description": "Newton's Second Law formula, introduced in later slides."
            }
        ],
        "images": [
            {
                "src": "https://example.com/images/newtons_cradle.jpg",
                "alt": "Newton's Cradle demonstrating inertia",
                "position": "right",
                "size": {"width": "40%", "height": "auto"}
            }
        ],
        "videos": []
    },
    "animations": [
        {"type": "fade_in", "target": "heading", "duration": "1s"},
        {"type": "slide_in", "target": "body", "direction": "left", "duration": "1.5s"}
    ],
    "speakerNotes": "Explain inertia using real-world examples. Emphasize how forces affect motion."
}

lesson_slide = LessonSlide(**example_slide_data)
print(lesson_slide.model_dump_json(indent=4))

