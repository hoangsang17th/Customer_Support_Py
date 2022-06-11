# Face Recognition use OpenCV
### Overview:
Tự động xác nhận những khách hàng đã đến cửa hàng dựa trên sự huấn luyên dữ liệu hình ảnh đã có sẵn(training) dựa trên thư viện OpenCV và hệ thống có thể tìm kiếm thông tin, dữ liệu khách hàng. 
Từ đó cửa hàng sẽ phân công các nhân viên liên quan đến để hỗ trợ khách hàng một cách nhanh chóng và chính xác.  
Hệ thống có thể hoạt động với số lượng lớn khách hàng từ 10 người trở lên đến cùng lúc, độ chính xác tương đối cao và an toàn.

use shop
go
SET IDENTITY_INSERT dbo.EMPLOYEE ON
insert into dbo.EMPLOYEE (employee_id, employee_code, employee_name) Values (19, 'B57', 'Trần Ngọc Thành')

select * from dbo.EMPLOYEE ON

pyuic5 -x UIs/ConfigCustomer.ui -o Views/ConfigCustomer.py
pyuic5 -x UIs/ConfigEmployee.ui -o Views/ConfigEmployee.py
pyuic5 -x UIs/ConfigInvoice.ui -o Views/ConfigInvoice.py
pyuic5 -x UIs/ConfigItem.ui -o Views/ConfigItem.py
pyuic5 -x UIs/App.ui -o Views/App.py