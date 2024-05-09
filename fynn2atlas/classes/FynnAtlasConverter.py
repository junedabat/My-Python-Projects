class FynnAtlasConverter:
  def __init__(self, file_to_convert : str, to_format : str, output_file : str, end_tags_inclusion: bool) -> None:
    self.file_to_convert = file_to_convert
    self.output_file = output_file

    self.handle_conversion(to_format, end_tags_inclusion)


  def handle_conversion(self, to_format : str, end_tags_inclusion : bool) -> None:
    if to_format == "atlas":
      self.check_end_tags_inclusion(end_tags_inclusion)
      self.convert_data_to_atlas()
    elif to_format == "fynn":
      self.convert_atlas_to_data()
    else: print("Invalid format")
  

  def check_end_tags_inclusion(self, end_tag_arg : str) -> None:
    if end_tag_arg:
      print(f"End tags enabled! {end_tag_arg}")
      self.end_tags_enabled = True
    else: 
      print(f"End tags disabled! {end_tag_arg}")
      self.end_tags_enabled = False


  # Oversees the conversion of a file from data to atlas
  def convert_data_to_atlas(self) -> None:
    # Open the file to read, and create the output file
    print(f"Opening {self.file_to_convert}")
    read_file = open(self.file_to_convert, encoding = "utf-8")
    print("Open!")

    print("Creating the output file...")
    write_file = open(f"export/{self.output_file}", "w", encoding = "utf-8")
    print(f"Created {write_file.name}!")

    print("Reading the input file...")
    # Cycle through the input file
    for line in read_file:
      # Read a line and convert it
      data : list = self.extract_data_from_line(line)
      print(f"Found {data}")
      key : str = data[0]
      message : str = self.convert_line_skips(data[1])
      converted_line : str = self.convert_data_line_to_atlas(key, message)

      print(f"{data} converted! Writing...")
      # Write the converted content into the output file
      write_file.write(converted_line)
    print(f"All done! Exported converted data into {write_file.name}")
    # Close the files
    read_file.close()
    write_file.close()


  def convert_atlas_to_data(self) -> None:
    pass

  # Takes a string and outputs a list of elements that are separated by "="
  # (e.g: Input: "msg1=Legeaater" -> Output: ["msg1","Legeaater"]
  def extract_data_from_line(self, line : str) -> list:
    return line.replace("\n","").split("=")


  def convert_line_skips(self, message : str) -> str:
    return message.replace("/","<LINE>\n")


  def convert_data_line_to_atlas(self, key : str, message : str) -> str:
    end_tag = ""
    if self.end_tags_enabled:
      end_tag = "<END>"
    return f"#W16({key})\n{message}{end_tag}\n\n"
