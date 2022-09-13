import subprocess
from alive_progress import alive_bar


with alive_bar(title="😎💵", spinner="fish2") as bar:
    subprocess.call("/home/dimitar/Desktop/web_scrapper/run_script.sh")
    bar()
