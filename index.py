def modify_content(content):
    return content.upper()

def read_and_write_file():
    input_filename = input("Enter the filename to read: ")
    
    try:
 
        with open(input_filename, "r") as file:
            content = file.read()
            print("File read successfully.")
        
  
        modified_content = modify_content(content)
        
       
        output_filename = input("Enter the filename to write the modified content to: ")
        

        with open(output_filename, "w") as file:
            file.write(modified_content)
            print("Modified content written successfully.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{input_filename}' could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


read_and_write_file()
