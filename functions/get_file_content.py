import os


MAX_CHARS = 10000


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Reads and returns the contents of a file within the working directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The path to the file to read, relative to the working directory.",
                },
            },
            "required": ["file_path"],
        },
    },
}








def get_file_content(working_directory: str, file_path: str) -> str:
  try:
    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.join(working_dir_abs,file_path)
    target_file = os.path.normpath(target_file)
    common_path = os.path.commonpath([working_dir_abs,target_file])
    if common_path != working_dir_abs:
      return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"

    if os.path.isfile(target_file) != True:
      return f"Error: File not found or is not a regular file: \"{file_path}\""

    with open(target_file, "r") as f:
      content = f.read(MAX_CHARS)
      if f.read(1):
        x = (f"[...File \"{file_path}\" truncated at {MAX_CHARS} characters]")
        content += x
      return content

  except Exception as f:
    return f"Error: {f}"
