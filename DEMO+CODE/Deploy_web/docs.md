# Deploy with azure cloud
1) Tạo container registry trên azure web
B1: az login
B2: tạo Dockerfile
B3: az acr build --registry svmsentiment --resource-group webinar --image svmsentreg .

2) Tạo App services -> web app
B1: 



# Nếu gặp lỗi:
1) (TasksOperationsNotAllowed) ACR Tasks requests for the registry svmsentiment and 70ec360a-c4f4-424d-9fee-50d13a937ff4 are not permitted. 
Fix: https://learn.microsoft.com/en-us/answers/questions/1530524/how-to-fix-(tasksoperationsnotallowed)-acr-tasks-r 

