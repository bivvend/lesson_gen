import os
from utils import generate_directory_structures
import defines
#Create the directory structures for the course structure
#Creates a default List file

if __name__ == "__main__":
    base_directory = os.path.dirname(os.path.abspath(__file__))
    base_directory = os.path.join(base_directory, defines.COURSE_STRUCTURE_DIR)
    print(f"Creating  course structure directory structures in {base_directory}")
    generate_directory_structures.create_directories_and_empty_structure(base_directory)