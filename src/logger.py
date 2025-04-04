import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)


'''
Why is this Logging Required?

Debugging: Logging provides detailed insights into the program’s flow and helps trace where and why errors occur.

Monitoring: Logs record important events and states during execution, which can be useful for monitoring application performance and behavior.

Auditing: They offer a record of activities that can be reviewed later, useful for auditing or post-mortem analysis in case of issues.

Maintenance: Clear logs simplify the maintenance process by allowing developers to quickly pinpoint issues without stepping through code with a debugger.
'''