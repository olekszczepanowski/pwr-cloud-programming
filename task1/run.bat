start cmd /k "title Consumer1_1 && python -m consumer1.app.main"
timeout /t 1
start cmd /k "title Consumer1_2 && python -m consumer1.app.main"
timeout /t 1
start cmd /k "title Consumer2 && python -m consumer2.app.main"
timeout /t 1
start cmd /k "title Consumer4 && python -m consumer4.app.main"
timeout /t 1
start cmd /k "title Consumer3_Publisher4 && python -m consumer3_publisher4.app.main"
timeout /t 1
start cmd /k "title Publisher1_1 && python -m publisher1.app.main"
timeout /t 1
start cmd /k "title Publisher1_2 && python -m publisher1.app.main"
timeout /t 1
start cmd /k "title Publisher1_3 && python -m publisher1.app.main"
timeout /t 1
start cmd /k "title Publisher2 && python -m publisher2.app.main"
timeout /t 1
start cmd /k "title Publisher3 && python -m publisher3.app.main"

