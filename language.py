"""
Enhanced language features implementation for Kingdom Foods website - Complete All Languages
"""

from flask import request, session, g, current_app

# Define available languages and their codes
LANGUAGES = {
    'en': 'English',
    'vi': 'Vietnamese',
    'lo': 'Lao',
    'th': 'Thai'
}

# Translation dictionaries for different languages
TRANSLATIONS = {
    'en': {
        # Site information
        'site_name': 'Kingdom Foods',
        'site_description': 'International Food Products',
        
        # Header
        'nav_thailand': 'Thailand',
        'nav_vietnam': 'Vietnam',
        'nav_laos': 'Laos',
        'nav_contact': 'Contact Us',
        'nav_home': 'Home',
        
        # Homepage
        'hero_title': 'Welcome to Kingdom Foods',
        'hero_subtitle': 'Your trusted supplier of premium food products from Laos, Vietnam, and Thailand',
        'about_heading': 'About Us',
        'about_subheading': 'Bringing the finest Southeast Asian flavors to the world',
        'about_text1': 'Kingdom Foods specializes in sourcing and distributing high-quality food products from Laos, Vietnam, and Thailand. With our extensive network of suppliers and rigorous quality control standards, we ensure that only the best products reach our customers.',
        'about_text2': 'Our mission is to introduce the unique flavors of Southeast Asia to international markets while supporting local farmers and producers.',
        'categories_heading': 'Our Services',
        'categories_subheading': 'Explore what we offer',
        'category_thai': 'Thailand',
        'category_thai_desc': 'Premium selections from Thailand',
        'category_vietnam': 'Vietnam',
        'category_vietnam_desc': 'Traditional products from Vietnam',
        'category_laos': 'Laos',
        'category_laos_desc': 'Authentic flavors from Laos',
        'explore_btn': 'Explore',
        'certifications_heading': 'Our Certifications',
        'certifications_subheading': 'Quality assurance you can trust',
        
        # Pages
        'pages_thai_heading': 'Thailand',
        'pages_thai_subheading': 'Authentic and high-quality products from Thailand',
        'pages_vietnam_heading': 'Vietnam',
        'pages_vietnam_subheading': 'Authentic and high-quality products from Vietnam',
        'pages_laos_heading': 'Laos',
        'pages_laos_subheading': 'Authentic and high-quality products from Laos',
        
        # Contact page
        'contact_heading': 'Contact Us',
        'contact_subheading': 'Get in touch with our team',
        'contact_form_heading': 'Send us a message',
        'field_title': 'Title',
        'field_company': 'Company',
        'field_website': 'Website',
        'field_address': 'Address',
        'field_name': 'Full Name',
        'field_phone': 'Phone Number',
        'field_email': 'Email Address',
        'field_business': 'Your Business Model',
        'field_message': 'Message',
        'required': 'Required',
        'option_select': '-- Select --',
        'option_retail': 'Retail',
        'option_wholesale': 'Wholesale',
        'option_distributor': 'Distributor',
        'option_manufacturer': 'Manufacturer',
        'option_other': 'Other',
        'send_btn': 'Send',
        
        # Thank you page
        'thankyou_title': 'Thank You for Contacting Us!',
        'thankyou_message1': 'Your message has been sent successfully. Our team will review your inquiry and get back to you as soon as possible.',
        'thankyou_message2': 'A confirmation has been sent to the email address you provided.',
        'return_home': 'Return to Homepage',
        'explore_products': 'Explore Our Services',
        
        # Error messages
        'required_fields': 'Please fill in all required fields: {0}',
        'email_error': 'An error occurred while sending the email. Please try again later.',
        'email_success': 'Your message has been sent successfully. Thank you for contacting us!',
        
        # Footer
        'copyright': '© {0} Kingdom Foods. All rights reserved.',
        'footer_contact': 'Contact Information',
        'footer_address': 'Address',
        'footer_phone': 'Phone',
        'footer_email': 'Email',
        
        # Error pages
        '404_title': 'Page Not Found',
        '404_message': 'The page you are looking for might have been removed, had its name changed, or is temporarily unavailable.',
        '500_title': 'Server Error',
        '500_message1': 'Something went wrong on our end. We are working to fix the issue.',
        '500_message2': 'Please try again later or contact us if the problem persists.',
        
        # Slideshow
        'slide1_title': 'Premium Southeast Asian Foods',
        'slide1_desc': 'Authentic flavors from Thailand, Vietnam, and Laos',
        'slide2_title': 'Quality Guaranteed',
        'slide2_desc': 'Carefully selected products from trusted suppliers',
        'slide3_title': 'International Distribution',
        'slide3_desc': 'Bringing Southeast Asian flavors to the world',
        
        # Contact form
        'contact_info_heading': 'Our Contact Information',
        'business_hours': 'Business Hours',
        'business_hours_weekdays': 'Monday - Friday: 8:30 AM - 5:30 PM',
        'business_hours_weekend': 'Saturday: 9:00 AM - 1:00 PM, Sunday: Closed',
        'field_required': 'This field is required',
        'invalid_email': 'Please enter a valid email address',
        'sending': 'Sending...',
        
        # Thank you page
        'email_confirmation': 'Email Confirmation',
        'thankyou_message3': 'If you have any further questions, please do not hesitate to contact us.',
    },
    'vi': {
        # Site information
        'site_name': 'Kingdom Foods',
        'site_description': 'Sản Phẩm Thực Phẩm Quốc Tế',
        
        # Header
        'nav_thailand': 'Thái Lan',
        'nav_vietnam': 'Việt Nam',
        'nav_laos': 'Lào',
        'nav_contact': 'Liên Hệ',
        'nav_home': 'Trang Chủ',
        
        # Homepage
        'hero_title': 'Chào mừng đến với Kingdom Foods',
        'hero_subtitle': 'Nhà cung cấp tin cậy các sản phẩm thực phẩm cao cấp từ Lào, Việt Nam và Thái Lan',
        'about_heading': 'Về Chúng Tôi',
        'about_subheading': 'Mang hương vị Đông Nam Á tuyệt vời nhất đến thế giới',
        'about_text1': 'Kingdom Foods chuyên tìm nguồn cung ứng và phân phối các sản phẩm thực phẩm chất lượng cao từ Lào, Việt Nam và Thái Lan. Với mạng lưới nhà cung cấp rộng khắp và tiêu chuẩn kiểm soát chất lượng nghiêm ngặt, chúng tôi đảm bảo chỉ những sản phẩm tốt nhất đến tay khách hàng.',
        'about_text2': 'Sứ mệnh của chúng tôi là giới thiệu hương vị độc đáo của Đông Nam Á ra thị trường quốc tế đồng thời hỗ trợ nông dân và nhà sản xuất địa phương.',
        'categories_heading': 'Dịch Vụ Của Chúng Tôi',
        'categories_subheading': 'Khám phá những gì chúng tôi cung cấp',
        'category_thai': 'Thái Lan',
        'category_thai_desc': 'Sản phẩm cao cấp từ Thái Lan',
        'category_vietnam': 'Việt Nam',
        'category_vietnam_desc': 'Sản phẩm truyền thống từ Việt Nam',
        'category_laos': 'Lào',
        'category_laos_desc': 'Hương vị đích thực từ Lào',
        'explore_btn': 'Khám Phá',
        'certifications_heading': 'Chứng Nhận Của Chúng Tôi',
        'certifications_subheading': 'Đảm bảo chất lượng bạn có thể tin tưởng',
        
        # Pages
        'pages_thai_heading': 'Thái Lan',
        'pages_thai_subheading': 'Sản phẩm đích thực và chất lượng cao từ Thái Lan',
        'pages_vietnam_heading': 'Việt Nam',
        'pages_vietnam_subheading': 'Sản phẩm đích thực và chất lượng cao từ Việt Nam',
        'pages_laos_heading': 'Lào',
        'pages_laos_subheading': 'Sản phẩm đích thực và chất lượng cao từ Lào',
        
        # Contact page
        'contact_heading': 'Liên Hệ',
        'contact_subheading': 'Liên hệ với đội ngũ của chúng tôi',
        'contact_form_heading': 'Gửi tin nhắn cho chúng tôi',
        'field_title': 'Tiêu đề',
        'field_company': 'Công ty',
        'field_website': 'Website',
        'field_address': 'Địa chỉ',
        'field_name': 'Họ và tên',
        'field_phone': 'Số điện thoại',
        'field_email': 'Địa chỉ email',
        'field_business': 'Mô hình kinh doanh của bạn',
        'field_message': 'Nội dung',
        'required': 'Bắt buộc',
        'option_select': '-- Chọn --',
        'option_retail': 'Bán lẻ',
        'option_wholesale': 'Bán buôn',
        'option_distributor': 'Nhà phân phối',
        'option_manufacturer': 'Nhà sản xuất',
        'option_other': 'Khác',
        'send_btn': 'Gửi',
        
        # Thank you page
        'thankyou_title': 'Cảm Ơn Bạn Đã Liên Hệ!',
        'thankyou_message1': 'Tin nhắn của bạn đã được gửi thành công. Đội ngũ của chúng tôi sẽ xem xét yêu cầu của bạn và phản hồi trong thời gian sớm nhất.',
        'thankyou_message2': 'Một xác nhận đã được gửi đến địa chỉ email bạn đã cung cấp.',
        'return_home': 'Trở Về Trang Chủ',
        'explore_products': 'Khám Phá Dịch Vụ',
        
        # Error messages
        'required_fields': 'Vui lòng điền đầy đủ thông tin: {0}',
        'email_error': 'Có lỗi xảy ra khi gửi email. Vui lòng thử lại sau.',
        'email_success': 'Tin nhắn của bạn đã được gửi thành công. Cảm ơn bạn đã liên hệ với chúng tôi!',
        
        # Footer
        'copyright': '© {0} Kingdom Foods. Tất cả các quyền được bảo lưu.',
        'footer_contact': 'Thông Tin Liên Hệ',
        'footer_address': 'Địa Chỉ',
        'footer_phone': 'Điện Thoại',
        'footer_email': 'Email',
        
        # Error pages
        '404_title': 'Không Tìm Thấy Trang',
        '404_message': 'Trang bạn đang tìm kiếm có thể đã bị xóa, thay đổi tên hoặc tạm thời không khả dụng.',
        '500_title': 'Lỗi Máy Chủ',
        '500_message1': 'Đã xảy ra lỗi ở phía chúng tôi. Chúng tôi đang làm việc để khắc phục sự cố.',
        '500_message2': 'Vui lòng thử lại sau hoặc liên hệ với chúng tôi nếu vấn đề vẫn tiếp diễn.',
        
        # Slideshow
        'slide1_title': 'Thực Phẩm Đông Nam Á Cao Cấp',
        'slide1_desc': 'Hương vị đích thực từ Thái Lan, Việt Nam, và Lào',
        'slide2_title': 'Đảm Bảo Chất Lượng',
        'slide2_desc': 'Sản phẩm chọn lọc kỹ lưỡng từ nhà cung cấp tin cậy',
        'slide3_title': 'Phân Phối Quốc Tế',
        'slide3_desc': 'Mang hương vị Đông Nam Á đến khắp thế giới',
        
        # Contact form
        'contact_info_heading': 'Thông Tin Liên Hệ Của Chúng Tôi',
        'business_hours': 'Giờ Làm Việc',
        'business_hours_weekdays': 'Thứ Hai - Thứ Sáu: 8:30 - 17:30',
        'business_hours_weekend': 'Thứ Bảy: 9:00 - 13:00, Chủ Nhật: Đóng cửa',
        'field_required': 'Trường này là bắt buộc',
        'invalid_email': 'Vui lòng nhập địa chỉ email hợp lệ',
        'sending': 'Đang gửi...',
        
        # Thank you page
        'email_confirmation': 'Xác Nhận Email',
        'thankyou_message3': 'Nếu bạn có bất kỳ câu hỏi nào khác, vui lòng liên hệ với chúng tôi.',
    },
    'lo': {
        # Site information
        'site_name': 'Kingdom Foods',
        'site_description': 'ຜະລິດຕະພັນອາຫານສາກົນ',
        
        # Header
        'nav_thailand': 'ໄທ',
        'nav_vietnam': 'ຫວຽດນາມ',
        'nav_laos': 'ລາວ',
        'nav_contact': 'ຕິດຕໍ່ພວກເຮົາ',
        'nav_home': 'ໜ້າຫຼັກ',
        
        # Homepage
        'hero_title': 'ຍິນດີຕ້ອນຮັບສູ່ Kingdom Foods',
        'hero_subtitle': 'ຜູ້ຈັດຈຳໜ່າຍອາຫານຄຸນນະພາບສູງຈາກລາວ, ຫວຽດນາມ, ແລະ ໄທ',
        'about_heading': 'ກ່ຽວກັບພວກເຮົາ',
        'about_subheading': 'ນຳລົດຊາດທີ່ດີທີ່ສຸດຂອງອາຊີຕາເວັນອອກສ່ຽງໃຕ້ສູ່ໂລກ',
        'about_text1': 'Kingdom Foods ຊ່ຽວຊານໃນການຈັດຫາ ແລະ ຈັດຈຳໜ່າຍຜະລິດຕະພັນອາຫານຄຸນນະພາບສູງຈາກລາວ, ຫວຽດນາມ, ແລະ ໄທ. ດ້ວຍເຄືອຂ່າຍຜູ້ສະໜອງອາຫານທີ່ກວ້າງຂວາງ ແລະ ມາດຕະຖານການຄວບຄຸມຄຸນນະພາບທີ່ເຂັ້ມງວດ, ພວກເຮົາຮັບປະກັນວ່າມີແຕ່ຜະລິດຕະພັນທີ່ດີທີ່ສຸດເທົ່ານັ້ນທີ່ຈະໄປຮອດລູກຄ້າຂອງພວກເຮົາ.',
        'about_text2': 'ພາລະກິດຂອງພວກເຮົາແມ່ນເພື່ອແນະນຳລົດຊາດເອກະລັກຂອງອາຊີຕາເວັນອອກສ່ຽງໃຕ້ໃຫ້ກັບຕະຫຼາດສາກົນ ໃນຂະນະດຽວກັນກໍ່ສະໜັບສະໜຸນຊາວກະສິກອນ ແລະ ຜູ້ຜະລິດໃນທ້ອງຖິ່ນ.',
        'categories_heading': 'ບໍລິການຂອງພວກເຮົາ',
        'categories_subheading': 'ສຳຫຼວດສິ່ງທີ່ພວກເຮົາສະເໜີ',
        'category_thai': 'ໄທ',
        'category_thai_desc': 'ການຄັດເລືອກພິເສດຈາກໄທ',
        'category_vietnam': 'ຫວຽດນາມ',
        'category_vietnam_desc': 'ຜະລິດຕະພັນດັ້ງເດີມຈາກຫວຽດນາມ',
        'category_laos': 'ລາວ',
        'category_laos_desc': 'ລົດຊາດດັ້ງເດີມຈາກລາວ',
        'explore_btn': 'ສຳຫຼວດ',
        'certifications_heading': 'ໃບຢັ້ງຢືນຂອງພວກເຮົາ',
        'certifications_subheading': 'ການຮັບປະກັນຄຸນນະພາບທີ່ທ່ານໄວ້ວາງໃຈໄດ້',
        
        # Pages
        'pages_thai_heading': 'ໄທ',
        'pages_thai_subheading': 'ຜະລິດຕະພັນດັ້ງເດີມແລະຄຸນນະພາບສູງຈາກໄທ',
        'pages_vietnam_heading': 'ຫວຽດນາມ',
        'pages_vietnam_subheading': 'ຜະລິດຕະພັນດັ້ງເດີມແລະຄຸນນະພາບສູງຈາກຫວຽດນາມ',
        'pages_laos_heading': 'ລາວ',
        'pages_laos_subheading': 'ຜະລິດຕະພັນດັ້ງເດີມແລະຄຸນນະພາບສູງຈາກລາວ',
        
        # Contact form fields
        'contact_heading': 'ຕິດຕໍ່ພວກເຮົາ',
        'contact_subheading': 'ຕິດຕໍ່ກັບທີມງານຂອງພວກເຮົາ',
        'contact_form_heading': 'ສົ່ງຂໍ້ຄວາມຫາພວກເຮົາ',
        'contact_info_heading': 'ຂໍ້ມູນການຕິດຕໍ່ຂອງພວກເຮົາ',
        'field_title': 'ຫົວຂໍ້',
        'field_company': 'ບໍລິສັດ',
        'field_website': 'ເວັບໄຊທ໌',
        'field_address': 'ທີ່ຢູ່',
        'field_name': 'ຊື່ເຕັມ',
        'field_phone': 'ເບີໂທລະສັບ',
        'field_email': 'ທີ່ຢູ່ອີເມວ',
        'field_business': 'ຮູບແບບທຸລະກິດຂອງທ່ານ',
        'field_message': 'ຂໍ້ຄວາມ',
        'required': 'ຈຳເປັນ',
        'option_select': '-- ເລືອກ --',
        'option_retail': 'ຂາຍຍ່ອຍ',
        'option_wholesale': 'ຂາຍສົ່ງ',
        'option_distributor': 'ຕົວແທນຈຳໜ່າຍ',
        'option_manufacturer': 'ຜູ້ຜະລິດ',
        'option_other': 'ອື່ນໆ',
        'send_btn': 'ສົ່ງ',
        
        # Form validations
        'required_fields': 'ກະລຸນາຕື່ມຂໍ້ມູນໃສ່ເຂົ້າໃນຊ່ອງຕ່າງໆທີ່ຈຳເປັນ: {0}',
        'email_error': 'ມີຂໍ້ຜິດພາດເກີດຂຶ້ນໃນຂະນະສົ່ງອີເມວ. ກະລຸນາລອງໃໝ່ໃນພາຍຫຼັງ.',
        'email_success': 'ຂໍ້ຄວາມຂອງທ່ານຖືກສົ່ງສຳເລັດແລ້ວ. ຂອບໃຈທີ່ຕິດຕໍ່ຫາພວກເຮົາ!',
        'field_required': 'ຊ່ອງນີ້ຈຳເປັນຕ້ອງໃສ່',
        'invalid_email': 'ກະລຸນາໃສ່ທີ່ຢູ່ອີເມວທີ່ຖືກຕ້ອງ',
        'sending': 'ກຳລັງສົ່ງ...',

        # Thank You
        'thankyou_title': 'ຂອບໃຈທີ່ຕິດຕໍ່ຫາພວກເຮົາ!',
        'thankyou_message1': 'ຂໍ້ຄວາມຂອງທ່ານໄດ້ຖືກສົ່ງສຳເລັດແລ້ວ. ທີມງານຂອງພວກເຮົາຈະກວດຄຳຖາມຂອງທ່ານ ແລະ ຕິດຕໍ່ກັບຄືນໂດຍໄວທີ່ສຸດເທົ່າທີ່ຈະເປັນໄປໄດ້.',
        'thankyou_message2': 'ການຢັ້ງຢືນໄດ້ຖືກສົ່ງໄປຫາທີ່ຢູ່ອີເມລທີ່ທ່ານໃຫ້ໄວ້.',
        'return_home': 'ກັບໄປຫນ້າຫຼັກ',
        'explore_products': 'ສຳຫຼວດບໍລິການຂອງພວກເຮົາ',
        'email_confirmation': 'ການຢັ້ງຢືນທາງອີເມລ',
        'thankyou_message3': 'ຖ້າທ່ານມີຄຳຖາມເພີ່ມເຕີມ, ກະລຸນາຢ່າລັງເລທີ່ຈະຕິດຕໍ່ຫາພວກເຮົາ.',
        
        # Footer
        'copyright': '© {0} Kingdom Foods. ສະຫງວນລິຂະສິດທັງໝົດ.',
        'footer_contact': 'ຂໍ້ມູນການຕິດຕໍ່',
        'footer_address': 'ທີ່ຢູ່',
        'footer_phone': 'ໂທລະສັບ',
        'footer_email': 'ອີເມວ',
        
        # Error pages
        '404_title': 'ບໍ່ພົບໜ້າທີ່ຕ້ອງການ',
        '404_message': 'ໜ້າທີ່ທ່ານກຳລັງຊອກຫາອາດຈະຖືກລຶບ, ປ່ຽນຊື່, ຫຼື ບໍ່ສາມາດເຂົ້າເຖິງໄດ້ຊົ່ວຄາວ.',
        '500_title': 'ຂໍ້ຜິດພາດຂອງເຊີບເວີ',
        '500_message1': 'ມີບາງສິ່ງບາງຢ່າງຜິດພາດຈາກພວກເຮົາ. ພວກເຮົາກຳລັງເຮັດວຽກເພື່ອແກ້ໄຂບັນຫານີ້.',
        '500_message2': 'ກະລຸນາລອງໃໝ່ໃນພາຍຫຼັງຫຼືຕິດຕໍ່ພວກເຮົາຖ້າບັນຫາຍັງຄົງຢູ່.',
        
        # Slideshow
        'slide1_title': 'ອາຫານເອເຊຍຕາເວັນອອກສ່ຽງໃຕ້ຄຸນນະພາບສູງ',
        'slide1_desc': 'ລົດຊາດແທ້ຈາກໄທ, ຫວຽດນາມ, ແລະ ລາວ',
        'slide2_title': 'ຮັບປະກັນຄຸນນະພາບ',
        'slide2_desc': 'ຜະລິດຕະພັນທີ່ຄັດເລືອກຢ່າງລະມັດລະວັງຈາກຜູ້ສະໜອງທີ່ເຊື່ອຖືໄດ້',
        'slide3_title': 'ການຈຳໜ່າຍລະຫວ່າງປະເທດ',
        'slide3_desc': 'ນຳລົດຊາດເອເຊຍຕາເວັນອອກສ່ຽງໃຕ້ສູ່ໂລກ',
        
        # Contact form
        'business_hours': 'ເວລາເຮັດວຽກ',
        'business_hours_weekdays': 'ວັນຈັນ - ວັນສຸກ: 8:30 - 17:30',
        'business_hours_weekend': 'ວັນເສົາ: 9:00 - 13:00, ວັນອາທິດ: ປິດ',
    },
    'th': {
        # Site information
        'site_name': 'Kingdom Foods',
        'site_description': 'ผลิตภัณฑ์อาหารนานาชาติ',
        
        # Header
        'nav_thailand': 'ไทย',
        'nav_vietnam': 'เวียดนาม',
        'nav_laos': 'ลาว',
        'nav_contact': 'ติดต่อเรา',
        'nav_home': 'หน้าแรก',
        
        # Homepage
        'hero_title': 'ยินดีต้อนรับสู่ Kingdom Foods',
        'hero_subtitle': 'ผู้จัดจำหน่ายผลิตภัณฑ์อาหารคุณภาพสูงจากลาว เวียดนาม และไทย',
        'about_heading': 'เกี่ยวกับเรา',
        'about_subheading': 'นำรสชาติที่ดีที่สุดของเอเชียตะวันออกเฉียงใต้สู่โลก',
        'about_text1': 'Kingdom Foods เชี่ยวชาญในการจัดหาและจัดจำหน่ายผลิตภัณฑ์อาหารคุณภาพสูงจากลาว เวียดนาม และไทย ด้วยเครือข่ายผู้จัดหาที่กว้างขวางและมาตรฐานการควบคุมคุณภาพที่เข้มงวด เรารับประกันว่ามีเพียงผลิตภัณฑ์ที่ดีที่สุดเท่านั้นที่จะถึงมือลูกค้าของเรา',
        'about_text2': 'พันธกิจของเราคือการแนะนำรสชาติเอกลักษณ์ของเอเชียตะวันออกเฉียงใต้สู่ตลาดนานาชาติ ในขณะเดียวกันก็สนับสนุนเกษตรกรและผู้ผลิตท้องถิ่น',
        'categories_heading': 'บริการของเรา',
        'categories_subheading': 'สำรวจสิ่งที่เรานำเสนอ',
        'category_thai': 'ไทย',
        'category_thai_desc': 'คัดสรรพิเศษจากประเทศไทย',
        'category_vietnam': 'เวียดนาม',
        'category_vietnam_desc': 'ผลิตภัณฑ์ดั้งเดิมจากเวียดนาม',
        'category_laos': 'ลาว',
        'category_laos_desc': 'รสชาติแท้จากลาว',
        'explore_btn': 'สำรวจ',
        'certifications_heading': 'ใบรับรองของเรา',
        'certifications_subheading': 'การรับประกันคุณภาพที่คุณไว้วางใจได้',
        
        # Pages
        'pages_thai_heading': 'ไทย',
        'pages_thai_subheading': 'ผลิตภัณฑ์แท้และคุณภาพสูงจากประเทศไทย',
        'pages_vietnam_heading': 'เวียดนาม',
        'pages_vietnam_subheading': 'ผลิตภัณฑ์แท้และคุณภาพสูงจากเวียดนาม',
        'pages_laos_heading': 'ลาว',
        'pages_laos_subheading': 'ผลิตภัณฑ์แท้และคุณภาพสูงจากลาว',

        # Contact form fields
        'contact_heading': 'ติดต่อเรา',
        'contact_subheading': 'ติดต่อกับทีมของเรา',
        'contact_form_heading': 'ส่งข้อความถึงเรา',
        'contact_info_heading': 'ข้อมูลการติดต่อของเรา',
        'field_title': 'หัวข้อ',
        'field_company': 'บริษัท',
        'field_website': 'เว็บไซต์',
        'field_address': 'ที่อยู่',
        'field_name': 'ชื่อเต็ม',
        'field_phone': 'หมายเลขโทรศัพท์',
        'field_email': 'อีเมล',
        'field_business': 'รูปแบบธุรกิจของคุณ',
        'field_message': 'ข้อความ',
        'required': 'จำเป็น',
        'option_select': '-- เลือก --',
        'option_retail': 'ค้าปลีก',
        'option_wholesale': 'ค้าส่ง',
        'option_distributor': 'ผู้จัดจำหน่าย',
        'option_manufacturer': 'ผู้ผลิต',
        'option_other': 'อื่นๆ',
        'send_btn': 'ส่ง',
    
        # Form validations
        'required_fields': 'กรุณากรอกข้อมูลในช่องที่จำเป็นทั้งหมด: {0}',
        'email_error': 'เกิดข้อผิดพลาดขณะส่งอีเมล กรุณาลองอีกครั้งในภายหลัง',
        'email_success': 'ส่งข้อความของคุณเรียบร้อยแล้ว ขอบคุณที่ติดต่อเรา!',
        'field_required': 'จำเป็นต้องกรอกช่องนี้',
        'invalid_email': 'กรุณาใส่อีเมลที่ถูกต้อง',
        'sending': 'กำลังส่ง...',

        # Thank You
        'thankyou_title': 'ขอบคุณที่ติดต่อเรา!',
        'thankyou_message1': 'ข้อความของคุณถูกส่งเรียบร้อยแล้ว ทีมของเราจะตรวจสอบคำขอของคุณและติดต่อกลับโดยเร็วที่สุด',
        'thankyou_message2': 'การยืนยันได้ถูกส่งไปยังอีเมลที่คุณให้ไว้',
        'return_home': 'กลับสู่หน้าหลัก',
        'explore_products': 'สำรวจบริการของเรา',
        'email_confirmation': 'การยืนยันทางอีเมล',
        'thankyou_message3': 'หากคุณมีคำถามเพิ่มเติม โปรดอย่าลังเลที่จะติดต่อเรา',
        
        # Footer
        'copyright': '© {0} Kingdom Foods. สงวนลิขสิทธิ์ทั้งหมด',
        'footer_contact': 'ข้อมูลการติดต่อ',
        'footer_address': 'ที่อยู่',
        'footer_phone': 'โทรศัพท์',
        'footer_email': 'อีเมล',
        
        # Error pages
        '404_title': 'ไม่พบหน้าที่ค้นหา',
        '404_message': 'หน้าที่คุณกำลังค้นหาอาจถูกลบ เปลี่ยนชื่อ หรือไม่สามารถเข้าถึงได้ชั่วคราว',
        '500_title': 'ข้อผิดพลาดของเซิร์ฟเวอร์',
        '500_message1': 'เกิดข้อผิดพลาดจากฝั่งเรา เรากำลังดำเนินการแก้ไขปัญหานี้',
        '500_message2': 'กรุณาลองใหม่ในภายหลังหรือติดต่อเราหากปัญหายังคงอยู่',
        
        # Slideshow
        'slide1_title': 'อาหารเอเชียตะวันออกเฉียงใต้พรีเมียม',
        'slide1_desc': 'รสชาติแท้จากไทย เวียดนาม และลาว',
        'slide2_title': 'การรับประกันคุณภาพ',
        'slide2_desc': 'ผลิตภัณฑ์ที่คัดสรรอย่างพิถีพิถันจากผู้จัดหาที่เชื่อถือได้',
        'slide3_title': 'การจัดจำหน่ายระหว่างประเทศ',
        'slide3_desc': 'นำรสชาติเอเชียตะวันออกเฉียงใต้สู่โลก',
        
        # Contact form
        'business_hours': 'เวลาทำการ',
        'business_hours_weekdays': 'จันทร์ - ศุกร์: 8:30 - 17:30',
        'business_hours_weekend': 'เสาร์: 9:00 - 13:00, อาทิตย์: ปิด',
    }
}

