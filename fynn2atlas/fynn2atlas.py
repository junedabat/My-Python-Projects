from classes.FynnAtlasConverter import FynnAtlasConverter
import argparse

def check_arguments():
  parser = argparse.ArgumentParser(description='Fynn Atlas Converter')
  parser.add_argument('file_to_convert', type=str)
  parser.add_argument('to_format',type=str)
  parser.add_argument('output_file', type=str)

  class IncludeEndTagsAction(argparse.Action):
    def __init__(self, option_strings, dest, default, nargs=None):
      super().__init__(option_strings, dest, default=default, nargs=nargs)
        
    def __call__(self, parser, namespace, values, option_string=None):
      setattr(namespace, self.dest, True)    
  parser.add_argument('--include_end_tags', action=IncludeEndTagsAction, nargs='?', default=False)
 
  return parser.parse_args()

if __name__ == "__main__":
  args = check_arguments()
  print(args)
  converter = FynnAtlasConverter(file_to_convert = args.file_to_convert,
                                 to_format = args.to_format,
                                 output_file = args.output_file, 
                                 end_tags_inclusion = args.include_end_tags)
