import os
from utils import generate_directory_structures
import defines
#Create the directory structures for the lesson plans
#Creates a default JSON file for the year's lesson plans

if __name__ == "__main__":
    base_directory = os.path.dirname(os.path.abspath(__file__))
    base_directory = os.path.join(base_directory, defines.LESSON_PLANS_DIR)
    print(f"Creating lesson plan directory structures in {base_directory}")
    generate_directory_structures.create_directories(base_directory)