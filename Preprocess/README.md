# Data preprocess
- data_preprocess.py檔案中分別有兩個function: load_data, read_pdf
- **loda_data**: 負責載入參考資料，並且返回一個字典，其中key為檔案名稱，value為PDF檔內容中的文本
- **read_pdf**: 其中用到了pdfplumber，來幫我們做PDF的讀取，Function主要負責讀取單個PDF文件並返回其文本內容