def get_locale():
    """Determine the best language to use"""
    # 1. Check URL parameter first
    lang = request.args.get('lang')
    if lang and lang in LANGUAGES:
        session['lang'] = lang
        return lang
    
    # 2. Check session
    if 'lang' in session and session['lang'] in LANGUAGES:
        return session['lang']
    
    # 3. Check Accept-Language header
    if request.accept_languages:
        for lang_code, _ in request.accept_languages:
            if lang_code in LANGUAGES:
                session['lang'] = lang_code
                return lang_code
    
    # 4. Default to English
    return 'en'

def translate(key, *args):
    """Get a translated string for the current locale"""
    lang = getattr(g, 'lang', 'en')
    translations = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    text = translations.get(key, key)
    
    if args:
        try:
            return text.format(*args)
        except:
            return text
    
    return text

def language_selector_middleware():
    """Middleware to set language in global context before each request"""
    g.lang = get_locale()

def register_template_functions(app):
    """Register template functions for Jinja2"""
    @app.template_filter('get_lang')
    def get_lang_filter():
        return getattr(g, 'lang', 'en')
    
    @app.template_global('t')
    def t_function(key, *args):
        return translate(key, *args)
    
    @app.context_processor
    def inject_languages():
        return {
            'LANGUAGES': LANGUAGES,
            'current_lang': getattr(g, 'lang', 'en'),
            't': translate
        }