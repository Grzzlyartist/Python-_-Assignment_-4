import os


def modify_readme(text):
    try:
        # Check if file exists
        if not os.path.exists(text):
            raise FileNotFoundError(f"The file '{text}' does not exist.")
        
        # Check if file is readable
        if not os.access(text, os.R_OK):
            raise PermissionError(f"You don't have permission to read '{text}'.")
        
        # Read the file
        with open(text, 'r') as file:
            content = file.read()
        
        # Create modified content
        modified_content = content + "\n\n## Modified Section\nThis README was automatically modified by a Python script."
        
        # Create output filename
        base_name = os.path.splitext(text)[0]
        output_filename = f"{base_name}_modified.md"
        
        # Write modified content to new file
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Successfully created modified file: {output_filename}")
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("README File Modifier")
    print("--------------------")
    
    # Get filename from user
    filename = input("Please enter the filename of the README file to modify: ")
    
    # Process the file
    modify_readme(filename)

if __name__ == "__main__":
    main()