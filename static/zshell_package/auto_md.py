import re,time
write_date = '%s年%s月%s日'%(2019,10,10)#编写时间
Auditing_date = '%s年%s月%s日' % (time.localtime()[0], time.localtime()[1], time.localtime()[2])#修订时间
base_infomation = ''
# 版本
edit_info= ''# 修订信息
# 产品概要说明：例子：产品管理系统是公司运营内部使用的对公司线上产品进行管理对订单进行发布的系统平台。可以对订单进行审核及管理，对产品进行管理，对订单效果进行查询。保证整个运营服务系统的正常流转。
product_summary = ''#产品概要说明
product_name = ''#产品名称
product_slogan = ''#产品slogan
# 产品特色： 简单优雅的设计、良好的交流氛围、丰富的文章主题、Mardown富文本等特色功能
product_feature = ''#产品特色

with open('需求文档.md','r') as file_read:
    content = ''
    for item in file_read:
        item = re.sub(r'\$write_date\$', write_date, item, 1)
        item = re.sub(r'\$Auditing_date\$', Auditing_date, item, 1)
        item = re.sub(r'\$base_infomation\$', base_infomation, item, 1)

        item = re.sub(r'\$edit_info\$', edit_info, item, 1)
        item = re.sub(r'\$product_summary\$', product_summary, item, 1)
        item = re.sub(r'\$product_name\$', product_name, item, 1)
        item = re.sub(r'\$product_slogan\$', product_slogan, item, 1)
        item = re.sub(r'\$product_feature\$', product_feature, item, 1)
        item = re.sub(r'\$Auditing_date\$', Auditing_date, item, 1)
        item = re.sub(r'\$Auditing_date\$', Auditing_date, item, 1)
        item = re.sub(r'\$Auditing_date\$', Auditing_date, item, 1)
        item = re.sub(r'\$Auditing_date\$', Auditing_date, item, 1)
        item = re.sub(r'\$Auditing_date\$', Auditing_date, item, 1)



        content +=item
    with open('../需求文档.md','w') as file_write:
        file_write.write(content)
