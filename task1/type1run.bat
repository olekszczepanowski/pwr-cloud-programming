start cmd /k "title Consumer1_1 && python -m consumer1.app.main"
timeout /t 1
start cmd /k "title Consumer1_2 && python -m consumer1.app.main"
timeout /t 1
start cmd /k "title Publisher1_1 && python -m publisher1.app.main"
timeout /t 1
start cmd /k "title Publisher1_2 && python -m publisher1.app.main"
timeout /t 1
start cmd /k "title Publisher1_3 && python -m publisher1.app.main"

