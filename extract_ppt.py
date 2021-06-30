import text_processing

from tika import parser
# file = "temp/hornbill1508-191223205319.pdf"
# parsed_data = parser.from_file(file)
# print(parsed_data["metadata"])
# print("__________________________________________------------------------------_______________________________________")
# print(parsed_data["content"])

class data_extracter:
    def __init__(self) -> None:
        self.process = text_processing.process_text()

    def extract(self,file):
        parsed_data = parser.from_file(file)
        pro_df, pro_data = self.process.process(parsed_data["content"])
        return pro_df, pro_data

