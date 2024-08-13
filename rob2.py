from RPA.JavaAccessBridge import JavaAccessBridge
import argparse
from locators import locators 
parser = argparse.ArgumentParser()
parser.add_argument("--command")
args = parser.parse_args()
print(locators)

jab = JavaAccessBridge()
print(jab.list_java_windows())
jab.select_window("asda")
jab.type_text(
   locators["text"],
    args.command,
    enter=True,
    clear=True,
)

jab.type_text(
    locators["text"],
    args.command,
    index=1,
    clear=True,
    typing=False,

)
jab.click_element(locators["send"])