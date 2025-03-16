start cmd /k "title Publisher3 && python -m publisher3.app.main"
timeout /t 1
start cmd /k "title Consumer4 && python -m consumer4.app.main"
timeout /t 1
start cmd /k "title Consumer3_Publisher4 && python -m consumer3_publisher4.app.main"