import os


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files and directories in a specified directory, including their sizes and whether each item is a directory.",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "The directory path to list, relative to the working directory. Defaults to the working directory itself.",
                },
            },
        },
    },
}



def get_files_info(working_directory: str, directory: str = ".") -> str:
  try:
      working_dir_abs = os.path.abspath(working_directory)
      target_dir = os.path.join(working_dir_abs , directory)
      target_dir = os.path.normpath(target_dir)
      common_path = os.path.commonpath([target_dir, working_dir_abs])
      valid_target_dir = None
      if common_path == working_dir_abs:
        valid_target_dir = True
      else:
        valid_target_dir = False
        x = f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
        return x

      if os.path.isdir(target_dir) != True:
        x = f"Error: \"{directory}\" is not a directory"
        return x

      items = os.listdir(target_dir)

      lines = []



      for item in items:
        item_path = os.path.join(target_dir, item)
        file_size = os.path.getsize(item_path)
        is_dir = os.path.isdir(item_path)
        lines.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")


      x = "\n".join(lines)

      return x

  except Exception as e:
    return f"Error: {e}"
