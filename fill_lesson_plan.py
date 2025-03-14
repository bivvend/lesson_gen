import json_structures
import json_structures.lesson_plan_structures
import utils
import defines
import os
import json

import utils.generate_text

#Use OpenAI to fill in the lesson plan 

lessonCode = "PHY_10_01"
subject = defines.SUBJECTS.PHYSICS    
level = defines.LEVELS.GCSE
yearGroup = defines.YEAR_GROUPS_GCSE.YEAR_10
specification = defines.GCSE_SPEC_TEXT

initial_plan = True
critique = True  
improve = True


if __name__  == "__main__":
    #Iterate through the lesson plans folder for the lesson with the matching lesson code
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), defines.LESSON_PLANS_DIR)
    lesson_plan_file = os.path.join(base_dir, subject.name, level.name, yearGroup.name, defines.DRAFTS, f"empty_plan_{lessonCode}.json")
    filled_lesson_plan_file = os.path.join(base_dir, subject.name, level.name, yearGroup.name, defines.DRAFTS, f"filled_plan_{lessonCode}.json")
    critique_file = os.path.join(base_dir, subject.name, level.name, yearGroup.name, defines.DRAFTS, f"critique_{lessonCode}.txt")
    final_lesson_plan_file = os.path.join(base_dir, subject.name, level.name, yearGroup.name,defines.FINAL, f"final_plan_{lessonCode}.json")
    if os.path.exists(lesson_plan_file):
        print(f"Lesson plan file exists: {lesson_plan_file}")

        if initial_plan:
            #Load the lesson plan file
            with open(lesson_plan_file, "r") as f:
                lesson_plan = json.load(f)
                #Fill in the lesson plan using OpenAI
                prompt = [
                    f"You are a UK based {subject} teacher. You are planning a lesson for a {level} class in {yearGroup}. "
                    f"The lesson is about {lesson_plan["lessonTitle"]}.\n",

                    f"A JSON structure defining the lesson plan is provided below: \n",
                    f"{lesson_plan} \n",

                    f"Fill the lesson plan for this lesson. Include the lesson objectives, the lesson activities, "
                    f"the lesson resources, and the lesson assessment. \n",

                    f"You must use the specification below to help you plan the lesson. \n",
                    f"{specification} \n"

                ]
                response_format = json_structures.lesson_plan_structures.LessonPlan
                print(response_format)
                response = utils.generate_text.generate_structured_text(prompt, response_format)
                print(response.model_dump_json())
                #Save the filled lesson plan
                
                with open(filled_lesson_plan_file, "w") as f:
                    f.write(response.model_dump_json(indent=4))
                print(f"Filled lesson plan saved to: {filled_lesson_plan_file}") 
        if critique:
            with open(filled_lesson_plan_file, "r") as f:
                lesson_plan = json.load(f)
                #Fill in the lesson plan using OpenAI
                prompt = [
                    f"You are a mentor for a {subject} teacher. You are writing advice and comments for a {level} class in {yearGroup}. "
                    f"The lesson is about {lesson_plan["lessonTitle"]}.\n",

                    f"A JSON structure defining the lesson plan is provided below: \n",
                    f"{lesson_plan} \n",


                    f"Make specific comments on the lesson plan for this lesson. Ensure you check that all the learning objectives are met, "
                    f"the lesson activities are appropriate, the lesson resources are suitable, and the lesson assessment is effective. \n",
                    f"You should be very tough and critical in your comments. Make stong definte suggestions for improvement and don't be afraid of offending. \n",

                    f"You must use the {level} specification below to help you comment. \n",
                    f"{specification} \n"

                ]
                response = utils.generate_text.generate_text(prompt)
                print(response)
                #Save the filled lesson plan
                
                with open(critique_file, "w") as f:
                    f.write(str(response))
                print(f"Critique saved to: {critique_file}")
        if improve:
            with open(filled_lesson_plan_file, "r") as f:
                with(open(critique_file, "r")) as c:
                    lesson_plan = json.load(f)
                    #Fill in the lesson plan using OpenAI
                    prompt = [
                        f"You are a UK based {subject} teacher. You are planning a lesson for a {level} class in {yearGroup}. "
                        f"The lesson is about {lesson_plan["lessonTitle"]}.\n",

                        f"A JSON structure defining your first version of the lesson plan is provided below: \n",
                        f"{lesson_plan} \n",

                        f"Your mentor has provided the following critique of your lesson plan: \n",
                        f"{c} \n",

                        f"Improve the lesson plan based on the critique. You must address all the comments made by your mentor. \n",

                    ]
                    response_format = json_structures.lesson_plan_structures.LessonPlan
                    print(response_format)
                    response = utils.generate_text.generate_structured_text(prompt, response_format)
                    print(response.model_dump_json())
                    #Save the filled lesson plan
                    
                    with open(final_lesson_plan_file, "w") as f:
                        f.write(response.model_dump_json(indent=4))
                    print(f"Final lesson plan saved to: {final_lesson_plan_file}") 
            
    else:
        print(f"Lesson plan file does not exist: {lesson_plan_file}")
        exit()


